import urllib
import flask

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os

app = Flask('__main__')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
