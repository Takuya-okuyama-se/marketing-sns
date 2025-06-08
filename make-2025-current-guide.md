# Make.com 2025年6月現在 最新設定ガイド

## 📅 現在：2025年6月8日

## 🎯 Make.com 最新インターフェース対応

### STEP 1: 新規シナリオ作成

1. **Make.comにログイン**
2. **左メニュー「Scenarios」**
3. **右上「+ Create a new scenario」ボタン**

## STEP 2: Scheduleトリガー設定

### 2-1. モジュール追加
1. **画面中央の大きな「+」をクリック**
2. **検索バーに「Schedule」と入力**
3. **時計アイコンの「Schedule」を選択**

### 2-2. 設定内容
```
Trigger settings:
├─ Run scenario: At regular intervals
├─ Interval: Every 1 days
├─ Time: 17:00
├─ Days of the week: All days
└─ Timezone: Asia/Tokyo
```

**「OK」をクリックして保存**

## STEP 3: Notion検索設定

### 3-1. Notionモジュール追加
1. **Scheduleモジュールの右側に出る「+」をクリック**
2. **「Notion」で検索**
3. **Notionロゴをクリック**
4. **「Search Database Items」を選択**

### 3-2. 接続設定（初回のみ）
1. **Connection欄の「Add」をクリック**
2. **Connection name**: `Notion SNS投稿`
3. **Internal Integration Token**: 
   ```
   secret_で始まるトークンを貼り付け
   ```
4. **「Save」ボタン**

### 3-3. データベース検索設定
```
Database ID: 20cf6cb9b22580a4a60eec49b48c60b1
（手動で入力、またはドロップダウンから選択）

Filter設定:
1. Add filterをクリック
2. Property: 投稿日
3. Condition: equals  
4. Value: {{formatDate(now; "YYYY-MM-DD")}}

AND条件追加:
1. + Add conditionをクリック
2. Property: ステータス
3. Condition: equals
4. Value: 予約済み
```

## STEP 4: Twitter投稿設定

### 4-1. Twitterモジュール追加
1. **Notionモジュールの右「+」**
2. **「X (Twitter)」で検索**（2025年は「X」表記の可能性）
3. **「Create a Tweet」または「Create a Post」を選択**

### 4-2. 認証設定
```
Connection Type: OAuth 1.0a
Consumer Key: [あなたのAPI Key]
Consumer Secret: [あなたのAPI Secret]
Access Token: [あなたのAccess Token]
Access Token Secret: [あなたのAccess Token Secret]
```

### 4-3. 投稿内容設定
1. **Text欄をクリック**
2. **右側のパネルが開く**
3. **「1. Notion」セクションを展開**
4. **「Twitter」フィールドを選択**
   - 自動的に `{{1.Twitter}}` が入力される

## STEP 5: Notion更新設定

### 5-1. 更新モジュール追加
1. **Twitterの右「+」**
2. **「Notion」選択**
3. **「Update a Database Item」選択**

### 5-2. 更新内容
```
Connection: Notion SNS投稿（既存）
Database ID: 20cf6cb9b22580a4a60eec49b48c60b1
Database Item ID: {{1.id}}

Properties to update:
├─ ステータス: 投稿済み
└─ 投稿URL: https://x.com/status/{{2.id}}
```

## 🧪 2025年6月8日のテスト

### テストデータ準備（Notion）
```
タイトル: 日曜講座案内
投稿日: 2025-06-08
カテゴリー: 塾の特徴
ステータス: 予約済み ← 重要！
Twitter: 【テスト投稿】少人数制学習塾の特徴をお伝えします。#test
```

### テスト実行
1. **画面下部「Run once」クリック**
2. **実行フロー確認**：
   - Schedule → ✅
   - Notion (1) → ✅（1件取得）
   - Twitter → ✅
   - Notion Update → ✅

### 本番設定
1. **左下のスイッチをON**
2. **「Scenario is ON」表示確認**
3. **毎日17:00に自動実行開始**

## ⚠️ 2025年6月特有の注意点

### 日付形式
- Notion: `2025-06-08` または `2025/6/8`
- Make.com: `YYYY-MM-DD` 形式推奨

### API変更点
- Twitter → X (Twitter) に名称変更の可能性
- レート制限の確認

### タイムゾーン
- 必ず `Asia/Tokyo` を選択
- サマータイムはないので安心

## 📊 運用スケジュール（2025年6月）

```
6/8（日）  - 今日 - テスト投稿
6/9（月）  - 勉強法
6/10（火） - 合格体験談
6/11（水） - 重要ポイント
6/12（木） - 入試情報
6/13（金） - モチベーション
6/14（土） - 保護者向け
6/15（日） - 塾の特徴
```

## ✅ 最終確認

- [ ] Notionの日付が2025年6月になっている
- [ ] ステータスが「予約済み」
- [ ] Make.comでテスト成功
- [ ] スケジュールON
- [ ] 17:00に自動投稿される

これで2025年6月の自動投稿システムが稼働します！