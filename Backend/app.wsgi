#! /usr/bin/python3.7
import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/home/ec2-user/RunningProject/Backend')
from app import app as application
application.secret_key = 'my_secret'