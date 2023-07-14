from sqlalchemy import create_engine

from sqlalchemy.orm import scoped_session, sessionmaker

from sqlalchemy.ext.declarative import declarative_base




# Configure the PostgreSQL database connection

engine = create_engine("postgresql://postgres:Password0#@database1.cuetvdodk2bh.us-east-1.rds.amazonaws.com:5432/ecom")







db = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))




Base = declarative_base()

Base.query = db.query_property()