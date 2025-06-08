# Notion + Make 自動投稿連携ガイド

## 🎯 現在の状況
Notionデータベースにデータが入りました！次は自動投稿の設定です。

## 📊 データベースの最終確認

### 必要な設定
- [x] データ入力完了
- [ ] カレンダービュー追加
- [ ] ステータスの色分け
- [ ] Make連携用のIntegration作成

## 🚀 Make（Integromat）連携設定

### STEP 1: Notion Integration作成（5分）

1. **Notionの設定画面へ**
   ```
   左サイドバー → Settings & members
   ```

2. **Integrations作成**
   ```
   Connections → Develop or manage integrations
   → + New integration
   ```

3. **設定内容**
   ```
   Name: SNS自動投稿
   Logo: （任意）
   Associated workspace: あなたのワークスペース
   Capabilities: すべてチェック✓
   ```

4. **Tokenをコピー**
   ```
   Internal Integration Token: secret_xxxxxxxxxxxx
   （後で使うので保存）
   ```

### STEP 2: データベースに接続許可

1. **データベースページを開く**
2. **右上の「...」メニュー**
3. **「Add connections」**
4. **作成した「SNS自動投稿」を選択**

### STEP 3: Make側の設定（10分）

#### アカウント作成
1. [make.com](https://www.make.com) にアクセス
2. 無料アカウント作成
3. 「Create a new scenario」

#### シナリオ作成
```
[Trigger] Schedule
毎日17:00に実行
    ↓
[Action] Notion - Search Objects
データベースから今日の投稿を検索
    ↓
[Filter] ステータス = "予約済み"
    ↓
[Action] Twitter - Create a Tweet
    ↓
[Action] Notion - Update a Database Item
ステータスを"投稿済み"に更新
```

### STEP 4: Notion検索設定

#### Search Objects設定
```
Connection: 新規作成（Integration Token貼り付け）
Database ID: あなたのデータベースID
Filter:
  - Property: 投稿日
  - Condition: equals
  - Value: {{formatDate(now; "YYYY-MM-DD")}}
  AND
  - Property: ステータス
  - Condition: equals  
  - Value: 予約済み
```

## 📝 データベースIDの取得方法

1. **NotionでデータベースのURLをコピー**
   ```
   https://www.notion.so/20cf6cb9b22580a4a60eec49b48c60b1?v=xxxxx
                          ↑ この部分がデータベースID
   ```

2. **ハイフンを追加**
   ```
   20cf6cb9-b225-80a4-a60e-ec49b48c60b1
   ```

## 🔧 テスト実行

### 手動テスト
1. Makeで「Run once」クリック
2. 今日の日付で「予約済み」のデータがあるか確認
3. 正常に取得できたらTwitter投稿テスト

### デバッグ
- データが見つからない → 日付形式を確認
- 権限エラー → Integration接続を確認
- Twitter投稿失敗 → API認証を確認

## 💡 便利な設定

### 複数投稿対応
```
Iterator追加
→ 複数の投稿を順番に処理
→ 各投稿に30秒の間隔を設定
```

### エラー通知
```
Error handler追加
→ メール通知
→ Notionにエラーログ記録
```

### 投稿時刻の分散
```
Schedule設定で複数時刻：
- 9:00 - 朝の投稿
- 12:00 - 昼の投稿  
- 17:00 - 夕方の投稿
- 21:00 - 夜の投稿
```

## ✅ 最終チェックリスト

### Notion側
- [ ] Integration作成完了
- [ ] データベースに接続許可
- [ ] 投稿日が正しい形式
- [ ] ステータスが「予約済み」

### Make側
- [ ] アカウント作成
- [ ] Notion連携設定
- [ ] Twitter連携設定
- [ ] テスト実行成功

### 運用開始
- [ ] 1週間分のデータ準備
- [ ] 毎日17:00の自動実行設定
- [ ] エラー通知設定

## 🎉 完成！

これで毎日自動的に：
1. Notionから今日の投稿を取得
2. Twitterに投稿
3. ステータスを「投稿済み」に更新

月間作業時間：10時間 → 1時間に短縮！