from queue import Empty
import pymysql
import handler
from run import Run

def connect_to_db(connect_data):
    conn = pymysql.connect(host=connect_data[0], user=connect_data[1], password=connect_data[2],database=connect_data[3])
    return conn

def retrieve_login_data():
    with open("config.txt", 'r') as myfile:
        data = myfile.read().splitlines()
    username = data[0].split('=')[1].replace(" ","")
    password = data[1].split('=')[1].replace(" ","")
    end_point = data[2].split('=')[1].replace(" ","")
    database = data[3].split('=')[1].replace(" ","")
    return [end_point, username, password, database]


conn = connect_to_db(retrieve_login_data())
run1 = Run(24,2.33, 130,'2022-08-30','On Treadmill','Easy')
handler.create_run(conn,run1)
for item in handler.get_all_runs(conn):
    print(item)

conn.close()


#This is new