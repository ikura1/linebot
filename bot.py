from flask import Flask

app = Flask(__name__)


@app.route("/")
def hoge():
    return "hoge"


if __name__ == "__main__":
    # off: -*- encoding: utf-8 -*-
    # off: debug=True
    # off: port=5000
    # off: host="0.0.0.0"
    app.run()
