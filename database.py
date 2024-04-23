import pymysql
import os
timeout = 10
def get_connection():
    connection = pymysql.connect(
        charset="utf8mb4",
        connect_timeout=timeout,
        cursorclass=pymysql.cursors.DictCursor,
        db=os.environ['DATABASE_NAME'],
        host=os.environ['DATABASE_HOST'],
        password=os.environ['DATABASE_PASSWORD'],
        read_timeout=timeout,
        port=int(os.environ['DATABASE_PORT']),
        user=os.environ['DATABASE_USER'],
        write_timeout=timeout,
    )
    return connection



def load_jobs_from_db():
  try:
    connection = get_connection()
    cursor = connection.cursor()
    # print("connection succesfully")
    cursor.execute("select * from jobs")
    return cursor.fetchall()
  finally:
    connection.close()