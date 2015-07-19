% rebase('base.tpl')
<ul class="list-group">
    % for menu in menus:
    <li class="list-group-item">
        {{menu['id']}} {{menu['name']}} {{menu['kcal']}}
        <img src="{{menu['image']}}">
    </li>
    % end
</ul>


