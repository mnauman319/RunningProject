from queue import Empty
import pymysql, handler, json, StatisticsService
from run import Run
from flask import Flask, jsonify
from markupsafe import escape
from collections import defaultdict

app = Flask(__name__)
app.config.update(
    testing=True,
    debug=True
)
@app.route("/")
def hello_world():
    return f"<p>Hello, Sam!</p>"

@app.route("/get_run_by_id/<int:id>", methods=['GET'])
def get_run_by_id(id):
    db_conn = database_connection()
    db_conn = db_conn.connect_to_db(db_conn.retrieve_login_data())
    run = Run.from_database(handler.get_run_by_id(db_conn,id)[0])
    print(run.toJSON())
    db_conn.close()
    return run.toJSON()

@app.route("/get_run/<date>", methods=['GET'])
def get_run_by_date(date):
    db_conn = database_connection()
    db_conn = db_conn.connect_to_db(db_conn.retrieve_login_data())
    run = Run.from_database(handler.get_run_by_date(db_conn,date)[0])
    print(run.toJSON())
    db_conn.close()
    return run.toJSON()

@app.route("/get_runs", methods=['GET'])
def get_all_runs():
    db_conn = database_connection()
    db_conn = db_conn.connect_to_db(db_conn.retrieve_login_data())
    runs = handler.get_all_runs(db_conn)
    output = ''
    for run in runs:
        output += Run.from_database(run).toJSON()
    db_conn.close()
    print(output)
    return output

@app.route("/get_runs/<start_date>/<end_date>", methods=['GET'])
def get_runs_in_date_range(start_date, end_date):
    db_conn = database_connection()
    db_conn = db_conn.connect_to_db(db_conn.retrieve_login_data())
    runs = handler.get_runs_in_date_range(db_conn,start_date,end_date)
    output = ''
    for run in runs:
        output += Run.from_database(run).toJSON()
    db_conn.close()
    print(output)
    return output

@app.route("/delete_run/<int:id>", methods=['POST'])
def delete_run_by_id(id):
    db_conn = database_connection()
    db_conn = db_conn.connect_to_db(db_conn.retrieve_login_data())
    handler.delete_run_by_id(db_conn, id)
    return get_all_runs()
    
class database_connection:
    def connect_to_db(self,connect_data):
        conn = pymysql.connect(host=connect_data[0], user=connect_data[1], password=connect_data[2],database=connect_data[3])
        return conn

    def retrieve_login_data(self):
        with open("config.txt", 'r') as myfile:
            data = myfile.read().splitlines()
        username = data[0].split('=')[1].replace(" ","")
        password = data[1].split('=')[1].replace(" ","")
        end_point = data[2].split('=')[1].replace(" ","")
        database = data[3].split('=')[1].replace(" ","")
        return [end_point, username, password, database]




