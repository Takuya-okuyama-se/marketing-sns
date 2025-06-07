# SNS画像投稿ガイド

## 現在の状況
- **Twitter**: テキストのみ自動投稿可能（現在の設定）
- **Instagram**: APIでの自動投稿は制限が多い

## 画像投稿の3つの方法

### 方法1: 画像URLを含むツイート【最も簡単】
Google Sheetsに画像URLを含めて投稿

#### 設定方法
1. 画像を事前にアップロード
   - Imgur（無料）
   - Google Drive（共有リンク）
   - GitHub（リポジトリに保存）

2. SheetsのTwitter投稿文に含める
```
【効率的な暗記法】
繰り返し学習が記憶定着の鍵！
詳しくはこちら👇
https://i.imgur.com/example.jpg
#高校受験 #勉強法
```

### 方法2: GitHub Actionsで画像投稿【要実装】

#### 必要な変更
`scripts/auto_post.py`を更新：

```python
def post_to_twitter_with_image(text, image_path):
    """画像付きツイート"""
    try:
        # 画像をアップロード
        media = api.media_upload(image_path)
        
        # メディアIDを指定してツイート
        tweet = api.update_status(
            status=text,
            media_ids=[media.media_id]
        )
        print(f"画像付き投稿成功: {tweet.id}")
        return True
    except Exception as e:
        print(f"エラー: {e}")
        return False
```

#### 画像の保存場所
```
marketing-sns/
├── images/
│   ├── 2025-06-08.jpg
│   ├── 2025-06-09.jpg
│   └── templates/
│       ├── monday.jpg
│       └── tuesday.jpg
```

### 方法3: 半自動化【推奨】

#### Buffer/Later連携
1. **画像は月初にまとめて作成**
   - Canvaで30枚作成（2時間）
   - テンプレート化で効率化

2. **投稿予約ツール使用**
   - Buffer（無料：月10投稿）
   - Later（無料：月30投稿）
   - Hootsuite（無料：月30投稿）

3. **運用フロー**
   - テキスト：GitHub Actions自動投稿
   - 画像：週1回手動で予約投稿

## Canvaでの画像作成効率化

### テンプレート作成
1. 曜日別テンプレート（7種類）
2. カテゴリー別デザイン
3. ブランドカラー統一

### 月次作成リスト
- 第1週：新月の目標・計画（4枚）
- 第2週：勉強法・テクニック（8枚）
- 第3週：応援・モチベーション（8枚）
- 第4週：入試情報・お知らせ（8枚）
- 予備：季節イベント（2枚）

## 実装優先順位

### Phase 1（今すぐ可能）
- テキストのみ自動投稿 ✅
- 画像URLをツイートに含める

### Phase 2（追加実装）
- GitHubに画像保存
- auto_post.py改修
- 画像付き自動投稿

### Phase 3（Instagram対応）
- Facebook Business連携
- Instagram Graph API
- または手動運用継続

## 当面の運用案

### Twitter
- **平日**: テキスト自動投稿（GitHub Actions）
- **週末**: 画像付き手動投稿（まとめて予約）

### Instagram
- **週3回**: 画像付き投稿（Later使用）
- **ストーリーズ**: 日々の様子（手動）

### 画像管理
```
Google Drive/
└── 塾SNS画像/
    ├── 2025年6月/
    │   ├── 01_月曜_勉強法.png
    │   ├── 02_火曜_合格体験.png
    │   └── ...
    └── テンプレート/
        ├── 曜日別/
        └── イベント/
```

## まとめ

1. **今すぐ**: テキスト投稿を開始
2. **今週中**: Canvaでテンプレート作成
3. **来週**: 画像URL含む投稿テスト
4. **将来**: 完全自動化検討

これで画像なしでも効果的な運用が可能です！