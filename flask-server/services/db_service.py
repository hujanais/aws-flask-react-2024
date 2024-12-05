import jsonpickle
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.applicant_dbmodel import Applicant, Person

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

    def add_person(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        new_person = Person(name="Applicant's spouse", email="jd@email.com", age=30)
        new_child1 = Person(name="child-1", email="child1@email.com", age=5)
        new_child2 = Person(name="child-2", email="child2@email.com", age=5)
        new_applicant = Applicant(name="Applicant", email="jane@email.com")
        new_applicant.spouse.append(new_person)
        new_applicant.children.extend([new_child1, new_child2])
        try:
            session.add(new_applicant)
            session.commit()

            print(f"Added new_applicant: {new_applicant.spouse}")
            print(f"Added new_person: {new_person.spouse_of}")
        except Exception as e:
            session.rollback()
            print("Error adding person:", e)
            raise
        finally:
            session.close()

    # def add_user(self, name, email):
    #     Session = sessionmaker(bind=self.engine)
    #     session = Session()
    #     new_user = UserModel(name=name, email=email)
    #     try:
    #         session.add(new_user)
    #         session.commit()
    #     except Exception as e:
    #         session.rollback()
    #         print("Error adding user:", e)
    #         raise
    #     finally:
    #         session.close()

    # def add_form(self, user_id, form_body: FormJsonModel):
    #     Session = sessionmaker(bind=self.engine)
    #     session = Session()
    #     new_form = FormModel(
    #         user_id=user_id, meta_data={"meta": "data"}, form_body=form_body
    #     )
    #     try:
    #         session.add(new_form)
    #         session.commit()
    #     except Exception as e:
    #         session.rollback()
    #         print("Error adding form:", e)
    #         raise
    #     finally:
    #         session.close()

    # def get_form(self, form_id) -> FormJsonModel:
    #     Session = sessionmaker(bind=self.engine)
    #     session = Session()
    #     form = session.query(FormModel).filter_by(form_id=form_id).first()
    #     session.close()
    #     if form is not None:
    #         jsonObj: FormJsonModel = jsonpickle.loads(form.form_body)
    #         jsonObj.form_id = form.form_id
    #         return jsonObj
    #     return None
