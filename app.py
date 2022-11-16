import os
from flask import Flask, flash, request, redirect, url_for, render_template
from markupsafe import escape
from werkzeug.exceptions import HTTPException


app = Flask(__name__)

#печать в консоль
def log(text):
    app.logger.info(text)

#url_for берёт ссылку, которая написана над функцией user_form
@app.route("/")
def main_page():
    log("main page")
    return '<a href="'+url_for('user_form')+'">Нажми на меня!</a>'

# get метод срабатывает, когда мы просто заходим на страницу
@app.get("/users")
def user_form():
    return render_template('user_form.html')

# post метод срабатывает, когда отправляется форма
@app.post("/users")
def user_page():
    #здесь все переданные post аргументы
    log(request.form)
    
    n = request.form["name"]
    l = request.form["lastname"]
    return render_template('user_page.html',name=n,lastname=l)

#интересная передача параметра
@app.route('/<text>')
def show_text(text):
    return "Your text is: "+text
    
@app.errorhandler(HTTPException)
def handle_exception(e):
    return render_template('error_page.html',code=e.code,name=e.name), e.code
    
#debug=True, иначе log не будет работать
if __name__ == "__main__":
    # app.secret_key = os.urandom(24)
    app.run(host="0.0.0.0",debug=True)
#код ниже не работать не будет, не добавлять

    
#старая попытка (рабочая)   
# def get_user_page(name, lastname):
    # return render_template('user_page.html',name=name,lastname=lastname)

# @app.route("/users", methods=['GET', 'POST'])
# def users_page():
    # if request.method == 'POST':
        # log(request.form)
        # log(request.args.get)
        # a = request.form
        # return get_user_page(a["name"],a["lastname"])
    # return render_template('user_form.html')
    