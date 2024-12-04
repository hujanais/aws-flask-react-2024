import jsonpickle
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models.form_json_model import FormJsonModel
from models.user_model import UserModel
from models.form_model import FormModel
from models.base import Base

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

    def add_form(self, user_id, form_body: FormJsonModel):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        new_form = FormModel(
            user_id=user_id, meta_data={"meta": "data"}, form_body=form_body
        )
        try:
            session.add(new_form)
            session.commit()
        except Exception as e:
            session.rollback()
            print("Error adding form:", e)
            raise
        finally:
            session.close()

    def get_form(self, form_id) -> FormJsonModel:
        Session = sessionmaker(bind=self.engine)
        session = Session()
        form = session.query(FormModel).filter_by(form_id=form_id).first()
        session.close()
        if form is not None:
            jsonObj: FormJsonModel = jsonpickle.loads(form.form_body)
            jsonObj.form_id = form.form_id
            return jsonObj
        return None
