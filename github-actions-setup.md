# GitHub Actions 自動投稿セットアップガイド

## セットアップ手順

### 1. Twitter Developer Account作成
`twitter-developer-setup.md`の手順に従って、以下を取得：
- TWITTER_API_KEY
- TWITTER_API_SECRET
- TWITTER_ACCESS_TOKEN
- TWITTER_ACCESS_TOKEN_SECRET

### 2. GitHub Secretsに登録

#### 手順：
1. GitHubで自分のリポジトリを開く
2. 「Settings」タブをクリック
3. 左メニュー「Secrets and variables」→「Actions」
4. 「New repository secret」をクリック
5. 以下を1つずつ追加：

| Name | Value |
|------|-------|
| TWITTER_API_KEY | Twitterで取得したAPIキー |
| TWITTER_API_SECRET | Twitterで取得したAPIシークレット |
| TWITTER_ACCESS_TOKEN | Twitterで取得したアクセストークン |
| TWITTER_ACCESS_TOKEN_SECRET | Twitterで取得したアクセストークンシークレット |
| GOOGLE_API_KEY | AIzaSyD-S-4B3hTceHcOdASZjuT-Ch9EIiDneEw |

### 3. Google Sheetsにデータ準備

投稿データを以下の形式で入力：
| 日付 | カテゴリー | Twitter投稿文 | Instagram投稿文 | 画像説明 | 投稿済み |
|------|------------|---------------|-----------------|----------|----------|
| 2025/1/8 | 勉強法 | 【効率的な暗記法】... | （省略） | （省略） | FALSE |

**重要**: 日付は`2025/1/8`または`2025/01/08`形式で入力

### 4. 動作テスト

#### ローカルテスト（Sheetsデータ取得のみ）
```bash
cd /mnt/c/Users/takuy/marketing
python scripts/test_local.py
```

#### GitHub Actionsで手動実行
1. GitHubリポジトリの「Actions」タブ
2. 「SNS Auto Post」をクリック
3. 右側の「Run workflow」→「Run workflow」
4. 実行結果を確認

### 5. 自動実行の確認

現在の設定：
- **毎日17:00（日本時間）に自動実行**
- `.github/workflows/auto-post.yml`で設定済み

## トラブルシューティング

### よくあるエラー

#### 1. 「Sheetsデータ取得エラー」
- Google SheetsのIDが正しいか確認
- APIキーが有効か確認
- Sheetsが「リンクを知っている全員」に公開されているか確認

#### 2. 「Twitter認証エラー」
- 4つのTwitter認証情報がすべて正しいか確認
- Twitter Appの権限が「Read and write」になっているか確認

#### 3. 「今日の投稿データが見つかりません」
- Sheetsの日付形式を確認（2025/1/8 または 2025/01/08）
- 日本時間とUTC時間の差を考慮

### デバッグ方法

1. **ローカルでテスト実行**
```bash
# Sheetsデータ取得のみテスト
python scripts/test_local.py

# フルテスト（要Twitter認証情報）
# test_local.pyにTwitter認証情報を設定後
python scripts/test_local.py full
```

2. **GitHub Actionsのログ確認**
- Actions → 実行履歴 → 詳細ログ

3. **Sheets APIの動作確認**
ブラウザで直接アクセス：
```
https://sheets.googleapis.com/v4/spreadsheets/1YKHCDU7NswNo5p3UHy6Q5jdTtChoCAXo4B_KTmGjlsI/values/シート1!A2:F366?key=AIzaSyD-S-4B3hTceHcOdASZjuT-Ch9EIiDneEw
```

## 運用開始チェックリスト

- [ ] Twitter Developer Account作成完了
- [ ] 4つのTwitter認証情報を取得
- [ ] GitHub Secretsに5つの値を登録
- [ ] Google Sheetsに1週間分のデータ入力
- [ ] ローカルテストでSheets取得成功
- [ ] GitHub Actions手動実行で投稿成功
- [ ] 毎日17:00の自動投稿を確認

## 次のステップ

### 機能追加案
1. **投稿済みフラグの自動更新**
   - Google Sheets APIの書き込み権限追加
   
2. **画像付き投稿**
   - Twitter API v2への移行
   
3. **エラー通知**
   - 失敗時にメール通知

### Instagram対応
- Instagram Graph API（要Facebook Business）
- または手動投稿の継続