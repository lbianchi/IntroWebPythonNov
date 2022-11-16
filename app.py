from flask import Flask, render_template

app = Flask("Olá")

@app.route("/")
def hello():
    return render_template("hello.html")

@app.route("/nome")
def nome():
    return "Lucas Bianchi"

@app.route("/nova aba")
def nova_aba():
    return "<b>Não tem nada aqui</b>"