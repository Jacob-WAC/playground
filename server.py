from flask import Flask, render_template

app = Flask(__name__)


@app.route('/page')
def hello_world():
    return render_template("index.html", classname="hello", times=3, color='blue')


@app.route('/page/<times>')
def other(times):
    return render_template("index.html", classname="hello", times=int(times), color='green')


@app.route('/page/<times>/<color>')
def other_other(times, color):
    return render_template("index.html", classname="hello", times=int(times), color=str(color))


@app.errorhandler(404)
def error(error):
    return "Sorry! No response. Try again"


if __name__ == "__main__":
    app.run(debug=True)
