<!DOCTYPE html>
<html>
<head lang="ja">
    <meta charset="UTF-8">
    <title>献立ノート</title>
</head>
<body>
    <p>献立一覧</p>

    <ul>
        % for menu in menus:
        <li>{{menu['id']}} {{menu['name']}} {{menu['kcal']}}</li>
        % end
    </ul>
</body>
</html>
