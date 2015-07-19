from bottle import route, post, run, template, request, redirect
import db

@route('/')
def kondate():
    menus = db.menus.select().execute().fetchall()
    return template('kondate', menus=menus)

@route('/menus/new')
def kondate_new():
    return template('kondate_new')

@post('/menus/new')
def kondate_create():
    name = request.forms.get('name')
    kcal = request.forms.get('kcal')
    image = request.forms.get('image')
    import pdb; pdb.set_trace()
    db.menus.insert().execute(name=name, kcal=kcal, image=image)
    return redirect('/')


run(host='localhost', port=8080, debug=True, reloader=True)
