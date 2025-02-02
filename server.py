from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def ruwiki():
    return render_template("ruwiki.html")

@app.route("/hello")
def hello():
    return 'привет мир'

@app.route("/max")
def find_max():
    a = int(request.args['a'])
    b = int(request.args['b'])
    if a > b: return f'{a}'
    else: return f'{b}'

@app.route("/sonic")
def sonic_article():
    return render_template('sonic_article.html')


@app.route("/base")
def base():
    return render_template('base.html', title = 'dfnsjdfnjsdfnjsdfn')

if __name__ == '__main__':
    app.run(debug=True)