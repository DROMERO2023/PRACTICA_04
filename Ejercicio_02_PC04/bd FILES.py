# bd.py
import sqlite3

class Bd:
    def __init__(self, bdName='exampleBdv1'):
        self.bdName = f'{bdName}.db'
        try:
            self.conexion = sqlite3.connect(self.bdName)
            self.cursor = self.conexion.cursor()
        except Exception as e:
            print('error', e)

    # métodos

    def newTable(self, tabla, sentencia):
        try:
            query = "CREATE TABLE IF NOT EXISTS {} ({});".format(tabla, sentencia)
            print(query)
            cursor = self.cursor
            cursor.execute(query)
            self.conexion.commit()
        except Exception as e:
            print('error', e)

    def insertValueOne(self, tabla, sentencia):
        try:
            query = f"""
            INSERT INTO {tabla} VALUES{sentencia};
            """
            cursor = self.cursor
            cursor.execute(query)
            self.conexion.commit()  # confirmación de mi cambio
        except Exception as e:
            print('error', e)

    def insertFromPrompt(self, tabla, sentencia, values):
        query = f"""
            INSERT INTO {tabla} VALUES({sentencia})
        """
        cursor = self.cursor
        cursor.execute(query, values)
        self.conexion.commit()

    def execute_query(self, query, parameters=None):
        try:
            if parameters is None:
                self.cursor.execute(query)
            else:
                self.cursor.execute(query, parameters)

            self.conexion.commit()

            return self.cursor.fetchall()
        except Exception as e:
            print('error', e)

    def lecturaTabla(self, tabla):
        try:
            query = f"SELECT * FROM {tabla};"
            print(query)
            cursor = self.cursor
            cursor.execute(query)
            data = cursor.fetchall()
            print(data)
            return data
        except Exception as e:
            print('error', e)

    def closedBd(self):
        self.conexion.close()


bd1 = Bd('examplewithclass')
# bd1.newTable('useres','nombre varchar(100), dni varchar(100),edad integer')
# bd1.insertValueOne('useres',"('gian','887877',20)")
bd1.lecturaTabla('useres')
