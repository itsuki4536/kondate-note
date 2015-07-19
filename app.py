from bottle import route, run, template
import db

@route('/')
def kondate():
    menus = db.menus.select().execute().fetchall()
    return template('kondate', menus=menus)


run(host='localhost', port=8080, debug=True, reloader=True)
