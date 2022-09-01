import psycopg2
from datetime import datetime

db_name = 'YaDB'
db_user = 'YaUser'
db_pass = 'YaPassword'
db_host = 'localhost'
db_port = '5432'
# Connecto to the database
conn = psycopg2.connect(dbname = db_name, user = db_user, password = db_pass, host = db_host, port = db_port)
cursor = conn.cursor()

cursor.execute('SELECT * FROM numbers LIMIT 10')
records = cursor.fetchall()


if len(records) > 0:
    last_id = records[-1][0]
else:
    last_id = 0
now_time = int(datetime.now().timestamp())

insert = """INSERT INTO numbers (number, timestamp) VALUES ({}, {})""".format(last_id + 1, now_time)
cursor.execute(insert)
conn.commit()

# cursor.execute('SELECT * FROM numbers LIMIT 10')
# records = cursor.fetchall()

# print(records)
cursor.close()
conn.close()