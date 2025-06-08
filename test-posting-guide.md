# テスト投稿ガイド（2025年6月8日）

## 🧪 今すぐテスト投稿する方法

### 方法1: GitHub Actions手動実行（推奨）

#### STEP 1: Google Sheetsにテストデータ準備
1. **Sheetsを開く**
   - https://docs.google.com/spreadsheets/d/1YKHCDU7NswNo5p3UHy6Q5jdTtChoCAXo4B_KTmGjlsI

2. **今日のデータを追加**
   ```
   日付: 2025/6/8
   カテゴリー: 塾の特徴
   Twitter投稿文: 【テスト投稿】少人数制学習塾の特徴をお伝えします。このツイートは自動投稿のテストです。 #test #自動投稿テスト
   投稿済み: FALSE
   ```

#### STEP 2: GitHub Actionsで実行
1. **GitHubリポジトリを開く**
   - https://github.com/Takuya-okuyama-se/marketing-sns

2. **Actionsタブをクリック**

3. **「SNS Auto Post」をクリック**

4. **「Run workflow」ボタンをクリック**
   - Branch: main
   - 「Run workflow」をクリック

5. **実行状況を確認**
   - 緑のチェック✅が表示されれば成功

### 方法2: ローカルでテスト実行

#### Windows (WSL)での実行
```bash
# 1. ディレクトリに移動
cd /mnt/c/Users/takuy/marketing

# 2. 環境変数を設定（実際の値に置き換え）
export TWITTER_API_KEY="your_api_key"
export TWITTER_API_SECRET="your_api_secret"
export TWITTER_ACCESS_TOKEN="your_access_token"
export TWITTER_ACCESS_TOKEN_SECRET="your_access_token_secret"
export GOOGLE_SHEETS_ID="1YKHCDU7NswNo5p3UHy6Q5jdTtChoCAXo4B_KTmGjlsI"
export GOOGLE_API_KEY="AIzaSyD-S-4B3hTceHcOdASZjuT-Ch9EIiDneEw"

# 3. Pythonパッケージインストール
pip install tweepy google-api-python-client google-auth

# 4. スクリプト実行
python3 scripts/auto_post.py
```

## 📝 テスト投稿の確認ポイント

### 1. 投稿前の確認
- [ ] Google Sheetsに今日（2025/6/8）のデータがある
- [ ] 投稿済みが「FALSE」になっている
- [ ] Twitter投稿文が入力されている

### 2. 実行中の確認
- [ ] GitHub Actionsが「In progress」表示
- [ ] エラーメッセージが出ていない

### 3. 投稿後の確認
- [ ] Twitterに投稿されている
- [ ] Google Sheetsの「投稿済み」が「TRUE」に変わった
- [ ] エラーログがない

## ⚠️ よくあるエラーと対処法

### エラー1: 「今日の投稿データが見つかりません」
**原因**: 日付形式が違う
**対処**: 
- Sheetsの日付を `2025/6/8` または `2025/06/08` に統一
- スクリプトで対応済みなので両方OK

### エラー2: 「Twitter API エラー: 403」
**原因**: API認証の問題
**対処**: 
- GitHub Secretsの設定を確認
- Twitter Developer Portalで権限確認

### エラー3: 「重複したツイート」
**原因**: 同じ内容は投稿できない
**対処**: 
- テキストを少し変更
- 時刻を追加: `#test_1700` など

## 🎯 本番運用開始

### テスト成功後の設定
1. **毎日のデータを準備**
   ```
   6/9（月） - 勉強法
   6/10（火）- 合格体験談
   6/11（水）- 重要ポイント
   ...
   ```

2. **自動実行の確認**
   - 毎日17:00に自動実行される
   - GitHub Actionsのscheduleは既に設定済み

3. **監視**
   - Actions → 実行履歴で確認
   - エラー時はメール通知（GitHubの設定）

## 💡 デバッグ用コマンド

### Sheetsデータ確認のみ
```bash
cd /mnt/c/Users/takuy/marketing
python3 scripts/test_sheets_only.py
```

### 実行ログの詳細確認
GitHub Actions の各ステップをクリックすると詳細ログが見れます

## ✅ チェックリスト

### テスト投稿前
- [ ] Google Sheetsに今日のデータ追加
- [ ] 投稿済み = FALSE
- [ ] テスト用のテキスト準備

### テスト実行
- [ ] GitHub Actions → Run workflow
- [ ] または ローカルで実行

### テスト後
- [ ] Twitter確認
- [ ] Sheets更新確認
- [ ] エラーがないか確認

これでテスト投稿完了です！