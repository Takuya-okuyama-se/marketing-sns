# Make.com シナリオ作成 完全ガイド（画像説明付き）

## 🎯 完成イメージ
```
⏰ Schedule → 🔍 Notion検索 → 🔀 フィルター → 🐦 Twitter投稿 → ✅ Notion更新
```

## STEP 1: Make.comにログイン

1. [make.com](https://www.make.com) にアクセス
2. 「Get started free」でアカウント作成
3. ダッシュボードで「Create a new scenario」をクリック

## STEP 2: Scheduleモジュール追加（トリガー）

### 2-1. モジュール追加
1. **画面中央の「+」をクリック**
2. **検索バーに「Schedule」と入力**
3. **時計アイコンの「Schedule」を選択**

### 2-2. Schedule設定
```
Run scenario: At regular intervals
Interval: 1 Day
Time: 17:00
Timezone: Asia/Tokyo
Start: 今日の日付
```

**設定画面の例：**
```
┌─────────────────────────┐
│ Schedule                │
├─────────────────────────┤
│ Interval: Every 1 days  │
│ Time: 17:00            │
│ Timezone: Asia/Tokyo    │
└─────────────────────────┘
```

## STEP 3: Notion検索モジュール追加

### 3-1. モジュール追加
1. **Scheduleモジュールの右側の「+」をクリック**
2. **「Notion」を検索して選択**
3. **「Search Objects」を選択**

### 3-2. Notion接続設定（初回のみ）
1. **「Add」ボタンをクリック**
2. **Connection name: 「SNS投稿管理」**
3. **Internal Integration Token: `secret_xxxxx`を貼り付け**
   - NotionのIntegration画面からコピー
4. **「Save」をクリック**

### 3-3. Search Objects詳細設定
```
Connection: SNS投稿管理（作成した接続）
Search in: Database
Database ID: 20cf6cb9-b225-80a4-a60e-ec49b48c60b1

Filter設定:
Property: 投稿日
Condition: On or after
Date: {{formatDate(now; "YYYY-MM-DD")}}

AND

Property: 投稿日  
Condition: On or before
Date: {{formatDate(now; "YYYY-MM-DD")}}

Sort設定:
Property: 投稿日
Direction: Ascending

Limit: 10
```

**フィルター設定の詳細：**
1. **「Add filter」をクリック**
2. **Property dropdown → 「投稿日」選択**
3. **Condition → 「equals」選択**
4. **Value欄に以下を入力：**
   ```
   {{formatDate(now; "YYYY-MM-DD")}}
   ```

## STEP 4: フィルターモジュール追加

### 4-1. フィルター追加
1. **Notionモジュールの右側の「+」**
2. **「Flow control」カテゴリ**
3. **「Filter」を選択（漏斗アイコン）**

### 4-2. フィルター条件設定
```
Label: 予約済みのみ
Condition: ステータス（Notionから取得） = 予約済み
```

**設定方法：**
1. **左側のフィールド：**
   - Notionモジュールをクリック
   - 「ステータス」を選択
2. **中央：「Equal to」を選択**
3. **右側：「予約済み」と入力**

## STEP 5: Twitter投稿モジュール追加

### 5-1. モジュール追加
1. **フィルターの右側の「+」**
2. **「Twitter」を検索**
3. **「Create a Tweet」を選択**

### 5-2. Twitter接続（初回のみ）
1. **「Add」ボタン**
2. **既存のTwitter認証情報を入力：**
   ```
   API Key: （GitHub Secretsに保存済み）
   API Secret: （GitHub Secretsに保存済み）
   Access Token: （GitHub Secretsに保存済み）
   Access Token Secret: （GitHub Secretsに保存済み）
   ```

### 5-3. Tweet内容設定
```
Status: {{3.Twitter}}
```
- 「3」はNotionモジュールの番号（自動的に表示される）
- 「Twitter」はNotionのプロパティ名

**動的データの選択方法：**
1. **Status欄をクリック**
2. **右側に表示されるNotionデータから「Twitter」を選択**
3. **自動的に `{{3.Twitter}}` が入力される**

## STEP 6: Notion更新モジュール追加

### 6-1. モジュール追加
1. **Twitterモジュールの右側の「+」**
2. **「Notion」を選択**
3. **「Update a Database Item」を選択**

### 6-2. 更新設定
```
Connection: SNS投稿管理（既存）
Database ID: 20cf6cb9-b225-80a4-a60e-ec49b48c60b1
Database Item ID: {{3.id}}

更新するプロパティ:
ステータス: 投稿済み
投稿URL: https://twitter.com/user/status/{{5.id_str}}
```

**設定詳細：**
1. **Database Item ID：**
   - Notionモジュールから「id」を選択
2. **Map をクリックして更新項目を追加**
3. **ステータス → 「投稿済み」に変更**
4. **投稿URL → TwitterのURLを設定**

## STEP 7: エラーハンドリング（オプション）

### Error Handler追加
各モジュールの右クリックメニューから：
```
Add error handler → Resume
```

これにより、1つの投稿でエラーが出ても次の投稿を処理します。

## 🧪 テスト実行

### 7-1. テストデータ準備
Notionで：
1. 投稿日を今日の日付に設定
2. ステータスを「予約済み」に
3. Twitter欄にテスト文章

### 7-2. Makeでテスト
1. **右下の「Run once」をクリック**
2. **各モジュールに緑のチェック✓が表示されれば成功**
3. **数字バブルで処理されたデータ数を確認**

### 7-3. 確認ポイント
- Notion: データが取得できているか
- Filter: 予約済みのみ通過しているか
- Twitter: 投稿されたか
- Notion更新: ステータスが変わったか

## 📊 実行結果の見方

各モジュールをクリックすると：
```
Input（入力データ）:
- 前のモジュールから受け取ったデータ

Output（出力データ）:
- 次のモジュールに渡すデータ

実行時間やエラー情報も表示
```

## ⚙️ スケジュール有効化

### テスト成功後：
1. **シナリオ画面左下のトグル**
2. **OFF → ON に切り替え**
3. **「Scheduling is ACTIVE」と表示**

## 🔧 よくあるエラーと対処法

### 1. Notion接続エラー
```
Error: Invalid token
```
**対処**: Integration tokenを再確認、データベースに接続許可

### 2. データが見つからない
```
The operation completed successfully, but no data was returned
```
**対処**: 
- 日付形式を確認（YYYY-MM-DD）
- ステータスが「予約済み」か確認

### 3. Twitter投稿エラー
```
Error: Duplicate status
```
**対処**: 同じ内容は連続投稿不可。テキストを少し変更

## 💡 応用設定

### 複数投稿対応
NotionとFilterの間に「Iterator」追加：
```
Iterator設定:
Array: {{3.array}}
```
これで複数の投稿を順番に処理

### 投稿間隔設定
各Twitter投稿の前に「Sleep」モジュール：
```
Delay: 30 seconds
```

### 条件分岐
「Router」で曜日別に処理を分岐：
```
Route 1: 月曜日 → 特別な処理
Route 2: その他 → 通常処理
```

## ✅ 完成チェックリスト

- [ ] Scheduleが17:00 Asia/Tokyoに設定
- [ ] Notionで今日のデータを正しく取得
- [ ] ステータスでフィルタリング成功
- [ ] Twitter投稿成功
- [ ] Notionのステータス更新成功
- [ ] シナリオをONに設定

これで完全自動化の完成です！🎉