import os
from flask import Flask, flash, request, redirect, url_for, render_template, g, make_response
from werkzeug.exceptions import HTTPException
from data_base import DB

# конфигурация
DB_FOLDER = 'sqlite/'
DATABASE_PATH = DB_FOLDER+'firstbd.db'
SQL_INIT_PATH = DB_FOLDER+'sq_db.sql'
SECRET_KEY = 'kgf38d6gkio23es2jrdfn324m'
UPLOAD_FOLDER = 'static/images'  # место загрузки файлов
ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg', 'gif'])  # допустимые расширения файла
DEBUG = True #True, иначе log не будет работать

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = SECRET_KEY
app.config.from_object(__name__)

data_base = DB(app.root_path, DATABASE_PATH, SQL_INIT_PATH)

# печать в консоль
def log(text):
    app.logger.info(text)

data_base.log = log    

def allowed_file(filename):  # проверка картинка ли загружена
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])  # основная стр
def index():
    id_user = request.cookies.get('id_user',0,int)
    if request.method == 'POST':
        if 'del_id' in request.form: #удаление поста
            data_base.deletePost(request.form.get('del_id'))
        else:
            message = request.form.get('message')  # получение текста
            f = request.files['img']
            if not (f and allowed_file(f.filename)):  # сохранение картинки
                flash('Недопустимый формат файла', category='error')
            elif not data_base.existPost(message,f.filename):# проверка есть ли уже такой пост
                data_base.addPost(message, f.filename, id_user)
                f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
    
    return render_template('index.html', posts=data_base.getPosts(), id=id_user, nickname = data_base.getUser(id_user)['nickname'])


@app.route('/userlist', methods=['GET', 'POST'])  # стр userlist
def userlist():
    if request.method == 'POST':
        if 'nickname' in request.form: # создать нового пользователя
            nickname = request.form.get('nickname')  # получение имени пользователя
            password = request.form.get('password')  # получение пароля
            
            if len(nickname) < 4 or len(password) < 4:
                flash('Имя/пароль слишком короткое', category='error')  
            elif len(nickname) > 20 or len(password) > 20:
                flash('Имя/пароль слишком длинное. Допускается 20 символов', category='error')
            elif not data_base.existUser(nickname): # проверка есть ли уже такой пользователь
                data_base.addUser(nickname, password)
            
        elif 'del_id' in request.form:
            #удалить пользователя
            del_id = request.form.get('del_id')
            now_id = request.cookies.get('id_user')
            data_base.deleteUser(del_id)
            if del_id==now_id: #заходим за админа, если удалили своего пользователя
                return render_with_cookies(0)
        else: #войти как пользователь
            id_user = request.form.get('id_user', type=int)
            input_password = request.form.get('password_user')
            real_password = data_base.getUser(id_user)['password']
            if input_password==real_password:
                return render_with_cookies(id_user)
    id = request.cookies.get('id_user',0,int)
    return render_template('userlist.html', users=data_base.getUsers(), id = id, nickname = data_base.getUser(id)['nickname'])

def render_with_cookies(id_user):
    content = render_template('userlist.html', users=data_base.getUsers(), id = id_user, nickname = data_base.getUser(id_user)['nickname'])
    result = make_response(content)
    result.set_cookie('id_user', str(id_user))
    return result

@app.post('/like')
def like():
    id = request.form.get('id')
    like = request.form.get('like')
    dislike = request.form.get('dislike')
    # data_base.likePost(id,like,dislike)
    log(id)
    log(like)
    log(dislike)
    return "Ok"
    

#вывод ошибок с котами
@app.errorhandler(HTTPException)
def handle_exception(e):
    return render_template('error_page.html', code=e.code, name=e.name), e.code

@app.teardown_appcontext
def close_db(error):  
    data_base.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=DEBUG)
