from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "hello world!　成功！！"

@app.route("/saki")
def saki():
    return "saki's page"


if __name__ == '__main__':
    app.run(debug=True)
