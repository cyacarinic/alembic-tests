from sqlalchemy import Column
from sqlalchemy import Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'usernew'
    id = Column(Integer, primary_key=True)
    guid = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    biography = Column(String)

    def __repr__(self):
        return '<User %d|%s>' % (self.id, self.email)
