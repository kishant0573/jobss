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
       query = "INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url,position) VALUES (%s, %s, %s, %s, %s, %s, %s,%s)"
       values = (id, data["full_name"], data["email_id"], data["linkedin_url"], data["Education"], data["work_experience"], data["resume_url"],data['position'])
       cursor.execute(query, values)
       connection.commit()
    finally:
      if connection:
        connection.close()



def logins(user_id,password):
    connection = None
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query="select user_id from users_login where user_id=%s and password=%s" 
        cursor.execute(query,(user_id,password))
        result = cursor.fetchone()
        if result:
           return result
        else:
            return None 
    finally:
        if connection:
            connection.close()



def register(user_id,user_name,password):
    connection = None
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query0 ="select * from users_sign where user_id = %s"
        value0 = user_id
        result0 = cursor.execute(query0,value0)
        if result0:
            return False
        query1 = "insert into users_sign(user_id,user_name,password) values (%s,%s,%s)"
        values1 = (user_id,user_name,password)
        cursor.execute(query1,values1)
        query2 = "insert into users_login(user_id,password) values (%s,%s)"
        values2 = (user_id,password)
        cursor.execute(query2,values2)
        connection.commit()
        return "successfully"
    finally:
        if connection:
            connection.close()


def count_application():
    connection = None
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "select count(*) from applications"
        cursor.execute(query)
        result = cursor.fetchone()
        return result
    finally:
        if connection:
            connection.close()
def show_in_table():
    connection = None
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "SELECT * FROM applications"
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    finally:
        if connection:
            connection.close()


def categories():
    connection = None
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "select distinct position from applications where position is not NULL"
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    finally:
        if connection:
            connection.close()

def admin_login(user_id,password):
    connection = None
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "select * from admin_login where user_id=%s and password=%s"
        values = (user_id, password)
        cursor.execute(query,values)
        result = cursor.fetchone()
        return result
    finally:
        if connection:
            connection.close()
            

