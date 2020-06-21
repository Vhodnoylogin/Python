import math
import sqlite3
import time


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__curr = db.cursor()

    def get_menu(self):
        sql = """select id, title, url from mainmenu"""
        try:
            self.__curr.execute(sql)
            res = self.__curr.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print('Ошибка чтения из БД ' + str(e))
        return []

    def add_post(self, title, text):
        sql = """insert into posts values (null, ?,?,?)"""
        try:
            tm = math.floor(time.time())
            self.__curr.execute(sql, (title, text, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Ошибка добавления статьи в БД ' + str(e))
            return False
        return True

    def get_post(self, post_id):
        sql = f"""select title, text from posts where id = {post_id} limit 1"""
        try:
            self.__curr.execute(sql)
            res = self.__curr.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print('Ошибка чтения из БД ' + str(e))
        return False, False

    def get_posts_annonce(self):
        sql = f"""select id, title, text from posts order by time desc """
        try:
            self.__curr.execute(sql)
            res = self.__curr.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print('Ошибка чтения из БД ' + str(e))
        return []
