# Twitter API 403エラーの解決方法

## 🚨 エラーの原因
Twitter API v1.1の`update_status`エンドポイントへのアクセスが制限されています。
新規アプリはAPI v2を使用する必要があります。

## 🔧 解決方法1: スクリプトをAPI v2対応に修正

### 修正版 auto_post.py

```python
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
    today_padded = jst.strftime('%Y/%m/%d')
    
    print(f"検索する日付: {today} または {today_padded}")
    
    # Sheets APIで全データ取得
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{sheet_id}/values/シート1!A2:F366?key={api_key}"
    
    try:
        print(f"\nAPIリクエスト送信中...")
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
        
        # エラーの詳細を表示
        if hasattr(e, 'api_codes'):
            print(f"APIコード: {e.api_codes}")
        if hasattr(e, 'api_messages'):
            print(f"APIメッセージ: {e.api_messages}")
            
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
        
        # API v2で投稿を試みる
        success = post_to_twitter_v2(post_data['twitter'])
        
        if success:
            print("投稿完了！")
            # TODO: Sheetsの「投稿済み」フラグを更新
        else:
            print("投稿に失敗しました")
            sys.exit(1)
    else:
        print("Twitter投稿文が空です")
    
    print(f"実行終了: {datetime.now()}")

if __name__ == "__main__":
    main()
```

### GitHub Actionsのワークフロー更新

`.github/workflows/auto-post.yml`も更新が必要な場合：

```yaml
- name: Install dependencies
  run: |
    pip install tweepy>=4.14.0 google-api-python-client==2.86.0 google-auth==2.17.3 requests
```

## 🔧 解決方法2: Twitter開発者ポータルで権限確認

### アクセスレベルの確認
1. [developer.x.com](https://developer.x.com) にログイン
2. Projects & Apps → あなたのApp
3. 「Settings」タブ
4. 「User authentication settings」

### 必要な設定
- **App permissions**: Read and write
- **Type of App**: Web App, Automated App or Bot

## 🔧 解決方法3: 代替の投稿方法

### requests ライブラリで直接API v2を使用
```python
import requests
import json
from requests_oauthlib import OAuth1

def post_tweet_direct(text):
    """requests で直接Twitter API v2を呼び出す"""
    
    auth = OAuth1(
        os.environ['TWITTER_API_KEY'],
        os.environ['TWITTER_API_SECRET'],
        os.environ['TWITTER_ACCESS_TOKEN'],
        os.environ['TWITTER_ACCESS_TOKEN_SECRET']
    )
    
    url = "https://api.twitter.com/2/tweets"
    payload = {"text": text}
    
    response = requests.post(
        url,
        auth=auth,
        json=payload,
        headers={"Content-Type": "application/json"}
    )
    
    if response.status_code == 201:
        print("投稿成功！")
        return True
    else:
        print(f"エラー: {response.status_code}")
        print(response.text)
        return False
```

## 🎯 推奨される対応

### 即座の解決
1. 上記の修正版スクリプトを`auto_post_v2.py`として保存
2. GitHub Actionsで新しいスクリプトを使用
3. テスト実行

### 長期的な対応
1. Twitter API v2に完全移行
2. Elevated accessの申請（必要な場合）

## ✅ テスト手順

1. **修正版スクリプトを作成**
2. **ローカルでテスト**
   ```bash
   python3 scripts/auto_post_v2.py
   ```
3. **成功したらGitHubにpush**
4. **GitHub Actionsを更新**

これでAPI v2経由で投稿できるようになります！