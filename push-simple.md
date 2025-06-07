# GitHubへの簡単push手順

## 1. Git初期設定
```bash
git config --global user.name "あなたの名前"
git config --global user.email "あなたのメール@example.com"
```

## 2. コミット実行
```bash
git commit -m "Initial commit: 高校受験塾向けSNS自動投稿管理システム"
```

## 3. GitHubでリポジトリ作成
1. [github.com/new](https://github.com/new) にアクセス
2. Repository name: `marketing-sns`
3. **Public**を選択
4. 「Create repository」をクリック

## 4. リポジトリ作成後の画面から
作成直後の画面に表示される以下のコマンドをコピーして実行：

```bash
git remote add origin https://github.com/[あなたのユーザー名]/marketing-sns.git
git branch -M main
git push -u origin main
```

## 5. 認証
pushを実行すると：
- **ブラウザが自動で開きます**
- GitHubにログインしていれば「Authorize」をクリック
- 完了！

トークン不要で、ブラウザ認証だけでOKです。

## 今後の更新
```bash
git add .
git commit -m "更新内容"
git push
```

これだけでGitHub Pagesも自動更新されます！