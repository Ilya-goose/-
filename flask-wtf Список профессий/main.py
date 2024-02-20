from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('index.html', title=title)


@app.route('/list_prof/<list>')
def profs_list(list):
    profs = [
        'инженер-исследователь',
        'пилот',
        'строитель',
        'экзобиолог',
        'врач',
        'инженер по терраформированию',
        'климатолог',
        'помогите',
        'лень',
        'писать',
        'профессии',
        'а',
        'б',
        'в',
        'г',
        'д',
    ]
    return render_template('profs_list.html', title="Список профессий", list_parameter=list, list_profs=profs)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
