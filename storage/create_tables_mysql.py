import mysql.connector

db_conn = mysql.connector.connect(host="localhost",
                                  user="mysql_user",
                                  password="SecuRe_pwd1",
                                  database="orders")

db_cursor = db_conn.cursor()

db_cursor.execute('''
          CREATE TABLE expense
          (id INT NOT NULL AUTO_INCREMENT,
           order_id VARCHAR(36) NOT NULL,
           item_id VARCHAR(36) NOT NULL,
           item_name VARCHAR(250) NOT NULL,
           quantity INTEGER NOT NULL,
           price DECIMAL NOT NULL,
           timestamp VARCHAR(100) NOT NULL,
           date_created VARCHAR(100) NOT NULL,
           trace_id VARCHAR(36) NOT NULL,
           PRIMARY KEY (id))
          ''')

db_conn.commit()
db_conn.close()
