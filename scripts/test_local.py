#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ローカルテスト用スクリプト
GitHub Actionsと同じ環境を再現してテスト実行
"""

import os
import sys
from datetime import datetime, timedelta

# テスト用の環境変数設定（実際の値に置き換えてください）
test_env = {
    'GOOGLE_SHEETS_ID': '1YKHCDU7NswNo5p3UHy6Q5jdTtChoCAXo4B_KTmGjlsI',
    'GOOGLE_API_KEY': 'AIzaSyD-S-4B3hTceHcOdASZjuT-Ch9EIiDneEw',
    # 以下は実際の値に置き換えてください
    'TWITTER_API_KEY': '',
    'TWITTER_API_SECRET': '',
    'TWITTER_ACCESS_TOKEN': '',
    'TWITTER_ACCESS_TOKEN_SECRET': ''
}

def test_sheet_only():
    """Sheetsデータ取得のみテスト"""
    print("=== Sheetsデータ取得テスト ===")
    
    # 環境変数設定
    os.environ['GOOGLE_SHEETS_ID'] = test_env['GOOGLE_SHEETS_ID']
    os.environ['GOOGLE_API_KEY'] = test_env['GOOGLE_API_KEY']
    
    # auto_post.pyのget_sheet_data関数をインポート
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from auto_post import get_sheet_data
    
    # データ取得テスト
    data = get_sheet_data()
    
    if data:
        print(f"\n取得成功！")
        print(f"日付: {data['date']}")
        print(f"カテゴリー: {data['category']}")
        print(f"Twitter投稿文: {data['twitter'][:50]}...")
        print(f"投稿済み: {data['posted']}")
    else:
        print("\nデータが見つかりませんでした")
        print("Google Sheetsに今日の日付のデータを追加してください")
        
        # 今日の日付を表示
        jst = datetime.now() + timedelta(hours=9)
        print(f"\n今日の日付（JST）: {jst.strftime('%Y/%m/%d')} または {jst.strftime('%Y/%-m/%-d')}")

def test_full():
    """フル機能テスト（要Twitter認証情報）"""
    print("=== フル機能テスト ===")
    
    # すべての環境変数を設定
    for key, value in test_env.items():
        if value:
            os.environ[key] = value
        else:
            print(f"警告: {key} が設定されていません")
    
    # auto_post.pyのmain関数を実行
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from auto_post import main
    
    main()

if __name__ == "__main__":
    print("SNS自動投稿 ローカルテスト\n")
    
    if len(sys.argv) > 1 and sys.argv[1] == "full":
        # Twitter認証情報が設定されているか確認
        if all(test_env.get(key) for key in ['TWITTER_API_KEY', 'TWITTER_API_SECRET', 'TWITTER_ACCESS_TOKEN', 'TWITTER_ACCESS_TOKEN_SECRET']):
            test_full()
        else:
            print("Twitter認証情報を設定してください")
            print("このファイルのtest_env辞書に値を入力してください")
    else:
        # デフォルトはSheetsテストのみ
        test_sheet_only()
        print("\nTwitter投稿もテストする場合:")
        print("1. このファイルのtest_envにTwitter認証情報を設定")
        print("2. python scripts/test_local.py full")