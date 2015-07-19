% rebase('base.tpl')
<form method="post" action="/menus/new">
    <div class="form-group">
        <label>名前</label>
        <input class="form-control" type="text" name="name">
    </div>
    <div class="form-group">
        <label>カロリー</label>
        <input class="form-control" type="text" name="kcal">
    </div>
    <div class="form-group">
        <label>画像URL</label>
        <input class="form-control" type="text" name="image">
    </div>
    <button class="btn btn-primary" type="submit">登録</button>
</form>
