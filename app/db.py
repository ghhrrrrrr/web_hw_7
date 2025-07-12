from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "postgresql+psycopg2://postgres:123123@localhost:5432/postgres"

engine = create_engine(DATABASE_URL, echo=True)
dbSesssion = sessionmaker(bind=engine)
session = dbSesssion()
Base = declarative_base()



