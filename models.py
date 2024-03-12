from database import Base
from sqlalchemy import Column, Integer, String



class Post(Base):
    __tablename__ = "states"

    id = Column(Integer,primary_key=True,nullable=False)
    abbreviation = Column(String,nullable=False)
    state = Column(String,nullable=False)
    