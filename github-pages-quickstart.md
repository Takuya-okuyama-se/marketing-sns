# GitHub Pages クイックスタートガイド

## GitHub Pagesとは
無料で静的ウェブサイトをホスティングできるGitHubのサービス

## 最短セットアップ手順（5分で完了）

### 1. GitHubアカウント作成
1. [github.com](https://github.com) にアクセス
2. "Sign up"をクリック
3. ユーザー名、メール、パスワードを入力

### 2. リポジトリ作成
1. GitHubにログイン後、右上の「+」→「New repository」
2. Repository name: `marketing-sns` （任意の名前）
3. **Public**を選択（無料版では必須）
4. 「Create repository」をクリック

### 3. ファイルアップロード
1. 「uploading an existing file」をクリック
2. 作成した以下のファイルをドラッグ&ドロップ：
   - index.html
   - system_architecture.md
   - setup_guide.md
3. 「Commit changes」をクリック

### 4. GitHub Pages有効化
1. リポジトリの「Settings」タブをクリック
2. 左メニューの「Pages」をクリック
3. Source: 「Deploy from a branch」を選択
4. Branch: 「main」を選択
5. Folder: 「/ (root)」を選択
6. 「Save」をクリック

### 5. サイト確認
- 数分後、`https://[あなたのユーザー名].github.io/marketing-sns/` でアクセス可能

## 無料版の制限事項

### できること ✅
- 静的サイト（HTML/CSS/JavaScript）のホスティング
- 独自ドメイン接続
- HTTPS対応（自動）
- 月間100GBの帯域幅
- 1GBのストレージ

### できないこと ❌
- プライベートリポジトリでの公開（有料版が必要）
- サーバーサイド処理（PHP、Python、データベース等）
- 100MBを超えるファイル
- 商用利用（広告収入を得る場合は要相談）
- 1時間に10回を超えるビルド

## よくあるトラブル

### サイトが表示されない
- **原因**: 反映に最大10分かかる
- **解決**: しばらく待つ

### 404エラー
- **原因**: ファイル名が違う、index.htmlがない
- **解決**: index.htmlを必ず作成

### 更新が反映されない
- **原因**: ブラウザキャッシュ
- **解決**: Ctrl+F5でリロード

## 次のステップ

1. **Google Sheetsと連携**
   ```javascript
   // Google Sheets APIを使用（別途設定必要）
   const SHEET_ID = 'あなたのシートID';
   const API_KEY = 'あなたのAPIキー';
   ```

2. **自動更新設定**
   - GitHub Actionsで定期実行
   - 無料枠: 月2,000分まで

3. **カスタムドメイン**
   - 独自ドメインを購入（年1,000円程度）
   - CNAMEファイルを追加

## 高校受験塾向けカスタマイズ

### 追加すべきページ
- about.html（塾の紹介）
- schedule.html（投稿スケジュール）
- templates.html（投稿テンプレート集）

### セキュリティ注意点
- 生徒の個人情報は載せない
- 写真は必ず許可を取る
- 連絡先はお問い合わせフォーム経由に

これで基本的なセットアップは完了です！