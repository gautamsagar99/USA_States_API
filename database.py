from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:root@localhost/sample'
SQLALCHEMY_DATABASE_URL = 'postgresql://root:87Jjc2Ffx83SF9hhFFpm2Fvu42pOWIxY@dpg-cnn8c1f79t8c739hi96g-a.oregon-postgres.render.com/autozone'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()