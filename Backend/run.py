import datetime as dt
from dataclasses import dataclass

class Run(object):
    id = 0
    def __init__(self, duration:float, distance:float, heart_rate:int, date_run:str, notes:str, run_type:str):
        self.duration = duration
        self.distance = distance
        self.pace = duration / self.distance
        self.heart_rate = heart_rate
        self.date_run = date_run
        self.notes = notes
        self.run_type = run_type
        self.id += 1
    
    def to_database_form(self):
        return (self.duration, self.distance, self.pace, self.heart_rate,  dt.datetime.strptime(self.date_run, "%Y-%m-%d"), self.notes, self.run_type)