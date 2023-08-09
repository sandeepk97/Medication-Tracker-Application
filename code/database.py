import mysql.connector

def get_db_connection():
    db = mysql.connector.connect(
        host='localhost',
        user='b00918c8',
        password='Cab#22se',
        database='b00918c8',
        auth_plugin='mysql_native_password',
    )
    return db
