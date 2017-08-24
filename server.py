import flask
app = flask.Flask(__name__)

@app.route("/")
def home():
    return "Please navigate to an endpoint <pre>/[encoding]</pre> e.g. /big5"

@app.route("/big5")
def big5():
    with open('big5.html', 'rb') as f:
        resp = flask.Response(f.read())
    resp.headers['Content-Type'] = 'text/html; charset=big5'
    return resp

@app.route("/gb2313")
def gb2313():
    with open('gb2313.html', 'rb') as f:
        resp = flask.Response(f.read())
    resp.headers['Content-Type'] = 'text/html; charset=GB2313'
    return resp
