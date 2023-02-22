from flask import Flask
from dotenv import load_dotenv
import os
from flask_cors import CORS
from flask_migrate import Migrate

#Model Imports
from models.db_init import db
from models.blog.blog_post import BlogPost

app = Flask(__name__)
load_dotenv()
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/appTable.db'
migrate = Migrate(app, db)

# TODO: ADD THE CREATE ALL THING

@app.route('/')
def home():
    return "RELEASE ME!!!! I BEG OF YOU!!!!"

@app.route('/site/info')
def info():
    info = {
        "site.name" : "app-template",
        "version": "v0.0.1",
        "status" : "development",
    }
    
    return info


@app.route('/add')
def add():

    
    title = 'Test'
    post = '<h1>Wow</h1><br><p>Today I learned how to code </p>'
    tags = ['wow', 'test', 'cool']
    
    post = BlogPost(
        title=title,
        post=post,
        tags=tags,
        )
    
    db.session.add(post)
    return 'Posted'

    
