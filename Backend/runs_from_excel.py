from app import database_connection
import pandas as pd
from run import Run
import handler
db = database_connection()
conn = db.connect_to_db(db.retrieve_login_data())

read_path = r"C:/Users/Mnaum/Downloads/Running Progress - Sheet1.csv"

data = pd.read_csv(read_path, encoding="ISO-8859-1")
column_names = list(data.columns)[:7]
vals = {}
for column in column_names:
    vals.update({column:0})
runs = []
for i in range(len(data[column_names[0]])):
    for column in column_names:
        null_rows = [False for i in range(len(data[column_names[0]]))]
        if data[column].isnull().any():
            null_rows = data[column].isnull()
        if null_rows[i] == True:
            vals.update({column: None})
        elif column == "Date":
            vals.update({column: data[column][i]+"/2022"})
        else: 
            vals.update({column: data[column][i]})
    runs.append(Run.from_dictionary(vals))     

for run in runs:
    handler.create_run(conn,run)
