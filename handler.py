from sqlite3 import Cursor
import pymysql
import sys
from run import Run


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