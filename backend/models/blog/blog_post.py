from models.db_init import db
from uuid import uuid4
from sqlalchemy_utils import UUIDType, ScalarListType, Timestamp

class BlogPost(db.Model, Timestamp):
    id = db.Column(UUIDType(binary=False), primary_key=True, default=uuid4)
    title = db.Column(db.Text(), nullable=False)
    post= db.Column(db.UnicodeText(), nullable=False)
    tags = db.Column(ScalarListType())
    isDeleted = db.Column(db.Boolean(), default=False)