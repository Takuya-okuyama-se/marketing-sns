# Google Sheetsへの自動反映を実現する方法

## 現状の問題点
1. **読み取り専用API**: 現在使用しているGoogle Sheets APIは読み取り専用
2. **自動投稿の依存**: GitHub Actionsの自動投稿はSheetsのデータを参照するため、Sheetsにデータがないと投稿されない

## 解決方法

### 方法1: Google Apps Script（GAS）を使用（推奨）

#### 1. Google SheetsでApps Scriptを作成

1. Google Sheetsを開く
2. 「拡張機能」→「Apps Script」をクリック
3. 以下のコードを貼り付け：

```javascript
function doPost(e) {
  try {
    // POSTデータを解析
    const data = JSON.parse(e.postData.contents);
    
    // スプレッドシートを取得
    const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('シート1');
    
    // 日付でデータを検索
    const lastRow = sheet.getLastRow();
    let targetRow = -1;
    
    for (let i = 2; i <= lastRow; i++) {
      const cellDate = sheet.getRange(i, 1).getValue();
      if (cellDate == data.date) {
        targetRow = i;
        break;
      }
    }
    
    // データが見つからない場合は新規追加
    if (targetRow === -1) {
      targetRow = lastRow + 1;
    }
    
    // データを更新
    sheet.getRange(targetRow, 1).setValue(data.date);
    sheet.getRange(targetRow, 2).setValue(data.category || '');
    sheet.getRange(targetRow, 3).setValue(data.twitter || '');
    sheet.getRange(targetRow, 4).setValue(data.instagram || '');
    sheet.getRange(targetRow, 5).setValue(data.imageUrl || '');
    sheet.getRange(targetRow, 6).setValue(data.status === 'posted' ? 'TRUE' : 'FALSE');
    
    // 成功レスポンス
    return ContentService
      .createTextOutput(JSON.stringify({success: true}))
      .setMimeType(ContentService.MimeType.JSON);
      
  } catch(error) {
    // エラーレスポンス
    return ContentService
      .createTextOutput(JSON.stringify({success: false, error: error.toString()}))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

// CORS対応
function doOptions(e) {
  return ContentService
    .createTextOutput('')
    .setMimeType(ContentService.MimeType.TEXT);
}
```

4. 「デプロイ」→「新しいデプロイ」をクリック
5. 種類: 「ウェブアプリ」を選択
6. 実行ユーザー: 「自分」
7. アクセス権限: 「全員」
8. デプロイをクリックし、表示されるURLをコピー

### 方法2: Google Sheets API v4 with OAuth（より安全）

#### 必要な設定：
1. Google Cloud Consoleでプロジェクトを作成
2. Google Sheets APIを有効化
3. OAuth 2.0認証情報を作成
4. サービスアカウントを使用

## index-v2.htmlの更新コード

```javascript
// Google Apps ScriptのURL（デプロイ後に取得したURL）
const GAS_URL = 'YOUR_DEPLOYED_WEB_APP_URL';

// Sheetsに自動保存する関数
async function saveToSheets(postData) {
    try {
        const response = await fetch(GAS_URL, {
            method: 'POST',
            mode: 'no-cors', // CORSエラーを回避
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(postData)
        });
        
        console.log('Sheetsへの保存完了');
        return true;
    } catch (error) {
        console.error('Sheets保存エラー:', error);
        return false;
    }
}

// savePost関数を更新
function savePost() {
    const dateStr = formatDate(currentEditingDate);
    
    const postData = {
        date: dateStr,
        category: document.getElementById('postCategory').value,
        twitter: document.getElementById('twitterText').value,
        instagram: document.getElementById('instagramText').value,
        imageUrl: document.getElementById('imageUrl').value,
        status: document.getElementById('postStatus').value,
        lastModified: new Date().toISOString()
    };
    
    // ローカルに保存
    postsData[dateStr] = postData;
    localStorage.setItem('postsData', JSON.stringify(postsData));
    
    // Sheetsに自動保存
    saveToSheets(postData).then(success => {
        if (success) {
            showSaveStatus('success', 'ローカルとSheetsに保存されました');
        } else {
            showSaveStatus('warning', 'ローカルに保存されました（Sheets保存失敗）');
        }
    });
    
    closeModal();
    generateCalendar();
    updateTodayStatus();
}
```

## セットアップ手順

1. **Google Apps Scriptの設定**
   - 上記のGASコードをデプロイ
   - 取得したURLをindex-v2.htmlに設定

2. **index-v2.htmlの更新**
   - GAS_URLを設定
   - savePost関数を更新

3. **テスト**
   - データを入力して保存
   - Google Sheetsで自動反映を確認

## メリット

1. **完全自動化**: データ入力→Sheets反映→自動投稿がシームレスに
2. **リアルタイム同期**: 保存と同時にSheetsも更新
3. **エラー処理**: Sheets保存に失敗してもローカルデータは保持

## 注意点

1. **GASの実行制限**: 1日あたりの実行回数に制限あり
2. **CORS**: no-corsモードのため、レスポンスは取得できない
3. **セキュリティ**: 公開URLなので、必要に応じて認証を追加

この方法で、完全に自動化されたシステムが実現できます！