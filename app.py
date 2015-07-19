from bottle import route, post, run, template, request, redirect
from sqlalchemy.exc import IntegrityError
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
    name = request.forms.name
    kcal = request.forms.kcal
    image = request.forms.image
    try:
        kcal = int(kcal)
        db.menus.insert().execute(name=name, kcal=kcal, image=image)
    except ValueError:
        return '入力が不正です.'
    except IntegrityError:
        return 'データが重複しています'
    return redirect('/')


@route('/menus/<id>')
def kondate(id):
    return  db.menus.delete().where(db.menus.c.id == id).execute()
    return redirect('/')

run(host='localhost', port=8080, debug=True, reloader=True)
