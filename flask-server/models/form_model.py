from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON

db = SQLAlchemy()


class FormModel(db.Model):
    __tablename__ = "forms"

    form_id = db.Column(db.String, primary_key=True)
    creation_date = db.Column(db.DateTime, default=datetime.timezone.utc)
    modified_date = db.Column(db.DateTime, onupdate=datetime.timezone.utc)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    form_body = db.Column(JSON, nullable=False)

    def __init__(self, form_id, user_id, form_body):
        self.form_id = form_id
        self.user_id = user_id
        self.form_body = form_body
