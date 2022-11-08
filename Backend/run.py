import datetime as dt
import json
import numpy as np
class Run(object):
    id = 0
    def __init__(self, duration:float, distance:float, heart_rate:int, date_run:str, notes:str, run_type:str):
        self.duration = duration
        self.distance = distance
        if duration == None or distance == None:
            self.pace = None
        else:
            self.pace = round(duration / distance,2)
        self.heart_rate = heart_rate
        self.date_run = date_run
        self.notes = notes
        self.run_type = run_type
        self.id += 1
    @classmethod
    def from_database(cls, args):
        run = cls(args[1],args[2],args[4],args[5].strftime("%Y-%m-%d"),args[6],args[7])
        run.id = args[0]
        return run
    @classmethod
    def from_dictionary(cls, dic):
        args = []
        for key in dic.keys():
            if key == "Date":
                val = dt.datetime.strptime(dic[key],"%m/%d/%Y").strftime("%Y-%m-%d")
                args.append(val)
            else:
                args.append(dic[key])
        run = cls(args[0],args[1],args[3],args[4],args[5],args[6])
        return run

    def toJSON(self):
        return json.dumps(self,default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def to_database_form(self):
        return (self.duration, self.distance, self.pace, self.heart_rate,  dt.datetime.strptime(self.date_run, "%Y-%m-%d"), self.notes, self.run_type)
    