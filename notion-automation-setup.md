# Notion + Make で作る最強のSNS自動投稿システム

## 🎯 完成イメージ
- Notionでカレンダー表示・ギャラリー表示切り替え
- 画像をドラッグ&ドロップするだけ
- AIが投稿文を自動生成
- 指定時刻に自動投稿

## 📋 必要なもの（すべて無料で開始）
1. Notionアカウント
2. Make（旧Integromat）アカウント
3. 既存のTwitter開発者アカウント

## Step 1: Notionデータベース作成（15分）

### 1. Notionにログイン
https://www.notion.so/

### 2. 新規ページ作成
```
/ → Database → Table を選択
タイトル: 「SNS投稿カレンダー」
```

### 3. プロパティ（列）設定

| プロパティ名 | タイプ | 説明 |
|------------|--------|------|
| タイトル | Title | 投稿の概要 |
| 投稿日 | Date | 投稿予定日時 |
| カテゴリー | Select | 勉強法/合格体験/入試情報など |
| Twitter | Text | Twitter投稿文（280文字） |
| Instagram | Text | Instagram投稿文 |
| 画像 | Files & media | ドラッグ&ドロップで追加 |
| ステータス | Select | 下書き/予約済み/投稿済み |
| 投稿URL | URL | 投稿後のリンク |
| AI生成 | Checkbox | AI文章生成するか |

### 4. ビューの追加

#### カレンダービュー
1. 「+ Add a view」クリック
2. Calendar選択
3. Date propertyに「投稿日」を設定

#### ギャラリービュー
1. 「+ Add a view」クリック
2. Gallery選択
3. Card previewに「画像」を設定

#### 今週の投稿ビュー
1. Table view追加
2. Filter: 投稿日 is This week
3. Sort: 投稿日 Ascending

### 5. テンプレート作成

#### 曜日別テンプレート
```
New → Template → 「月曜テンプレート」

デフォルト値：
- カテゴリー: 勉強法
- Twitter: 【効率的な学習法】
- ステータス: 下書き
```

## Step 2: Make（Integromat）設定（20分）

### 1. Makeアカウント作成
https://www.make.com/

### 2. 新規シナリオ作成

#### シナリオ1: 定時チェック&投稿
```
トリガー: Schedule（毎日17:00）
↓
Notion: データベース検索
（フィルター: 投稿日 = 今日 AND ステータス = 予約済み）
↓
Router（分岐）
├→ Twitter: ツイート作成
└→ Instagram: Graph API（※要Business Account）
↓
Notion: レコード更新（ステータス→投稿済み）
```

### 3. Notion連携設定

1. Makeで「Notion」モジュール追加
2. 「Create a connection」
3. Notion Integration作成：
   ```
   Notion → Settings → Integrations → New integration
   名前: Make連携
   Capabilities: すべてチェック
   ```
4. Integration Tokenをコピー
5. Makeに貼り付け

### 4. Twitter連携設定
既存のTwitter認証情報を使用：
- API Key
- API Secret
- Access Token
- Access Token Secret

## Step 3: AI文章生成機能（10分）

### NotionのAI機能活用
1. 空欄で「スペース」キー
2. 「Ask AI」選択
3. プロンプト例：
```
高校受験塾のTwitter投稿を作成してください。
テーマ：[カテゴリー]
文字数：280文字以内
ハッシュタグ：#高校受験 #少人数制塾
```

### Make + OpenAI連携（オプション）
```
Notion: 新規レコード監視
↓
OpenAI: GPT-3.5で文章生成
プロンプト: カテゴリーに応じた投稿文
↓
Notion: レコード更新
```

## Step 4: 画像管理の効率化

### Notionでの画像管理
1. **ドラッグ&ドロップ**
   - 画像ファイルを直接データベースにドロップ
   - 自動的にNotion内に保存

2. **Unsplash連携**
   - /image → Unsplashで無料画像検索
   - ワンクリックで挿入

3. **画像URL埋め込み**
   - /embed → 画像URLペースト
   - Google Drive画像も対応

### 画像の一括アップロード
```
1. ギャラリービューを開く
2. 複数画像を選択
3. まとめてドラッグ&ドロップ
4. 各カードに自動割り当て
```

## Step 5: 運用フロー

### 月初の作業（1時間）
```
1. Canvaで画像30枚作成
   ↓
2. Notionギャラリービューにドラッグ&ドロップ
   ↓
3. 各投稿の日付設定（カレンダーでドラッグ）
   ↓
4. AIで投稿文生成（スペースキー → Ask AI）
   ↓
5. ステータスを「予約済み」に一括変更
```

### 日々の運用（0分）
- Make が毎日17:00に自動チェック
- 該当投稿を自動配信
- ステータス自動更新

### 週次レビュー（15分）
```
Notionダッシュボード確認
├─ 今週の投稿状況
├─ 来週の予定
└─ パフォーマンス分析
```

## 📊 Notionダッシュボード作成

### ウィジェット追加
```
/embed

投稿カレンダー
├─ 月間投稿数: Count(ステータス=投稿済み)
├─ 予約済み: Count(ステータス=予約済み)
├─ 下書き: Count(ステータス=下書き)
└─ 今月の進捗: Progress Bar
```

### グラフ表示
```
/chart

カテゴリー別投稿数
曜日別パフォーマンス
月間推移
```

## 🚀 さらなる自動化

### 1. 投稿パフォーマンス自動取得
```
Make シナリオ追加：
Twitter API → いいね・RT数取得
↓
Notion データベース更新
```

### 2. 最適投稿時間の自動調整
```
パフォーマンスデータ分析
↓
高エンゲージメント時間帯を特定
↓
翌月の投稿時間を自動調整
```

### 3. コンテンツ自動生成
```
トレンドキーワード取得
↓
ChatGPT API で投稿案生成
↓
Notion に下書きとして保存
```

## 💰 コスト

### 完全無料で運用可能
- Notion: 無料プラン（個人利用）
- Make: 無料プラン（月1,000オペレーション）
- 1日1投稿なら月30オペレーションで十分

### 有料プランのメリット
- Notion Pro（$8/月）: 無制限ファイルアップロード
- Make Pro（$9/月）: 無制限オペレーション

## 🎓 学習リソース

### Notion
- [Notion公式ガイド](https://www.notion.so/help)
- [Notion API ドキュメント](https://developers.notion.com/)

### Make
- [Make Academy](https://academy.make.com/)
- [シナリオテンプレート](https://www.make.com/en/templates)

## トラブルシューティング

### よくある問題
1. **Makeが動作しない**
   - Notion Integrationの権限確認
   - データベースへのアクセス許可

2. **画像が表示されない**
   - Notion内アップロードを推奨
   - 外部URLは/embedを使用

3. **文字数オーバー**
   - NotionのFormula機能でカウント
   - Makeでバリデーション追加

これで月間作業時間を10時間→1時間に短縮できます！