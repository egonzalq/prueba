from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/crear')
def crear():
    return render_template("crear.html")

@app.route('/consultar')
def consultar():
    return render_template("consultar.html")

@app.route('/borrar')
def borrar():
    return render_template("borrar.html")

@app.route('/editar')
def editar():
    return render_template("editar.html")

# @app.route('/index')
# def principal():
#     return render_template("index.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")


if __name__=="__main__":
    app.run(host="127.0.0.1",port=5000, debug=True)    