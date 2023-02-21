from flask import Flask
from dotenv import load_dotenv
import os
from flask_cors import CORS
from flask_migrate import Migrate

#Model Imports
from models.db_init import db

app = Flask(__name__)
load_dotenv()
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/appTable.db'
migrate = Migrate(app, db)

@app.route('/')
def home():
    return "HELLO WORLD"

@app.route('/site/info')
def info():
    info = {
        "site.name" : "app-template",
        "version": "v0.0.1",
        "status" : "development",
    }
    
    return info

