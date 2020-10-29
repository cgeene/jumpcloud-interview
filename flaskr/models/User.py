
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base
 
 
Base = declarative_base()
 
 
class User(Base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    name = Column(String)
