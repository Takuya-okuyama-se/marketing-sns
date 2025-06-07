# 高校受験塾 SNS自動投稿管理システム

Twitter・Instagram向けの365日自動投稿を管理するシステムです。

## 機能
- 投稿カレンダー表示
- カテゴリー別投稿提案
- 投稿テンプレート管理
- 画像作成ガイド

## セットアップ方法

### 1. GitHubにpush
```bash
# リモートリポジトリを追加
git remote add origin https://github.com/[あなたのユーザー名]/marketing-sns.git

# ファイルを追加してコミット
git add .
git commit -m "Initial commit: SNS自動投稿システム"

# GitHubにpush
git push -u origin main
```

### 2. GitHub Pages有効化
1. GitHubでリポジトリのSettingsを開く
2. Pages → Source → Deploy from a branch
3. Branch: main を選択して Save

### 3. アクセス
`https://[あなたのユーザー名].github.io/marketing-sns/`

## ファイル構成
- `index.html` - メインの管理画面
- `system_architecture.md` - システム設計書
- `setup_guide.md` - セットアップガイド
- `github-pages-quickstart.md` - GitHub Pages利用ガイド

## 投稿スケジュール
- 月曜: 勉強法・学習テクニック
- 火曜: 合格体験談・生徒の声
- 水曜: 今週の重要ポイント解説
- 木曜: 入試情報・傾向分析
- 金曜: モチベーション・応援メッセージ
- 土曜: 保護者向け情報
- 日曜: 塾の特徴・少人数制のメリット