import psycopg2

class DAO:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                user = 'postgres',
                password = 'fiona',
                host = 'localhost',
                port = '5432',
                database = 'toDo_list'
            )
        except Exception as error:
            print(f"Oops! ocurrio un error: {error}\nException TYPE:\n {type(error)}")
    
    def print_task_list(self):
        sql_sentence = "SELECT * FROM task_list;"
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql_sentence)
                data = cursor.fetchall()
                return data
        except psycopg2.Error as error:
                print(f"Ocurr6io un error {error}")
                print(f"Tipo de excepcion: {type(error)}")