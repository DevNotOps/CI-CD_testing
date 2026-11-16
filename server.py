import flask

app = flask.Flask(__name__)

@app.route("/")
def hello():
    return "DevOps is awesome!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)