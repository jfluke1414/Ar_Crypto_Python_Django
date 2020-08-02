from . import model_connector

def insert_user():
    cursor, mydb = model_connector.mysql_db_info()
    cursor.execute("use cryptohard")
    mysql = "insert into user(user_name, user_id, user_pw, regdate) values('inzaghi33', 'inzaghi33@gmail.com', '7b52009b64fd0a2a49e6d8a939753077792b0554', NOW())";
    cursor.execute(mysql)
    mydb.commit()
    cursor.close()
    mydb.close()
insert_user()