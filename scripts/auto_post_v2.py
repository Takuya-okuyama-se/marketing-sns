#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import tweepy
from datetime import datetime, timedelta
import requests
import json

def get_sheet_data():
    """Google Sheetsから今日の投稿データを取得"""
    sheet_id = os.environ.get('GOOGLE_SHEETS_ID')
    api_key = os.environ.get('GOOGLE_API_KEY')
    
    # 今日の日付（日本時間）
    jst = datetime.now() + timedelta(hours=9)
    today = jst.strftime('%Y/%-m/%-d')
    today_padded = jst.strftime('%Y/%m/%d')
    
    print(f"検索する日付: {today} または {today_padded}")
    
    # Sheets APIで全データ取得
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{sheet_id}/values/シート1!A2:F366?key={api_key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # 今日のデータを検索
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
        return None
        
    except Exception as e:
        print(f"Sheetsデータ取得エラー: {e}")
        return None

def post_to_twitter_v2(text):
    """Twitter API v2を使用して投稿"""
    try:
        # Twitter API v2 クライアント作成
        client = tweepy.Client(
            consumer_key=os.environ['TWITTER_API_KEY'],
            consumer_secret=os.environ['TWITTER_API_SECRET'],
            access_token=os.environ['TWITTER_ACCESS_TOKEN'],
            access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET']
        )
        
        print("Twitter API v2で投稿を試みます...")
        
        # ツイート投稿
        response = client.create_tweet(text=text)
        
        if response.data:
            tweet_id = response.data['id']
            print(f"Twitter投稿成功: https://twitter.com/user/status/{tweet_id}")
            return True
        else:
            print("投稿は完了しましたが、レスポンスが空です")
            return False
            
    except tweepy.TweepyException as e:
        print(f"Twitter API エラー: {e}")
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
        success = post_to_twitter_v2(post_data['twitter'])
        
        if success:
            print("投稿完了！")
        else:
            print("投稿に失敗しました")
            sys.exit(1)
    else:
        print("Twitter投稿文が空です")
    
    print(f"実行終了: {datetime.now()}")

if __name__ == "__main__":
    main()