class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__curr = db.cursor()

    def getMenu(self):
        sql = """Select * from mainmenu"""
        try:
            self.__curr.execute(sql)
            res = self.__curr.fetchall()
            if res:
                return res
        except:
            print('Ошибка чтения из БД')
        return []
