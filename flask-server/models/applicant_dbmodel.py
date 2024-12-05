from sqlalchemy import ARRAY, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base


class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    age = Column(Integer, nullable=False)
    applicant_id = Column(Integer, ForeignKey("applicant.id"))

    # Relationships
    spouse_of = relationship(
        "Applicant", back_populates="spouse", overlaps="children_of"
    )
    children_of = relationship(
        "Applicant", back_populates="children", overlaps="spouse_of"
    )

    def __repr__(self):
        return f"<Person(name={self.name}, email={self.email}, age={self.age})>"


class Applicant(Base):
    __tablename__ = "applicant"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    # Relationships
    spouse = relationship(
        "Person", back_populates="spouse_of", overlaps="children, children_of"
    )
    children = relationship(
        "Person", back_populates="children_of", overlaps="spouse, spouse_of"
    )

    def __repr__(self):
        return f"<Applicant(name={self.name}, email={self.email})>"
