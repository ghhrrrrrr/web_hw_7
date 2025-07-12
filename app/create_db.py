
from app.db import Base, engine
from app import models  

def create_tables():
    Base.metadata.create_all(bind=engine)
    print("created")

if __name__ == "__main__":
    create_tables()
