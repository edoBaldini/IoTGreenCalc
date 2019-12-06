from mip import Model, xsum, BINARY, CBC
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    m = Model(solver_name=CBC)
    app.run(debug=True, host='0.0.0.0')
