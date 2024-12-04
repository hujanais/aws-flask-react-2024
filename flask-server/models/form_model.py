import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Sequence
from sqlalchemy.dialects.postgresql import JSON
from models.base import Base


class FormModel(Base):
    __tablename__ = "forms"

    form_id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    creation_date = Column(DateTime, default=datetime.datetime.utcnow)
    modified_date = Column(
        DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow
    )
    user_id = Column(Integer, nullable=False)
    meta_data = Column(JSON, nullable=False)
    form_body = Column(JSON, nullable=False)
