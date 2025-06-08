# Make.com 簡単5ステップ設定

## 🚀 5分で完成する最短手順

### 準備するもの
1. **Notion Integration Token**: `secret_xxxxx`
2. **データベースID**: `20cf6cb9b22580a4a60eec49b48c60b1`
3. **Twitter API情報**: 4つのキー

## STEP 1️⃣: シナリオ作成
```
Make.com → Scenarios → + Create a new scenario
```

## STEP 2️⃣: Schedule追加（毎日17:00）
```
中央の [+] → Schedule → 設定:
- Interval: 1 Days
- Time: 17:00
- Timezone: Asia/Tokyo
```

## STEP 3️⃣: Notion検索追加
```
Scheduleの右 [+] → Notion → Search Database Items

接続設定:
- Token貼り付け
- Database選択 or ID入力

フィルター:
- 投稿日 = {{formatDate(now; "YYYY-MM-DD")}}
- ステータス = 予約済み
```

## STEP 4️⃣: Twitter投稿追加
```
Notionの右 [+] → Twitter → Create a Tweet

Text欄:
- 右パネルからNotionデータ選択
- 「Twitter」フィールドをクリック
```

## STEP 5️⃣: Notion更新追加
```
Twitterの右 [+] → Notion → Update Database Item

設定:
- Item ID: Notionのidを選択
- ステータス: 投稿済み
```

## ✅ 完了！
```
Run once でテスト → 左下トグルON
```

---

## 🆘 うまくいかない時

### データベースが見つからない
→ ID直接入力: `20cf6cb9b22580a4a60eec49b48c60b1`

### 日付フィルターが効かない
→ テスト用に手動で日付条件を外してみる

### Twitterエラー
→ 同じ文章は投稿できないので、テキストを変更

## 📱 動作確認
1. Notionで今日の日付・予約済みのデータ作成
2. Make.comで「Run once」
3. 各モジュールに ✅ が表示されれば成功！