from tracemalloc import start
import pymysql
from run import Run
import datetime as dt
from user import User
def get_all_runs(conn:pymysql.connect):
    cursor = conn.cursor()
    sql = 'select * from runs'
    cursor.execute(sql)
    data = cursor.fetchall()
    return data

def get_run_by_id(conn:pymysql.connect, id:int):
    cursor = conn.cursor()
    sql = 'select * from runs where id = %s'
    cursor.execute(sql, id)
    data = cursor.fetchall()
    if data == ():
        raise ValueError("There is no run with id of " + str(id) + " enter a valid id." )
    return data

def get_run_by_date(conn:pymysql.connect, date:str):
    cursor = conn.cursor()
    sql = 'select * from runs where date_run = %s'
    cursor.execute(sql, date)
    data = cursor.fetchall()
    if data == ():
        raise ValueError("There is no run with date of " + str(date) + " enter a valid date." )
    return data

# def get_runs_by_user(conn:pymysql.connect, user:User):


def get_runs_in_date_range(conn:pymysql.connect, start_date:str, end_date:str):
    cursor = conn.cursor()
    sql = 'select * from runs where date_run >= %s and date_run <= %s'
    cursor.execute(sql, [start_date, end_date])
    data = cursor.fetchall()
    return data


def create_run(conn:pymysql.connect, run:Run):
    cursor = conn.cursor()
    sql = 'Insert into runs(duration,distance,pace,heart_rate,date_run,notes, run_type) values(%s, %s, %s, %s, %s, %s, %s);'
    cursor.execute(sql, run.to_database_form())
    conn.commit()

def delete_run_by_id(conn:pymysql.connect, id:int):
    try:
        get_run_by_id(conn, id) == ()
    except ValueError as e:
        return e
    cursor = conn.cursor()
    sql = 'delete from runs where id = %s'
    cursor.execute(sql, id)
    conn.commit()
    return get_all_runs(conn)