#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Google Sheetsデータ取得のみのテスト（tweepy不要）
"""

import os
import requests
from datetime import datetime, timedelta

def get_sheet_data_simple():
    """シンプルなSheetsデータ取得"""
    sheet_id = '1YKHCDU7NswNo5p3UHy6Q5jdTtChoCAXo4B_KTmGjlsI'
    api_key = 'AIzaSyD-S-4B3hTceHcOdASZjuT-Ch9EIiDneEw'
    
    # 今日の日付（日本時間）
    jst = datetime.now() + timedelta(hours=9)
    today = jst.strftime('%Y/%-m/%-d')
    today_padded = jst.strftime('%Y/%m/%d')
    
    print(f"検索する日付: {today} または {today_padded}")
    
    # Sheets APIで全データ取得
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{sheet_id}/values/シート1!A2:F366?key={api_key}"
    
    try:
        print(f"\nAPIリクエスト送信中...")
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        print(f"データ取得成功！ {len(data.get('values', []))}件のデータ")
        
        # 最初の5件を表示
        print("\n最初の5件のデータ:")
        for i, row in enumerate(data.get('values', [])[:5]):
            if row:
                date = row[0] if len(row) > 0 else 'N/A'
                category = row[1] if len(row) > 1 else 'N/A'
                twitter = row[2][:30] + '...' if len(row) > 2 and len(row[2]) > 30 else row[2] if len(row) > 2 else 'N/A'
                print(f"{i+1}. {date} | {category} | {twitter}")
        
        # 今日のデータを検索
        found = False
        for row in data.get('values', []):
            if len(row) >= 3 and (row[0] == today or row[0] == today_padded):
                print(f"\n✅ 今日の投稿データが見つかりました！")
                print(f"日付: {row[0]}")
                print(f"カテゴリー: {row[1] if len(row) > 1 else 'N/A'}")
                print(f"Twitter投稿文: {row[2] if len(row) > 2 else 'N/A'}")
                print(f"投稿済み: {row[5] if len(row) > 5 else 'FALSE'}")
                found = True
                break
        
        if not found:
            print(f"\n❌ 今日（{today}）のデータは見つかりませんでした")
            print("Google Sheetsに今日の日付でデータを追加してください")
        
    except requests.exceptions.HTTPError as e:
        print(f"\nHTTPエラー: {e}")
        print(f"ステータスコード: {response.status_code}")
        print(f"レスポンス: {response.text}")
    except Exception as e:
        print(f"\nエラー: {e}")

if __name__ == "__main__":
    print("Google Sheets データ取得テスト\n")
    print("=" * 50)
    get_sheet_data_simple()