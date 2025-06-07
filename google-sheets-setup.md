# Google Sheets API 連携設定ガイド

## 1. Google Cloud Console設定（無料）

### ステップ1: プロジェクト作成
1. [Google Cloud Console](https://console.cloud.google.com/)にアクセス
2. 「プロジェクトを作成」をクリック
3. プロジェクト名: `sns-marketing-juku`
4. 「作成」をクリック

### ステップ2: Google Sheets API有効化
1. 左メニュー「APIとサービス」→「ライブラリ」
2. 「Google Sheets API」を検索
3. 「有効にする」をクリック

### ステップ3: APIキー作成
1. 「APIとサービス」→「認証情報」
2. 「認証情報を作成」→「APIキー」
3. 作成されたAPIキーをコピー（後で使用）
4. 「キーを制限」をクリック

### ステップ4: APIキーの制限（重要）
1. アプリケーションの制限：「HTTPリファラー」
2. ウェブサイトの制限に追加：
   - `https://takuya-okuyama-se.github.io/*`
   - `http://localhost:*`（テスト用）
3. API制限：「Google Sheets API」のみを選択
4. 「保存」

## 2. Google Sheetsの準備

### ステップ1: スプレッドシート作成
1. [Google Sheets](https://sheets.google.com)で新規作成
2. シート名: `SNS投稿カレンダー`

### ステップ2: データ構造
| A列 | B列 | C列 | D列 | E列 | F列 |
|-----|-----|-----|-----|-----|-----|
| 日付 | カテゴリー | Twitter投稿文 | Instagram投稿文 | 画像説明 | 投稿済み |
| 2025/1/1 | 新年挨拶 | 新年あけましておめでとうございます... | 🎍新年のご挨拶🎍... | 新年の挨拶画像 | FALSE |

### ステップ3: 共有設定
1. 右上の「共有」ボタン
2. 「リンクを取得」
3. 「制限付き」→「リンクを知っている全員」に変更
4. 「閲覧者」権限でOK
5. URLからシートIDを取得：
   ```
   https://docs.google.com/spreadsheets/d/【ここがシートID】/edit
   ```

## 3. 実装コード

### index.htmlに追加するコード
```javascript
// Google Sheets API設定
const SHEET_ID = 'あなたのシートID'; // 上記で取得したID
const API_KEY = 'あなたのAPIキー'; // Google Cloudで作成したキー
const RANGE = 'シート1!A2:F366'; // 365日分のデータ範囲

// データ読み込み関数
async function loadSheetData() {
    try {
        const response = await fetch(
            `https://sheets.googleapis.com/v4/spreadsheets/${SHEET_ID}/values/${RANGE}?key=${API_KEY}`
        );
        
        if (!response.ok) {
            throw new Error('データ取得エラー');
        }
        
        const data = await response.json();
        const posts = data.values || [];
        
        // データを処理
        posts.forEach((row, index) => {
            const [date, category, twitter, instagram, image, posted] = row;
            console.log(`${date}: ${category}`);
            // カレンダーに反映する処理
        });
        
        alert('データを更新しました！');
        
    } catch (error) {
        console.error('エラー:', error);
        alert('データ取得に失敗しました。APIキーとシートIDを確認してください。');
    }
}

// 今日の投稿データを取得
async function getTodayPost() {
    const today = new Date();
    const formattedDate = `${today.getFullYear()}/${today.getMonth()+1}/${today.getDate()}`;
    
    try {
        const response = await fetch(
            `https://sheets.googleapis.com/v4/spreadsheets/${SHEET_ID}/values/${RANGE}?key=${API_KEY}`
        );
        
        const data = await response.json();
        const posts = data.values || [];
        
        const todayPost = posts.find(row => row[0] === formattedDate);
        
        if (todayPost) {
            return {
                date: todayPost[0],
                category: todayPost[1],
                twitter: todayPost[2],
                instagram: todayPost[3],
                image: todayPost[4],
                posted: todayPost[5] === 'TRUE'
            };
        }
        
        return null;
        
    } catch (error) {
        console.error('エラー:', error);
        return null;
    }
}
```

## 4. セキュリティ注意事項

### ⚠️ 重要な制限事項
1. **APIキーは公開される**
   - GitHub Pagesは静的サイトなので、APIキーが露出します
   - 必ず上記の「APIキーの制限」を設定してください

2. **読み取り専用にする**
   - Sheetsは「閲覧者」権限のみ
   - 書き込みは手動で行う

3. **代替案（より安全）**
   - Google Apps Script（GAS）を使用
   - 中間APIサーバーを構築（Vercel無料枠など）

## 5. Google Apps Script（無料・安全）

より安全な方法として、GASを使用：

### GASセットアップ
1. Sheetsで「拡張機能」→「Apps Script」
2. 以下のコードを貼り付け：

```javascript
function doGet(e) {
  const sheet = SpreadsheetApp.getActiveSheet();
  const data = sheet.getDataRange().getValues();
  
  // ヘッダーを除いたデータ
  const posts = data.slice(1).map(row => ({
    date: row[0],
    category: row[1],
    twitter: row[2],
    instagram: row[3],
    image: row[4],
    posted: row[5]
  }));
  
  // CORS対応
  return ContentService
    .createTextOutput(JSON.stringify(posts))
    .setMimeType(ContentService.MimeType.JSON);
}
```

3. 「デプロイ」→「新しいデプロイ」
4. 「ウェブアプリ」として公開
5. URLをコピー（これがAPIエンドポイント）

### index.htmlでの使用
```javascript
const GAS_URL = 'あなたのGAS URL';

async function loadSheetData() {
    const response = await fetch(GAS_URL);
    const posts = await response.json();
    // データ処理
}
```

この方法ならAPIキーが不要で安全です！