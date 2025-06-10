// Google Apps Script - Drive Upload Service
// このコードをGoogle Apps Scriptにコピーして、Webアプリとしてデプロイしてください

function doPost(e) {
  try {
    // POSTデータを解析
    const data = JSON.parse(e.postData.contents);
    const fileName = data.fileName;
    const fileData = data.fileData;
    const mimeType = data.mimeType || 'video/webm';
    
    // Base64デコード
    const blob = Utilities.newBlob(Utilities.base64Decode(fileData), mimeType, fileName);
    
    // Google Driveの特定のフォルダに保存（フォルダIDを設定してください）
    const folderId = '1yrLqAXQuO83R2weHHffr-LAnFvMs2A8o'; // ここにGoogle DriveのフォルダIDを入力
    let folder;
    
    if (folderId) {
      folder = DriveApp.getFolderById(folderId);
    } else {
      // フォルダIDが設定されていない場合はルートに保存
      folder = DriveApp.getRootFolder();
    }
    
    // ファイルを作成
    const file = folder.createFile(blob);
    
    // 共有設定（リンクを知っている人は閲覧可能）
    file.setSharing(DriveApp.Access.ANYONE_WITH_LINK, DriveApp.Permission.VIEW);
    
    // ダウンロード用URLを生成
    const fileId = file.getId();
    const downloadUrl = `https://drive.google.com/file/d/${fileId}/view?usp=sharing`;
    const directUrl = `https://drive.google.com/uc?export=download&id=${fileId}`;
    
    // レスポンスを返す
    return ContentService
      .createTextOutput(JSON.stringify({
        success: true,
        fileId: fileId,
        fileName: fileName,
        fileUrl: downloadUrl,
        directUrl: directUrl,
        message: 'ファイルが正常にアップロードされました'
      }))
      .setMimeType(ContentService.MimeType.JSON);
      
  } catch (error) {
    // エラーレスポンス
    return ContentService
      .createTextOutput(JSON.stringify({
        success: false,
        error: error.toString(),
        message: 'アップロード中にエラーが発生しました'
      }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

// GET リクエスト（テスト用）
function doGet(e) {
  return ContentService
    .createTextOutput(JSON.stringify({
      message: 'Google Drive Upload Service is running',
      usage: 'Send POST request with {fileName, fileData, mimeType}'
    }))
    .setMimeType(ContentService.MimeType.JSON);
}

// 設定手順：
// 1. Google Apps Script (https://script.google.com) で新規プロジェクトを作成
// 2. このコードを貼り付け
// 3. YOUR_FOLDER_ID_HERE を実際のGoogle DriveフォルダIDに置き換え
// 4. デプロイ > 新しいデプロイ
// 5. 種類：ウェブアプリ
// 6. 実行ユーザー：自分
// 7. アクセスできるユーザー：全員
// 8. デプロイ
// 9. Web App URLをコピーして、index-v3.htmlのGAS_URLに設定