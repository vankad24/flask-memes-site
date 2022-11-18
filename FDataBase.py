import sqlite3, datetime, math


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getUsers(self):
        sql = '''SELECT * FROM users'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except:
            print("Ошибка чтения из users")
        return []

    def addUser(self, nickname, password):
        try:
            self.__cur.execute("INSERT INTO users VALUES(NULL, ?, ?)", (nickname, password))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления пользователя в БД " + str(e))
            return False
        return True

    def getPosts(self):
        sql = '''SELECT * FROM posts'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except:
            print("Ошибка чтения из posts")
        return []

    def addPost(self, message, image):
        try:
            tm = datetime.datetime.now()  # текущее время
            tm = tm.strftime("%d-%m-%Y %H:%M")
            self.__cur.execute("INSERT INTO posts VALUES(NULL, ?, ?, ?, ?, ?, ?)", ('Admin', message, image, 0, 0, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления пользователя в БД " + str(e))
            return False
        return True
