from bottle import route, run, template
import db

@route('/')
def kondate():
    menus = db.menus.select().execute().fetchall()
    return template('kondate', menus=menus)

@route('/menus/new')
def kondate_new():
    return template('kondate_new')


run(host='localhost', port=8080, debug=True, reloader=True)
