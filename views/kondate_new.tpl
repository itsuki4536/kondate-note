<!DOCTYPE html>
<html>
<head lang="ja">
    <meta charset="UTF-8">
    <title>献立ノート</title>
</head>
<body>
    <p>献立の追加</p>
    <form method="post" action="/menus/new">
        <input type="hidden" name="mcode" value="UTF-8">
        名前：　<input type="text" name="name">
        カロリー：　<input type="text" name="kcal">
        画像URL：　<input type="text" name="image">
        <button type="submit">登録</button>
    </form>
</body>
</html>
