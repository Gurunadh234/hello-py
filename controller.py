from flask import Flask

app = Flask(__name__)

@app.route('/hello', methods = ['GET'])
def hello():
    return "<h1>Hello world!!!!</h1>"


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>Error: Page not found</h1>", 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000)
