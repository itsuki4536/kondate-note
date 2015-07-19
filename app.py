from bottle import route, run, template

@route('/')
def kondate():
    return template('kondate')


run(host='localhost', port=8080, debug=True, reloader=True)
