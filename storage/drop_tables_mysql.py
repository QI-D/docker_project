import mysql.connector

db_conn = mysql.connector.connect(host="localhost",
                                  user="mysql_user",
                                  password="SecuRe_pwd1",
                                  database="orders")

db_cursor = db_conn.cursor()
db_cursor.execute(''' DROP TABLE expense ''')
db_conn.commit()
db_conn.close()
