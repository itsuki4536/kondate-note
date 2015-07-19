% rebase('base.tpl')
<form method="post" action="/menus/new">
    <div class="form-group">
        <label for="name">名前</label>
        <input id="name" class="form-control" type="text" name="name" required>
    </div>
    <div class="form-group">
        <label for="kcal">カロリー</label>
        <input id="kcal" class="form-control" type="number" name="kcal" required>
    </div>
    <div class="form-group">
        <label for="image_url">画像URL</label>
        <input id="image_url" class="form-control" type="text" name="image">
    </div>
    <button class="btn btn-primary" type="submit">登録</button>
</form>
