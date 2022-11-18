import os
from flask import Flask, flash, request, redirect, url_for, render_template
from markupsafe import escape
from werkzeug.exceptions import HTTPException

UPLOAD_FOLDER = 'static/images'
ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'kgf38d6gkio23es2jrdfn324m'

# печать в консоль
def log(text):
    app.logger.info(text)


def allowed_file(filename):  # проверка картинка ли загружена
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])  # основная стр
def index():
    if request.method == 'POST':
        message = request.form.get('message')  # получение текста
        f = request.files['img']
        if f and allowed_file(f.filename):  # сохранение картинки
            flash('Пост создан', category='success')
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        else:
            flash('Недопустимый формат файла', category='error')
    return render_template('index.html')


@app.route('/userlist', methods=['GET', 'POST'])  # стр userlist
def userlist():
    if request.method == 'POST':
        nickname = request.form.get('nickname')  # получение имени пользователя
        password = request.form.get('password')  # получение пароля
        if len(nickname) <= 20 and len(password) <= 20 \
           and len(nickname) >= 4 and len(password) >= 4:
            flash('Пользователь создан', category='success')
        elif len(nickname) > 20 or len(password) > 20:
            flash('Имя/пароль слишком длинное. Допускается 20 символов', category='error')
        else:
            flash('Имя/пароль слишком короткое', category='error')
            
    return render_template('userlist.html')


@app.errorhandler(HTTPException)
def handle_exception(e):
    return render_template('error_page.html', code=e.code, name=e.name), e.code


# debug=True, иначе log не будет работать
if __name__ == "__main__":
    # app.secret_key = os.urandom(24)
    app.run(host="0.0.0.0", debug=True)

# url_for берёт ссылку, которая написана над функцией user_form
# @app.route("/")
# def main_page():
#    log("main page")
#    return '<a href="'+url_for('user_form')+'">Нажми на меня!</a>'

# post метод срабатывает, когда отправляется форма
# @app.post("/users")
# def user_page():
# здесь все переданные post аргументы
#    log(request.form)    
#    n = request.form["name"]
#    l = request.form["lastname"]
#    return render_template('user_page.html',name=n,lastname=l)

# интересная передача параметра
# @app.route('/<text>')
# def show_text(text):
#    return "Your text is: "+text
