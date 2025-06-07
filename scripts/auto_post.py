#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import tweepy
from datetime import datetime, timedelta
import requests
import json
import time
import random

def get_sheet_data():
    """Google Sheetsから今日の投稿データを取得"""
    sheet_id = os.environ.get('GOOGLE_SHEETS_ID')
    api_key = os.environ.get('GOOGLE_API_KEY')
    
    # 今日の日付（日本時間）
    jst = datetime.now() + timedelta(hours=9)
    today = jst.strftime('%Y/%-m/%-d')
    
    # 日付の別形式も試す（ゼロパディングあり）
    today_padded = jst.strftime('%Y/%m/%d')
    
    # Sheets APIで全データ取得
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{sheet_id}/values/シート1!A2:F366?key={api_key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # 今日のデータを検索（複数の日付形式に対応）
        for row in data.get('values', []):
            if len(row) >= 3 and (row[0] == today or row[0] == today_padded):
                return {
                    'date': row[0],
                    'category': row[1] if len(row) > 1 else '',
                    'twitter': row[2] if len(row) > 2 else '',
                    'instagram': row[3] if len(row) > 3 else '',
                    'image': row[4] if len(row) > 4 else '',
                    'posted': row[5] if len(row) > 5 else 'FALSE'
                }
        
        print(f"今日（{today} または {today_padded}）の投稿データが見つかりません")
        
        # デバッグ用：最初の5件のデータを表示
        print("\n利用可能なデータ（最初の5件）:")
        for i, row in enumerate(data.get('values', [])[:5]):
            if row:
                print(f"  {i+1}: {row[0]} - {row[1] if len(row) > 1 else 'N/A'}")
        
        return None
        
    except Exception as e:
        print(f"Sheetsデータ取得エラー: {e}")
        return None

def post_to_twitter(text):
    """Twitterに投稿"""
    try:
        # Twitter認証
        auth = tweepy.OAuthHandler(
            os.environ['TWITTER_API_KEY'],
            os.environ['TWITTER_API_SECRET']
        )
        auth.set_access_token(
            os.environ['TWITTER_ACCESS_TOKEN'],
            os.environ['TWITTER_ACCESS_TOKEN_SECRET']
        )
        api = tweepy.API(auth, wait_on_rate_limit=True)
        
        # API接続テスト
        try:
            api.verify_credentials()
            print("Twitter認証成功")
        except Exception as e:
            print(f"Twitter認証エラー: {e}")
            return False
        
        # 重複回避のためのタイムスタンプ追加（必要に応じてコメントアウト解除）
        # text = f"{text}\n\n{datetime.now().strftime('%H:%M')}"
        
        # 画像URLが含まれている場合の処理
        if 'http' in text and ('.jpg' in text or '.png' in text or '.jpeg' in text):
            print("画像URLを含む投稿を検出")
        
        # ツイート投稿
        tweet = api.update_status(text)
        print(f"Twitter投稿成功: https://twitter.com/user/status/{tweet.id}")
        return True
        
    except tweepy.TweepyException as e:
        print(f"Twitter API エラー: {e}")
        if hasattr(e, 'api_codes') and 187 in e.api_codes:
            print("エラー: 重複したツイートです")
        return False
    except Exception as e:
        print(f"予期しないエラー: {e}")
        return False

def main():
    """メイン処理"""
    print(f"実行開始: {datetime.now()}")
    
    # 環境変数チェック
    required_vars = [
        'TWITTER_API_KEY',
        'TWITTER_API_SECRET', 
        'TWITTER_ACCESS_TOKEN',
        'TWITTER_ACCESS_TOKEN_SECRET',
        'GOOGLE_SHEETS_ID',
        'GOOGLE_API_KEY'
    ]
    
    missing_vars = [var for var in required_vars if not os.environ.get(var)]
    if missing_vars:
        print(f"エラー: 必要な環境変数が設定されていません: {missing_vars}")
        sys.exit(1)
    
    # Sheetsからデータ取得
    post_data = get_sheet_data()
    
    if not post_data:
        print("投稿データがないため終了します")
        sys.exit(0)
    
    if post_data['posted'] == 'TRUE':
        print("すでに投稿済みです")
        sys.exit(0)
    
    # Twitter投稿
    if post_data['twitter']:
        print(f"Twitter投稿内容: {post_data['twitter']}")
        success = post_to_twitter(post_data['twitter'])
        
        if success:
            print("投稿完了！")
            # 実際の運用では、ここでSheetsの「投稿済み」フラグを更新
        else:
            print("投稿に失敗しました")
            sys.exit(1)
    else:
        print("Twitter投稿文が空です")
    
    print(f"実行終了: {datetime.now()}")

if __name__ == "__main__":
    main()