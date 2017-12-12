import psycopg2
from psycopg2.extras import execute_values, execute_batch
class Db():
    def __init__(self, db="chatbot", user="postgres", password="76832dc", host="127.0.0.1", port="5432"):
        try:
            self.conn = psycopg2.connect(database=db, user=user, password=password, host=host, port=port)
            self.cur = self.conn.cursor()
            print("Connected")
        except Exception as e:
            print("I am unable to connect to the database - {}".format(e))

    def query(self, query):
        try:
            self.cur.execute(query)
        except Exception as e:
            print("{}".format(e))

    def query_execute_values(self, query, values_list, template=None, page_size=100):
        try:
            execute_values(self.cur, query, values_list, template, page_size)
        except Exception as e:
            print("{}".format(e))

    def create(self, query):
        try:
            self.cur.execute(query)
            self.conn.commit()
        except Exception as e:
            print("{}".format(e))

    def close(self):
        self.cur.close()
        self.conn.close()

# db = Db()
# db.query("SELECT * FROM test_conn;")
# rows = db.cur.fetchall()
# print(db.cur.fetchall())
# db.close()