from . import model_connector

def get_user_info():
    cursor, mydb = model_connector.mysql_db_info()
    mysql = "SELECT currency, price, date FROM coin_info WHERE exchange_name = 'coinone' AND id = (SELECT MAX(id) FROM coin_info WHERE exchange_name = 'coinone') ORDER BY DATE DESC"
    cursor.execute(mysql)
    result = cursor.fetchall()
    cursor.close()
    mydb.close()
    return result

# mysql = "select * from user"
# cursor.execute(mysql)
# resultall = cursor.fetchall()
# for row in resultall
#     print(row)
#
# mysql = "select user_name from user"
# cursor.execute(mysql)
# result = cursor.fetchone()
# for row in result
#     print(row)

