# IFTTT（イフト）でSNS自動投稿を設定する方法【初心者向け】

## IFTTTとは？
「If This Then That」の略で、異なるサービスを連携させる無料ツールです。
プログラミング不要で、Google Sheets → Twitter/Instagramの自動投稿が可能！

## セットアップ手順（15分で完了）

### 1. IFTTTアカウント作成
1. [ifttt.com](https://ifttt.com)にアクセス
2. 「Get started」→ メールアドレスで登録
3. 無料プランを選択

### 2. Twitter自動投稿の設定

#### ステップ1: アプレット作成
1. 「Create」ボタンをクリック
2. 「If This」をクリック

#### ステップ2: トリガー設定（Google Sheets）
1. 「Google Sheets」を検索して選択
2. 「New row added to spreadsheet」を選択
3. Googleアカウントと連携
4. 以下を設定：
   - Spreadsheet URL: `https://docs.google.com/spreadsheets/d/1YKHCDU7NswNo5p3UHy6Q5jdTtChoCAXo4B_KTmGjlsI`
   - 「Create trigger」

#### ステップ3: アクション設定（Twitter）
1. 「Then That」をクリック
2. 「Twitter」を検索して選択
3. 「Post a tweet」を選択
4. Twitterアカウントと連携
5. Tweet textに以下を設定：
   ```
   {{ColumnC}}
   ```
   （C列のTwitter投稿文を使用）

#### ステップ4: 保存
1. 「Continue」→「Finish」
2. アプレット名を設定（例：塾SNS自動投稿）

### 3. 動作の仕組み

Google Sheetsの構成：
| A列（日付） | B列（カテゴリー） | C列（Twitter投稿文） | D列（Instagram投稿文） |
|-------------|-------------------|---------------------|----------------------|
| 2025/1/10 | 勉強法 | 【効率的な暗記法】... | 📚暗記のコツ📚... |

新しい行を追加すると、自動的にC列の内容がツイートされます！

### 4. 運用方法

#### 毎日の投稿を自動化
1. **事前準備**（月1回）
   - 1ヶ月分の投稿を作成
   - Google Sheetsに保存

2. **毎日の作業**（1分）
   - 朝、その日の投稿行をシートの最下部に追加
   - 自動的にツイートされる！

3. **時間指定投稿のコツ**
   - 17:00に投稿したい場合、16:55頃に行を追加
   - IFTTTは最大15分の遅延がある

### 5. Instagram連携（もう1つのアプレット）

#### 注意事項
- Instagramは**ビジネスアカウント**が必要
- 画像投稿は不可（テキストのみ）
- Facebook経由での投稿になる

#### 設定方法
1. InstagramをFacebookページと連携
2. IFTTTで新規アプレット作成
3. If: Google Sheets → Then: Facebook Pages
4. 「Create a link post」を選択
5. Message欄に`{{ColumnD}}`を設定

### 6. トラブルシューティング

#### 投稿されない場合
- IFTTTアプリで通知を確認
- Google Sheetsの共有設定を確認
- 連携アカウントの再認証

#### 文字化けする場合
- シートの文字コードをUTF-8に
- 絵文字は避ける

### 7. 便利な活用法

#### 曜日別自動投稿
Google Sheetsで関数を使用：
```
=IF(WEEKDAY(A2)=2,"月曜日は勉強法の日！","")
```

#### ハッシュタグ自動追加
C列に以下のような形式で入力：
```
=B2&" #高校受験 #少人数制塾 #"&TEXT(TODAY(),"mm月dd日")
```

## まとめ

### メリット
✅ 完全無料（2つまで）
✅ プログラミング不要
✅ 安定性が高い
✅ 15分で設定完了

### デメリット
❌ 画像投稿は不可
❌ 投稿時間の細かい指定不可
❌ 無料版は2つのアプレットまで

### おすすめ運用
1. Twitter：IFTTT自動投稿（テキスト）
2. Instagram：週1回手動でまとめて投稿（画像付き）
3. 管理：すべてGoogle Sheetsで一元化

これで毎日の投稿が劇的に楽になります！