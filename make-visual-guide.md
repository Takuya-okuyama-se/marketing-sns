# Make.com ビジュアル設定ガイド

## 🎨 シナリオの見た目

```
     [⏰]
  Schedule
  17:00 毎日
      ↓
     [📋]
   Notion
  今日の投稿
      ↓
     [🔽]
   Filter
  予約済み
      ↓
     [🐦]
   Twitter
    投稿
      ↓
     [✅]
   Notion
 ステータス更新
```

## 📍 各モジュールの詳細設定

### 1️⃣ Schedule（スケジュール）
```
┌─ Schedule ─────────────┐
│ ⏰ Every day at 17:00  │
│                        │
│ Timezone: Asia/Tokyo   │
└────────────────────────┘
```
**クリックして設定：**
- Interval: 1 Days
- Time: 17:00
- Timezone: Asia/Tokyo

### 2️⃣ Notion Search（検索）
```
┌─ Notion ───────────────┐
│ 🔍 Search Objects      │
│                        │
│ Database: SNS投稿      │
│ Filter: 投稿日 = 今日  │
└────────────────────────┘
```
**重要な設定：**
```
Database ID: 20cf6cb9-b225-80a4-a60e-ec49b48c60b1
Filter: 投稿日 equals {{formatDate(now; "YYYY-MM-DD")}}
```

### 3️⃣ Filter（フィルター）
```
┌─ Filter ───────────────┐
│ 🔽 Condition          │
│                        │
│ ステータス = 予約済み  │
└────────────────────────┘
```
**設定方法：**
1. 左側：`{{3.ステータス}}`（Notionから）
2. 中央：`Equal to`
3. 右側：`予約済み`

### 4️⃣ Twitter Post（投稿）
```
┌─ Twitter ──────────────┐
│ 🐦 Create a Tweet      │
│                        │
│ {{3.Twitter}}          │
└────────────────────────┘
```
**動的データの選択：**
- Status欄クリック → Notionアイコン → Twitter選択

### 5️⃣ Notion Update（更新）
```
┌─ Notion ───────────────┐
│ ✅ Update Item         │
│                        │
│ ステータス → 投稿済み  │
└────────────────────────┘
```
**更新内容：**
- Database Item ID: `{{3.id}}`
- ステータス: `投稿済み`
- 投稿URL: `https://twitter.com/status/{{5.id_str}}`

## 🎯 クリックする場所（順番）

### 画面上での操作順序：
```
1. 中央の [+] → Schedule選択
              ↓
2. Scheduleの右 [+] → Notion選択
              ↓
3. Notionの右 [+] → Flow control → Filter
              ↓
4. Filterの右 [+] → Twitter選択
              ↓
5. Twitterの右 [+] → Notion選択
```

## 💡 データの流れを確認

### テスト実行時の表示：
```
Schedule [1] → Notion [1] → Filter [1] → Twitter [1] → Notion [1]
```
数字は処理されたデータ数

### 成功時の表示：
- 各モジュール：緑のチェック ✅
- エラー時：赤い ❌

## 🔍 デバッグのコツ

### 各モジュールをクリックすると見える情報：
```
┌─ Input ────────────────┐
│ 受け取ったデータ       │
├─ Output ───────────────┤
│ 次に渡すデータ         │
└────────────────────────┘
```

### Notion検索結果の例：
```
Output:
- id: "abc123..."
- タイトル: "週末の勉強法"
- 投稿日: "2025-06-01"
- Twitter: "【週末の勉強法】..."
- ステータス: "予約済み"
```

## ⚡ ショートカット

### モジュール操作：
- **右クリック**: メニュー表示
- **Ctrl+C/V**: コピー＆ペースト
- **Delete**: モジュール削除
- **ドラッグ**: 位置変更

### 便利な機能：
- **Clone**: モジュールを複製
- **Disable**: 一時的に無効化
- **Notes**: メモを追加

## 🎊 完成形

最終的にこのような流れになります：
```
毎日17:00
    ↓
Notionから今日の「予約済み」投稿を取得
    ↓
Twitterに投稿
    ↓
Notionのステータスを「投稿済み」に更新
```

自動化完成！🚀