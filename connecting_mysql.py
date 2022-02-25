#import required modules
#This module is/was used in testing connection with MySQL Database.
import db_func#User written Module
from time import sleep
import mysql.connector as mysql
from mysql.connector import errorcode
from getpass import getpass

host="localhost"
username='anirudh'
password='root'
data="gAAAAABiGRdd5BIiWPuiJzVPrzK6jIp3XUToUVoKAbHUSXHz12CRRTwd5SaG81Wa"
db=db_func.connect(username, password, 'testing_env',host=host)
cursor_obj=db.cursor()
print("Successfully Connected to DB")
statement='create table if not exists passwords(AccName varchar(100),passw varchar(256));'
cursor_obj.execute(statement)
name=input('Enter account name:')
passw="gAAAAABiGRdd5BIiWPuiJzVPrzK6jIp3XUToUVoKAbHUSXHz12CRRTwd5SaG81Wa"
query='insert into passwords values("{}","{}");'.format(name,passw)
db_func.exec(cursor_obj, query)
print("Inserted all input")
op=db_func.display(cursor_obj, 'select * from passwords')
for i in op:
    for j in i:
        print("{}:{}".format(i,j))
#cursor_obj.execute('commit')
db.close()
