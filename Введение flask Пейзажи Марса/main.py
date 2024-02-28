from flask import Flask

app = Flask(__name__)


@app.route('/carousel')
def carousel():
    return

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
