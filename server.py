from flask import Flask, render_template

app = Flask(__name__)


@app.route('/page/<times>/<color>')
def hello_world(times, color):
    return render_template("index.html", classname="hello", times=int(times), color=str(color))


@app.errorhandler(404)
def error(error):
    return "Sorry! No response. Try again"


if __name__ == "__main__":
    app.run(debug=True)
