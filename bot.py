# -*- encoding: utf-8 -*-
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hoge():
    return "hoge"


if __name__ == "__main__":
    # off: debug=True
    # off: port=5000
    app.run(host="0.0.0.0")
