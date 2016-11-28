from flask import Flask

app = Flask(__name__)

cookies = 0


@app.route("/")
def hello():
    return "Hello cookie eater friend! "


@app.route("/cookies")
def getCookies():
    global cookies
    cookies += 1
    return "I have {} cookies !".format(cookies)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
