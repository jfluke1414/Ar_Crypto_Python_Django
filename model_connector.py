import mysql.connector

# class mysql_connect_info:
def mysql_db_info():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234", database="cryptohard")
    cursor = mydb.cursor()
    return cursor, mydb

def sqlite3_db_info():
    db = ""
    return db





