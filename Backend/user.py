import json

class User:
    def __init__(self, username:str, password:str, f_name:str, l_name: str):
        self.username = username
        self.password = password
        self.f_name = f_name
        self.l_name = l_name
        self.name = f_name + l_name
        self.runs = []
    