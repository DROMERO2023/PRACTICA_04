# log.py
import sqlite3

class Log:
    def __init__(self, bdName='logDatabase'):
        self.bdName = f'{bdName}.db'
        try:
            self.conexion = sqlite3.connect(self.bdName)
            self.cursor = self.conexion.cursor()
            self.newTable('log', 'id INTEGER PRIMARY KEY, info TEXT NOT NULL')
        except Exception as e:
            print('error', e)

    def newTable(self, tabla, sentencia):
        try:
            query = "CREATE TABLE IF NOT EXISTS {} ({});".format(tabla, sentencia)
            cursor = self.cursor
            cursor.execute(query)
            self.conexion.commit()
        except Exception as e:
            print('error', e)

    def register_log(self, info):
        try:
            query = f"INSERT INTO log (info) VALUES ('{info}')"
            cursor = self.cursor
            cursor.execute(query)
            self.conexion.commit()
        except Exception as e:
            print('error', e)

    def lecturaTabla(self, tabla):
        try:
            query = f"SELECT * FROM {tabla};"
            cursor = self.cursor
            cursor.execute(query)
            data = cursor.fetchall()
            print(data)
            return data
        except Exception as e:
            print('error', e)

    def closedBd(self):
        self.conexion.close()

# Uso del Log
# logger = Log()
# logger.register_log('Información que quieres guardar en el log')
# logger.lecturaTabla('log')
# logger.closedBd()

