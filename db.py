import mysql.connector
def create_connection():
    host_name = 'localhost'
    user_name = '**YOUR USERNAME**'
    password_name = '**YOUR PASSWORD**'
    database_name = 'minor_project'

    conn = mysql.connector.connect(host=host_name,user=user_name,password = password_name,database = database_name)
    
    return conn
def insert_login(data):
    conn = create_connection()

    cursor = conn.cursor()
    query = "INSERT INTO `login` VALUES (%s,%s,%s,%s,%s);"

    cursor.execute(query,data)
    conn.commit()

def check_login(data):
    conn = create_connection()
    cursor = conn.cursor()
    query = "SELECT username FROM login WHERE username = %s and password = %s"

    cursor.execute(query,data)

    result = cursor.fetchone()

    if result:
        return result
    
    return False

def insert_history(data):
    conn = create_connection()
    cursor = conn.cursor()
    query = "INSERT INTO histories values(%s,%s,concat(curdate(),' ',curtime()),%s);"

    cursor.execute(query,data)

    conn.commit()

def show_history(data):
    conn = create_connection()
    cursor = conn.cursor()
    query = "SELECT history,category FROM histories WHERE username = %s ORDER BY date desc"

    cursor.execute(query,data)

    result = cursor.fetchall()

    return result

