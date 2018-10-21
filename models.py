from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.sqlite import \
            BLOB, BOOLEAN, CHAR, DATE, DATETIME, DECIMAL, FLOAT, \
            INTEGER, NUMERIC, SMALLINT, TEXT, TIME, TIMESTAMP, \
            VARCHAR
from sqlalchemy.sql import select
from app import db


engine = create_engine('sqlite:///movelit.db', echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

# Set your classes here.

class District(Base):
    __tablename__ = 'districts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(TEXT, nullable=False)
    geometry = db.Column(TEXT, nullable=True)


    def __init__(self, name=None, geometry=None):
        self.name = name
        self.password = password


# Create tables.
# Base.metadata.create_all(bind=engine)
