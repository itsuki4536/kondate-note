# kondate-note
献立情報を管理するWebアプリケーション

# 実装内容
* [ ] 献立の一覧表示と追加(出来れば編集機能)
* [ ] 献立は名前とカロリーと画像URLを持つ

# 手順

1. [x] 献立テーブルを用意(SQLAlchemy)
2. [x] Bottleでトップページにkondate.tpl(中身はHelloって表示させるだけ)を表示
3. [x] トップページに献立の一覧(selectしたやつを全部表示)を渡してあげて表示
4. [ ] 献立の登録画面を作成
    * [x] `/menus/new` にGETリクエストを送ると、献立作成フォームを表示
    * [x] `/menus/new` にPOSTでデータを送ると献立を登録して、トップページにリダイレクト
    * [ ] 名前の文字化けを修正
    * [ ] トップページから`/menus/new`へのリンクを追加
5. [ ] 画像をimgタグで表示
6. [ ] デザインを綺麗に
