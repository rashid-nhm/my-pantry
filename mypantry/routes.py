from mypantry import app


@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    return "Hello World!"
