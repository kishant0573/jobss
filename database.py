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
    connection = None
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM jobs")
            return cursor.fetchall()
    finally:
        if connection:
            connection.close()

def load_data_for_id(id):
    connection = None
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM jobs WHERE id = %s", (id,))
            result = cursor.fetchall()
            if not result:
                return "<p>Job ID not found</p>"
            else:
                return result[0]
    finally:
        if connection:
            connection.close()
def save_to_db(id,data):
    
    connection = None
    try:
       connection = get_connection()
       cursor = connection.cursor()
       query = "INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (%s, %s, %s, %s, %s, %s, %s)"
       values = (id, data["full_name"], data["email_id"], data["linkedin_url"], data["Education"], data["work_experience"], data["resume_url"])
       cursor.execute(query, values)
       connection.commit()
    finally:
      if connection:
        connection.close()