% rebase('base.tpl')
<ul class="list-group">
    % for menu in menus:
    <li class="list-group-item">
        <a href="/menus/{{ menu['id'] }}">
            {{menu['id']}} {{menu['name']}} {{menu['kcal']}}
        </a>
        <img src="{{menu['image']}}">
    </li>
    % end
</ul>
