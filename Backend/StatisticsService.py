import handler
import json
from run import Run
import datetime as dt
import pymysql

def get_weekly_totals(conn:pymysql.connect,start_date:str):
    end_date = dt.datetime.strptime(start_date, '%Y-%m-%d').date()+dt.timedelta(days=7)
    data = handler.get_runs_in_date_range(conn, start_date, end_date)
    totals = {
    "duration": 0,
    "distance": 0,
    "pace": 1,
    "heart_rate": 0,
    }
    print('\n')
    for row in data:
        totals["duration"] = round(totals["duration"] + row[1],2)
        totals["distance"] = round(totals["distance"] + row[2],2)
        totals["heart_rate"] += row[4]
    totals["heart_rate"] /= round(len(data),2)
    totals["pace"] = totals["duration"] / totals["distance"]
    totals["pace"] = int(totals["pace"]) + round((totals["pace"]-int(totals["pace"]))*.60,2)
    return json.dumps(totals)

    
