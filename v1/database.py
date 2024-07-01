import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = os.environ.get('DATABASE_URL')

engine = create_engine(DATABASE_URL)

session_factory = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()
