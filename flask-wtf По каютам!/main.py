from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('index.html', title=title)


@app.route('/distribution')
def distribution():
    list_of_astronauts = [
        'Ридли Скотт', 'Энди Уир',
        'Марк Уотни', 'Венката Капур',
        'Тедди Сандерс', 'Шон Бин'
    ]

    return render_template('index.html', title="По каютам!", list_names=list_of_astronauts)


if __name__ == '__main__':    app.run(port=8080, host='127.0.0.1')
