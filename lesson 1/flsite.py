from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
	return "some text"


@app.route("/about")
def about():
	return "<h1> About site</h1>"


if __name__ == "__main__":
	app.run(debug=True)
