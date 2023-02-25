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

db.init_app(app)

with app.app_context():
    db.create_all()
    db.session.commit()

migrate = Migrate(app, db)

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
    db.session.commit()
    return 'Posted'

@app.route('/get')
def getAllPosts():
    rows = db.session.query(BlogPost).all()
    allposts = []
    for row in rows:
        allposts.append(row.to_dict())
    return allposts
