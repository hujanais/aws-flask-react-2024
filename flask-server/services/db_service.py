from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models.user_model import Base, UserModel

DATABASE_URL = "postgresql://myuser:mypassword@localhost:5432/mydatabase"


class DBService:
    def __init__(self):
        self.engine = None  # Initialize engine as None
        try:
            self.engine = create_engine(DATABASE_URL)
            print("Database connection established.")
        except Exception as e:
            print("Error connecting to the database:", e)
            raise  # Re-raise the exception to handle it upstream

    def create_table(self):
        Base.metadata.drop_all(self.engine)
        Base.metadata.create_all(self.engine)

    def add_user(self, name, email):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        new_user = UserModel(name=name, email=email)
        try:
            session.add(new_user)
            session.commit()
        except Exception as e:
            session.rollback()
            print("Error adding user:", e)
            raise
        finally:
            session.close()
