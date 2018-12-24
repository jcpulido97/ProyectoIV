import urllib
import flask
import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os

app = Flask('__main__')
if os.environ.get('DATABASE_URL'):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
else:
    print("ERROR: DATABASE_URL not set", file=sys.stderr)
    sys.exit()

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
