from sqlalchemy import Column, Integer, Sequence, String
from sqlalchemy.ext.declarative import declarative_base
from models.base import Base


class UserModel(Base):
    __tablename__ = "users"

    userId = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    name = Column(String(50))
    email = Column(String(50))
