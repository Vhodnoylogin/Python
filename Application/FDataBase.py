import math
import sqlite3
import time


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__curr = db.cursor()

    def get_menu(self):
        sql = """select * from mainmenu"""
        try:
            self.__curr.execute(sql)
            res = self.__curr.fetchall()
            if res:
                return res
        except:
            print('Ошибка чтения из БД')
        return []

    def add_post(self, title, text):
        sql = """insert into posts values (null, ?,?,?)"""
        try:
            tm = math.floor(time.time())
            self.__curr.execute(sql, (title, text, tm))
            self.__db.submit()
        except sqlite3.Error as e:
            print('Ошибка добавления статьи в БД ' + str(e))
            return False
        return True
