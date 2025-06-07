# SNS自動投稿セットアップガイド

## 完全無料で実現する3つの方法

### 方法1: IFTTT（イフト）を使用【推奨】
**無料枠: 2つのアプレット（Twitter + Instagram）**

#### 設定手順
1. [IFTTT](https://ifttt.com)でアカウント作成
2. 「Create」から新規アプレット作成
3. IF: Google Sheets → 新しい行が追加されたら
4. THEN: Twitter → ツイートを投稿

#### メリット
- 設定が簡単（10分で完了）
- Google Sheetsと直接連携
- 安定性が高い

#### デメリット
- 無料版は2つまで（Twitter/Instagram各1つ）
- 画像投稿は有料版が必要

### 方法2: Zapier（ザピアー）
**無料枠: 月100タスクまで**

#### 設定手順
1. [Zapier](https://zapier.com)でアカウント作成
2. Zap作成：Google Sheets → Twitter/Instagram
3. トリガー：新しい行または更新された行
4. アクション：投稿を作成

#### メリット
- より柔軟な設定が可能
- 条件分岐が使える

#### デメリット
- 月100投稿まで（1日3投稿程度）
- 設定がやや複雑

### 方法3: GitHub Actions + Python【完全無料・上級者向け】

#### 必要なもの
- Twitter Developer Account（無料）
- Instagram Business Account
- Facebook Developer Account（無料）

## GitHub Actionsによる自動化実装

### 1. Twitter自動投稿の設定

#### Twitter Developer登録
1. [developer.twitter.com](https://developer.twitter.com)にアクセス
2. 「Sign up」→ 基本的な用途を選択
3. App作成後、API KeyとAccess Tokenを取得

#### secrets設定（GitHub）
1. リポジトリの Settings → Secrets → Actions
2. 以下を追加：
   - `TWITTER_API_KEY`
   - `TWITTER_API_SECRET`
   - `TWITTER_ACCESS_TOKEN`
   - `TWITTER_ACCESS_TOKEN_SECRET`

### 2. 自動投稿スクリプト

`.github/workflows/auto-post.yml` を作成：

```yaml
name: SNS Auto Post

on:
  schedule:
    # 毎日17:00（日本時間）に実行
    - cron: '0 8 * * *'  # UTC時間で設定
  workflow_dispatch: # 手動実行も可能

jobs:
  post:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Setup Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        pip install tweepy google-api-python-client google-auth
    
    - name: Run posting script
      env:
        TWITTER_API_KEY: ${{ secrets.TWITTER_API_KEY }}
        TWITTER_API_SECRET: ${{ secrets.TWITTER_API_SECRET }}
        TWITTER_ACCESS_TOKEN: ${{ secrets.TWITTER_ACCESS_TOKEN }}
        TWITTER_ACCESS_TOKEN_SECRET: ${{ secrets.TWITTER_ACCESS_TOKEN_SECRET }}
        GOOGLE_SHEETS_ID: '1YKHCDU7NswNo5p3UHy6Q5jdTtChoCAXo4B_KTmGjlsI'
      run: python scripts/auto_post.py
```

### 3. Pythonスクリプト

`scripts/auto_post.py` を作成：

```python
import os
import tweepy
from datetime import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Twitter認証
auth = tweepy.OAuthHandler(
    os.environ['TWITTER_API_KEY'],
    os.environ['TWITTER_API_SECRET']
)
auth.set_access_token(
    os.environ['TWITTER_ACCESS_TOKEN'],
    os.environ['TWITTER_ACCESS_TOKEN_SECRET']
)
api = tweepy.API(auth)

# 今日の投稿を取得してツイート
def post_today():
    today = datetime.now().strftime('%Y/%m/%d')
    
    # ここでGoogle Sheetsから今日のデータを取得
    # 簡略化のため、サンプルテキスト
    tweet_text = f"【{today}の投稿】\n高校受験に向けて今日も頑張りましょう！\n\n#高校受験 #少人数制塾"
    
    try:
        api.update_status(tweet_text)
        print(f"投稿成功: {tweet_text}")
    except Exception as e:
        print(f"エラー: {e}")

if __name__ == "__main__":
    post_today()
```

## 簡単な運用方法（手動＋半自動）

### 1. Buffer（バッファー）無料版
- 3つのSNSアカウントまで
- 月10投稿まで予約可能
- カレンダー表示で管理しやすい

### 2. Later（レイター）無料版
- 1つのSNSセットまで
- 月30投稿まで予約可能
- ビジュアルカレンダーが使いやすい

### 3. 運用フロー
1. 毎週日曜日に1週間分の投稿を準備
2. Google Sheetsで内容を管理
3. BufferやLaterで予約投稿
4. 所要時間：週30分程度

## Instagram投稿の注意点

### 公式APIの制限
- 個人アカウントでは自動投稿不可
- ビジネスアカウント＋Facebook連携が必要
- 画像投稿は特に制限が厳しい

### 代替案
1. **手動投稿を効率化**
   - 画像を事前に作成してストック
   - キャプションをコピペで投稿
   
2. **通知リマインダー**
   - Google Calendarで投稿時間を設定
   - スマホに通知→手動投稿

## 推奨する現実的な運用

### 完全無料で続けやすい方法
1. **Twitter**: IFTTTで自動化（テキストのみ）
2. **Instagram**: 週1回まとめて予約（Later無料版）
3. **管理**: Google Sheetsで一元管理
4. **画像**: Canvaで月初にまとめて作成

### タイムスケジュール例
- 毎月1日：画像30枚作成（2時間）
- 毎週日曜：投稿予約（30分）
- 毎日：効果測定・微調整（5分）

これなら無理なく継続できます！