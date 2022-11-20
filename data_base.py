# from flask import Flask, g
import os
import sqlite3, datetime, math
from flask import Flask, flash

class DB:
    def __init__(self, root, db, sql):
        self.sql_path = sql
        self.db_path = db
        self.root_path = root
        self.full_path = os.path.join(root,db)
        self.connected = False 
      

    def get_db(self):  
        if not self.connected:# соединение с БД, если оно не установлено
            db_exist = os.path.exists(self.full_path)
            self.db = sqlite3.connect(self.full_path, check_same_thread=False)#?
            self.db.row_factory = sqlite3.Row
            self.connected = True
            if not db_exist: # запись в БД, если она пустая
                with open(self.sql_path) as f:
                    self.db.cursor().executescript(f.read())
                self.db.commit()
            
        return self.db
        
    def close(self):# закрываем соединение с БД, если оно было установлено
        if self.connected:
            self.connected = False
            self.db.close()
            
    def getPosts(self):
        sql = '''SELECT posts.*, users.nickname FROM posts, users WHERE users.id = posts.id_user ORDER BY posts.id DESC'''
        cur = self.get_db().cursor()
        try:
            cur.execute(sql)
            res = cur.fetchall()
            if res:
                return res
        except:
            pass
        return []
        
    def existPost(self, message, image):
        sql = f'''SELECT * FROM posts WHERE message = "{message}" AND image = "{image}"'''
        cur = self.get_db().cursor()
        try:
            cur.execute(sql)
            res = cur.fetchall()
            if res:
                return True
        except: 
            pass
        return False
    
    def addPost(self, message, image, id_user):
        cur = self.get_db().cursor()
        try:
            tm = datetime.datetime.now()  # текущее время
            tm = tm.strftime("%d-%m-%Y %H:%M")
            cur.execute("INSERT INTO posts VALUES(NULL, ?, ?, ?, ?, ?, ?)", (id_user, message, image, 0, 0, tm))
            self.db.commit()
            flash('Пост создан', category='success')
        except sqlite3.Error as e:
            flash('Ошибка добавления поста', category='error')
    
    def deletePost(self, post_id):
        cur = self.get_db().cursor()
        try:
            cur.execute("DELETE FROM posts WHERE id = ?", (post_id,))
            self.db.commit()
            flash('Пост удалён', category='success')
        except sqlite3.Error as e:
            flash('Ошибка удаления', category='error')

    def likePost(self, post_id, likes, dislike):
        cur = self.get_db().cursor()
        try:
            cur.execute("UPDATE posts SET likes = ?, dislikes = ? WHERE id = ?", (like, dislike, post_id,))
            self.db.commit()
            flash('Обновлено', category='success')
        except sqlite3.Error as e:
            flash('Ошибка лайка', category='error')

    def existUser(self, nickname):
        sql = f'''SELECT * FROM users WHERE nickname = "{nickname}"'''
        cur = self.get_db().cursor()
        try:
            cur.execute(sql)
            res = cur.fetchall()
            if res:
                return True
        except: 
            pass
        return False
    
    def getUsers(self):
        sql = '''SELECT * FROM users'''
        cur = self.get_db().cursor()
        try:
            cur.execute(sql)
            res = cur.fetchall()
            if res:
                return res
        except:
            pass
        return []
        
    def getUser(self, id):
        sql = f'''SELECT * FROM users WHERE id = {id}'''
        cur = self.get_db().cursor()
        try:
            cur.execute(sql)
            res = cur.fetchall()
            if res:
                return res[0]
        except:
            pass
        return None

    def addUser(self, nickname, password):
        cur = self.get_db().cursor()
        try:
            cur.execute("INSERT INTO users VALUES(NULL, ?, ?)", (nickname, password))
            self.db.commit()
            flash('Пользователь создан', category='success')
        except sqlite3.Error as e:
            flash('Ошибка добавления пользователя', category='error')
            
    def deleteUser(self, user_id):
        cur = self.get_db().cursor()
        try:
            cur.execute("DELETE FROM users WHERE id = ?", (post_id,))
            self.db.commit()
            flash('Пользователь удалён', category='success')
        except sqlite3.Error as e:
            flash('Ошибка удаления', category='error')

     