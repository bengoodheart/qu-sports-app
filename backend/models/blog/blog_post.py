from models.db_init import db
from uuid import uuid4
from sqlalchemy_utils import UUIDType, ScalarListType, Timestamp

class BlogPost(db.Model, Timestamp):
    id = db.Column(UUIDType(binary=False), primary_key=True, default=uuid4)
    title = db.Column(db.Text(), nullable=False)
    post= db.Column(db.UnicodeText(), nullable=False)
    tags = db.Column(ScalarListType())
    isDeleted = db.Column(db.Boolean(), default=False)
        
    def __repr__(self):
            return '<BlogPost %r>' % self.title

    def to_dict(self):
        return {
            column.name: getattr(self, column.name, None)
            for column in BlogPost.__table__.columns
        }