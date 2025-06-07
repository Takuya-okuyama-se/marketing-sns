# Twitter Developer Account 設定ガイド

## 1. Twitter Developer Account登録（無料）

### ステップ1: Developer Portal アクセス
1. [developer.twitter.com](https://developer.twitter.com) にアクセス
2. 「Sign up」をクリック
3. 通常のTwitterアカウントでログイン

### ステップ2: 開発者申請
1. **User profile** 設定
   - 名前、メールアドレスを確認
   
2. **Describe your use case**
   - "Making a bot" を選択
   - 用途説明（英語）の例：
   ```
   I want to create an automated posting system for my educational institution.
   The bot will share daily educational content and study tips for high school students.
   No spam or aggressive following behavior will be implemented.
   ```

3. **同意して送信**
   - 規約に同意
   - 承認は通常即時（自動承認）

## 2. Twitter App作成

### ステップ1: Create Project
1. Developer Portal の「Projects & Apps」
2. 「Create Project」をクリック
3. プロジェクト名: `juku-sns-bot`

### ステップ2: App設定
1. **App environment**: Production
2. **App name**: `juku-marketing-bot`（一意である必要あり）
3. **Keys and tokens** が表示される

### ステップ3: 必要なキーを保存
以下の4つをメモ（後で使用）：
- **API Key**: `XXXXXXXXXXXXXXXXXXXXXXXXX`
- **API Key Secret**: `XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX`
- **Bearer Token**: （今回は不要）

### ステップ4: Access Token生成
1. 「Keys and tokens」タブ
2. 「Access Token and Secret」セクション
3. 「Generate」をクリック
4. 以下を保存：
   - **Access Token**: `XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX`
   - **Access Token Secret**: `XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX`

## 3. App権限設定

### User authentication settings
1. 「Settings」→「User authentication settings」
2. 「Set up」をクリック
3. **App permissions**: Read and write
4. **Type of App**: Web App, Automated App or Bot
5. **Callback URLs**: `https://takuya-okuyama-se.github.io/marketing-sns/`
6. **Website URL**: `https://takuya-okuyama-se.github.io/marketing-sns/`
7. 「Save」

## 4. GitHub Secretsに登録

### GitHubリポジトリで設定
1. リポジトリの「Settings」タブ
2. 左メニュー「Secrets and variables」→「Actions」
3. 「New repository secret」をクリック
4. 以下を1つずつ追加：

| Secret Name | Value |
|------------|-------|
| TWITTER_API_KEY | APIキーを貼り付け |
| TWITTER_API_SECRET | APIキーシークレットを貼り付け |
| TWITTER_ACCESS_TOKEN | アクセストークンを貼り付け |
| TWITTER_ACCESS_TOKEN_SECRET | アクセストークンシークレットを貼り付け |
| GOOGLE_API_KEY | AIzaSyD-S-4B3hTceHcOdASZjuT-Ch9EIiDneEw |

## 5. 動作確認

### 手動実行でテスト
1. GitHubリポジトリの「Actions」タブ
2. 「SNS Auto Post」ワークフロー
3. 「Run workflow」→「Run workflow」
4. 実行ログを確認

### ローカルでテスト
```bash
# 環境変数を設定してテスト実行
export TWITTER_API_KEY="your_key"
export TWITTER_API_SECRET="your_secret"
export TWITTER_ACCESS_TOKEN="your_token"
export TWITTER_ACCESS_TOKEN_SECRET="your_token_secret"
export GOOGLE_SHEETS_ID="1YKHCDU7NswNo5p3UHy6Q5jdTtChoCAXo4B_KTmGjlsI"
export GOOGLE_API_KEY="AIzaSyD-S-4B3hTceHcOdASZjuT-Ch9EIiDneEw"

python scripts/auto_post.py
```

## 6. よくあるエラーと対処法

### Error: 403 Forbidden
- App権限が「Read only」になっている
- → 「Read and write」に変更

### Error: 401 Unauthorized
- トークンが正しくない
- → 再生成して更新

### Error: Duplicate status
- 同じ内容のツイートは連続投稿不可
- → 投稿内容を少し変える

## 7. 運用開始チェックリスト

- [ ] Twitter Developer Account作成完了
- [ ] App作成と権限設定完了
- [ ] 4つのキー/トークンを取得
- [ ] GitHub Secretsに登録完了
- [ ] Google Sheetsに投稿データ準備
- [ ] Actions手動実行でテスト成功
- [ ] 毎日17:00の自動実行を確認

これで完全自動化の準備完了です！