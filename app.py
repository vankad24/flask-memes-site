import os
import sqlite3
from FDataBase import FDataBase
from flask import Flask, flash, request, redirect, url_for, render_template, g, make_response
from markupsafe import escape
from werkzeug.exceptions import HTTPException

# конфигурация
DATABASE = 'bd/firstbd.db'
DEBUG = True
SECRET_KEY = 'kgf38d6gkio23es2jrdfn324m'

UPLOAD_FOLDER = 'static/images'  # место загрузки файлов
ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg', 'gif'])  # допустимые расширения файла

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'kgf38d6gkio23es2jrdfn324m'
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'firstbd.db')))


def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn


def create_db():  # вспосогательная функция для создания таблиц БД
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():  # соединение с БД, если оно не установлено
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


# печать в консоль
def log(text):
    app.logger.info(text)


def allowed_file(filename):  # проверка картинка ли загружена
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])  # основная стр
def index():
    db = get_db()
    dbase = FDataBase(db)
    global id_user
    if request.method == 'POST':
        message = request.form.get('message')  # получение текста
        f = request.files['img']
        if f and allowed_file(f.filename):  # сохранение картинки
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
            noRepetitions = True
            for m in dbase.getPosts():  # проверка есть ли уже такой пост
                if m[2] == message and m[3] == f.filename:
                    noRepetitions = False
                    break
            if noRepetitions:
                if request.cookies.get('id_user'):
                    id_user = request.cookies.get('id_user')
                res = dbase.addPost(message, f.filename, int(id_user))
                if not res:
                    flash('Ошибка добавления поста', category='error')
                else:
                    flash('Пост создан', category='success')
        else:
            flash('Недопустимый формат файла', category='error')
    return render_template('index.html', posts=dbase.getPosts())


id_user = '0'


@app.route('/userlist', methods=['GET', 'POST'])  # стр userlist
def userlist():
    db = get_db()
    dbase = FDataBase(db)
    global id_user
    content = render_template('userlist.html', users=dbase.getUsers())
    result = make_response(content)
    if request.method == 'POST':
        if request.form.get('nickname'):
            nickname = request.form.get('nickname')  # получение имени пользователя
            password = request.form.get('password')  # получение пароля
            if len(nickname) <= 20 and len(password) <= 20 \
                    and len(nickname) >= 4 and len(password) >= 4:
                noRepetitions = True
                for m in dbase.getUsers():  # проверка есть ли уже такой пользователь
                    if m[1] == nickname and m[2] == password:
                        noRepetitions = False
                        break
                if noRepetitions:
                    res = dbase.addUser(nickname, password)
                    if not res:
                        flash('Ошибка добавления пользователя', category='error')
                    else:
                        flash('Пользователь создан', category='success')
            elif len(nickname) > 20 or len(password) > 20:
                flash('Имя/пароль слишком длинное. Допускается 20 символов', category='error')
            else:
                flash('Имя/пароль слишком короткое', category='error')
            content = render_template('userlist.html', users=dbase.getUsers())
            result = make_response(content)
        else:
            content = render_template('userlist.html', users=dbase.getUsers())
            result = make_response(content)
            id_user1 = request.form.get('id_user')
            result.set_cookie('id_user', id_user1)
    return result


@app.errorhandler(HTTPException)
def handle_exception(e):
    return render_template('error_page.html', code=e.code, name=e.name), e.code


@app.teardown_appcontext
def close_db(error):  # закрываем соединение с БД, если оно было установлено
    if hasattr(g, 'link_db'):
        g.link_db.close()


# debug=True, иначе log не будет работать
if __name__ == "__main__":
    # app.secret_key = os.urandom(24)
    app.run(host="0.0.0.0", debug=True)
