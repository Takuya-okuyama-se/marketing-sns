# 今すぐできる効率化改善（30分で実装）

## 1. Google Apps Script（GAS）で画像URL自動取得

### セットアップ手順
1. Google Sheetsを開く
2. 拡張機能 → Apps Script
3. 以下のコードを貼り付け

```javascript
function setupImageSync() {
  // メニューに追加
  const ui = SpreadsheetApp.getUi();
  ui.createMenu('SNS投稿管理')
    .addItem('画像を同期', 'syncDriveImages')
    .addItem('今月の投稿を生成', 'generateMonthlyPosts')
    .addToUi();
}

function syncDriveImages() {
  // 画像フォルダのID（URLから取得）
  const FOLDER_ID = 'あなたのフォルダID';
  const folder = DriveApp.getFolderById(FOLDER_ID);
  const files = folder.getFiles();
  
  const sheet = SpreadsheetApp.getActiveSheet();
  let row = 2; // データ開始行
  
  while (files.hasNext()) {
    const file = files.next();
    const fileName = file.getName();
    
    // ファイル名から日付を取得（例: 0608_勉強法.jpg）
    const dateMatch = fileName.match(/(\d{2})(\d{2})/);
    if (dateMatch) {
      const month = parseInt(dateMatch[1]);
      const day = parseInt(dateMatch[2]);
      const date = `2025/${month}/${day}`;
      
      // 該当する行を検索
      const values = sheet.getRange('A:A').getValues();
      for (let i = 0; i < values.length; i++) {
        if (values[i][0] === date) {
          // 画像URLを自動設定
          sheet.getRange(i + 1, 5).setValue(file.getUrl());
          break;
        }
      }
    }
  }
  
  SpreadsheetApp.getUi().alert('画像の同期が完了しました！');
}

function generateMonthlyPosts() {
  const sheet = SpreadsheetApp.getActiveSheet();
  const year = 2025;
  const month = 6; // 今月
  
  // カテゴリーテンプレート
  const templates = {
    1: { category: '勉強法', text: '【効率的な学習法】\n' },
    2: { category: '合格体験談', text: '【合格者の声】\n' },
    3: { category: '重要ポイント', text: '【今週の重要ポイント】\n' },
    4: { category: '入試情報', text: '【入試情報】\n' },
    5: { category: 'モチベーション', text: '【今日の応援メッセージ】\n' },
    6: { category: '保護者向け', text: '【保護者の皆様へ】\n' },
    0: { category: '塾の特徴', text: '【少人数制の強み】\n' }
  };
  
  // 月の日数を取得
  const lastDay = new Date(year, month, 0).getDate();
  
  for (let day = 1; day <= lastDay; day++) {
    const date = new Date(year, month - 1, day);
    const dayOfWeek = date.getDay();
    const template = templates[dayOfWeek];
    
    const row = day + 1;
    sheet.getRange(row, 1).setValue(`${year}/${month}/${day}`);
    sheet.getRange(row, 2).setValue(template.category);
    sheet.getRange(row, 3).setValue(template.text + 'ここに内容を入力');
    sheet.getRange(row, 6).setValue('FALSE');
  }
  
  SpreadsheetApp.getUi().alert('今月の投稿テンプレートを生成しました！');
}

// 初回実行時
function onOpen() {
  setupImageSync();
}
```

## 2. ドラッグ&ドロップ対応（index-v2.html改良版）

### 追加するコード
```javascript
// 画像ドロップエリアの追加
const imageSection = document.querySelector('.image-section');

imageSection.addEventListener('dragover', (e) => {
    e.preventDefault();
    imageSection.style.backgroundColor = '#e3f2fd';
});

imageSection.addEventListener('dragleave', (e) => {
    imageSection.style.backgroundColor = '';
});

imageSection.addEventListener('drop', async (e) => {
    e.preventDefault();
    imageSection.style.backgroundColor = '';
    
    const files = e.dataTransfer.files;
    if (files.length > 0 && files[0].type.startsWith('image/')) {
        // 画像をBase64に変換して表示
        const reader = new FileReader();
        reader.onload = (event) => {
            document.getElementById('imagePreview').src = event.target.result;
            document.getElementById('imagePreview').style.display = 'block';
            
            // 一時的にローカルストレージに保存
            const dateStr = document.getElementById('postDate').value;
            const imageData = {
                name: files[0].name,
                data: event.target.result,
                type: files[0].type
            };
            localStorage.setItem(`image_${dateStr}`, JSON.stringify(imageData));
            
            alert('画像をアップロードしました。Google Driveにアップロード後、URLを設定してください。');
        };
        reader.readAsDataURL(files[0]);
    }
});
```

## 3. 一括操作機能

### CSVインポート機能
```javascript
function importCSV() {
    const input = document.createElement('input');
    input.type = 'file';
    input.accept = '.csv';
    
    input.onchange = async (e) => {
        const file = e.target.files[0];
        const text = await file.text();
        const rows = text.split('\n').map(row => row.split(','));
        
        // ヘッダー行をスキップ
        for (let i = 1; i < rows.length; i++) {
            const [date, category, twitter, instagram, imageUrl] = rows[i];
            if (date) {
                postsData[date.trim()] = {
                    date: date.trim(),
                    category: category.trim(),
                    twitter: twitter.trim().replace(/"/g, ''),
                    instagram: instagram.trim().replace(/"/g, ''),
                    imageUrl: imageUrl.trim(),
                    status: 'draft'
                };
            }
        }
        
        localStorage.setItem('postsData', JSON.stringify(postsData));
        generateCalendar();
        alert(`${rows.length - 1}件のデータをインポートしました！`);
    };
    
    input.click();
}
```

## 4. キーボードショートカット

```javascript
document.addEventListener('keydown', (e) => {
    // Ctrl + S: 保存
    if (e.ctrlKey && e.key === 's') {
        e.preventDefault();
        if (document.getElementById('postModal').style.display === 'block') {
            savePost();
        }
    }
    
    // Ctrl + N: 新規投稿
    if (e.ctrlKey && e.key === 'n') {
        e.preventDefault();
        const today = new Date();
        openEditModal(today.getDate());
    }
    
    // ESC: モーダルを閉じる
    if (e.key === 'Escape') {
        closeModal();
    }
});
```

## 5. テンプレート挿入ボタン

```javascript
const templates = {
    monday: '【効率的な暗記法】\n繰り返し学習が記憶定着の鍵！\n当塾では少人数制だからこそ、一人ひとりの暗記状況を把握。\n最適なタイミングで復習を促します。\n\n#高校受験 #少人数制学習塾',
    
    tuesday: '【合格体験記】\n「少人数制だから質問しやすかった」\n昨年度合格したA君の言葉です。\n分からないことをすぐに聞ける環境が、合格への近道でした。\n\n#合格実績 #高校受験塾',
    
    // 他の曜日も追加
};

function insertTemplate() {
    const dayOfWeek = currentEditingDate.getDay();
    const dayNames = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'];
    const template = templates[dayNames[dayOfWeek]];
    
    if (template) {
        document.getElementById('twitterText').value = template;
        updateCharCount('twitter');
    }
}
```

これらの改善により、作業時間を大幅に短縮できます！

どの機能から実装したいですか？