from models.db_init import db
from uuid import uuid4
from sqlalchemy_utils import UUIDType, ScalarListType

class Post(db.Model):
    id = db.Column(UUIDType(binary=False), primary_key=True, default=uuid4)
    title = db.Column(db.Text(), nullable=False)
    post= db.Column(db.UnicodeText(), nullable=False)
    tags = db.Column(ScalarListType())
    isDeleted = db.Column(db.Boolean(default=False))
    startDraftDate = db.Column(db.DateTime())
    postedDate = db.Column(db.DateTime())
    
    
    