from pydantic import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

class Product(BaseModel):
    id: int
    name: str


Base = declarative_base()
class ProductDAO(Base):
    
    __tablename__ = "product"

    id = Column(Integer, autoincrement="auto", index=True, primary_key=True)
    name = Column(String(255))