from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from configparser import RawConfigParser
import os


db = SQLAlchemy()


app = Flask(__name__)

thisfolder = os.path.dirname(os.path.abspath(__file__))
inifile = os.path.join(thisfolder, 'conf.ini')


configur = RawConfigParser()
configur.read(inifile)

database = dict(configur.items('database'))

for config in database:
    app.config[config.upper()]=database[config]


db.init_app(app)
with app.app_context():
    from app.models import todo
    db.create_all(app=app)


from app.routes.route import update,hello_world,products,delete





