# GitHub Secrets 設定方法（画像付きガイド）

## GitHub Secretsとは
APIキーやパスワードなどの機密情報を安全に保存する仕組みです。
コードには表示されず、GitHub Actionsでのみ使用できます。

## 設定手順（5分で完了）

### 1. リポジトリのSettingsを開く
1. https://github.com/Takuya-okuyama-se/marketing-sns にアクセス
2. 上部メニューの「**Settings**」タブをクリック
   - リポジトリ名の下にある横並びのタブの一番右

### 2. Secretsページへ移動
1. 左側のメニューをスクロール
2. 「**Security**」セクションの中の
3. 「**Secrets and variables**」をクリック
4. 展開されたメニューから「**Actions**」をクリック

### 3. 新しいSecretを追加

#### 最初のSecret（TWITTER_API_KEY）を追加
1. 緑色の「**New repository secret**」ボタンをクリック
2. 以下を入力：
   - **Name**: `TWITTER_API_KEY`（この通りに入力、大文字小文字も同じに）
   - **Secret**: あなたのTwitter APIキーを貼り付け
3. 「**Add secret**」ボタンをクリック

#### 2つ目以降も同様に追加
「New repository secret」をクリックして、以下を順番に追加：

### 4. 追加するSecrets一覧

| 順番 | Name欄に入力する文字 | Secret欄に入力する内容 |
|------|---------------------|------------------------|
| 1 | `TWITTER_API_KEY` | TwitterのAPIキー |
| 2 | `TWITTER_API_SECRET` | TwitterのAPIキーシークレット |
| 3 | `TWITTER_ACCESS_TOKEN` | Twitterのアクセストークン |
| 4 | `TWITTER_ACCESS_TOKEN_SECRET` | Twitterのアクセストークンシークレット |
| 5 | `GOOGLE_API_KEY` | `AIzaSyD-S-4B3hTceHcOdASZjuT-Ch9EIiDneEw` |

### 5. 入力時の注意点

#### ✅ 正しい入力例
- Name: `TWITTER_API_KEY`
- Secret: `1234567890abcdefghijklmn`

#### ❌ よくある間違い
- Name: `twitter_api_key`（小文字はNG）
- Name: `TWITTER API KEY`（スペースはNG）
- Secret: `"1234567890abcdefghijklmn"`（引用符は不要）
- Secret: 前後に空白が入っている（コピペ時に注意）

### 6. 確認方法

すべて追加すると、以下のように表示されます：

```
Repository secrets (5)
• GOOGLE_API_KEY        Updated now
• TWITTER_ACCESS_TOKEN        Updated now
• TWITTER_ACCESS_TOKEN_SECRET Updated now
• TWITTER_API_KEY            Updated now
• TWITTER_API_SECRET         Updated now
```

値は`***`で隠されて表示されます（セキュリティのため）。

### 7. よくある質問

#### Q: 間違えて入力した場合は？
A: Secret名をクリック → 「Update」ボタン → 新しい値を入力

#### Q: 値が見えないけど大丈夫？
A: 正常です。一度設定すると値は確認できません（セキュリティ機能）

#### Q: Twitterの認証情報がまだない
A: `twitter-developer-setup.md`を参照してTwitter開発者登録を完了してください

#### Q: Name欄の大文字小文字を間違えた
A: 削除して作り直してください（Settings → クリック → Delete）

### 8. 動作確認

設定完了後、以下で確認：

1. リポジトリの「**Actions**」タブ
2. 「**SNS Auto Post**」をクリック
3. 「**Run workflow**」→「**Run workflow**」
4. 実行ログで認証エラーが出ないか確認

### トラブルシューティング

#### 「Bad credentials」エラー
- Secret名のスペルミス
- 大文字小文字の間違い
- 値の前後に空白が入っている

#### 「Authentication failed」エラー
- Twitter認証情報が間違っている
- Twitter Appの権限設定を確認

## まとめ

1. Settings → Secrets and variables → Actions
2. 「New repository secret」で5つ追加
3. Name欄は**正確に**入力（大文字小文字も同じに）
4. Secret欄にキーを貼り付け（前後の空白に注意）
5. Actionsタブでテスト実行

これで自動投稿の準備完了です！