import sqlite3
import os


class Bd:
    def __init__(self):
        try:
            path=os.path.join(os.path.dirname(__file__),'store.bd')
            self.conection=sqlite3.connect(path)
        except Exception as e:
            print("error ",e)
    def execute_query(self,query):
        try:
            conn=self.conection
            cursor=conn.cursor()
            cursor.execute(query)
            conn.commit()
        except Exception as e:
            print("error execute query",e)
    
    def get_data(self,query):
        try:
            conn=self.conection
            cursor=conn.cursor()
            cursor.execute(query)
            data=cursor.fetchall()
            return data
        except Exception as e:
            print("get data",e)
