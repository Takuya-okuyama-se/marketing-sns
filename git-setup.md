# GitHubへのpush手順

## 1. Gitの初期設定（初回のみ）
```bash
# あなたの名前とメールアドレスを設定
git config --global user.name "あなたの名前"
git config --global user.email "あなたのメール@example.com"
```

## 2. GitHubでリポジトリ作成
1. [github.com](https://github.com)にログイン
2. 右上の「+」→「New repository」
3. Repository name: `marketing-sns`
4. **Public**を選択（GitHub Pages利用のため必須）
5. 「Create repository」をクリック

## 3. ローカルからpush
```bash
# リモートリポジトリを追加
git remote add origin https://github.com/[あなたのユーザー名]/marketing-sns.git

# 現在の状態を確認
git status

# コミット（すでにaddは完了しています）
git commit -m "Initial commit: 高校受験塾向けSNS自動投稿管理システム"

# GitHubにpush
git push -u origin main
```

## 4. 認証方法

### 方法1: Personal Access Token（推奨）
1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. 「Generate new token」をクリック
3. 期限とscopeを設定（repoにチェック）
4. トークンをコピー（一度しか表示されません）
5. pushの際のパスワードとして使用

### 方法2: GitHub CLI
```bash
# GitHub CLIをインストール後
gh auth login
```

## 5. 今後の更新方法
```bash
# 変更をステージング
git add .

# コミット
git commit -m "更新内容の説明"

# push
git push
```

## トラブルシューティング

### Permission deniedエラー
- Personal Access Tokenを使用
- またはSSHキーを設定

### main/masterブランチの問題
```bash
# 現在のブランチ確認
git branch

# mainブランチがない場合
git checkout -b main
```