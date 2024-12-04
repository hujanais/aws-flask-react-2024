from dataclasses import dataclass
import uuid


@dataclass
class DocumentType:  # Enum
    EDUCATION = "Education"
    PASSPORT = "Passport"
    SSN = "ssn"
    OTHER = "Other"


class FormAddressModel:
    def __init__(self, address1: str, address2: str):
        self.address1 = address1
        self.address2 = address2

    def __str__(self):
        return f"FormAddressModel(address1={self.address1}, address2={self.address2})"

    def validate(self):
        if not self.address1:
            raise ValueError("Address1 is required")
        if not self.address2:
            raise ValueError("Address2 is required")
        return True


class AttachedDocumentModel:
    def __init__(
        self, document_url: str, document_name: str, document_type: DocumentType
    ):
        self.id = uuid.uuid4()
        self.document_url = document_url
        self.document_name = document_name
        self.document_type = document_type

    def __str__(self):
        return f"AttachedDocumentModel(id={self.id}, document_url={self.document_url}, document_name={self.document_name}, document_type={self.document_type})"


class FormJsonModel:
    def __init__(self, name: str, email: str, address: FormAddressModel):
        self.form_id = None

        self.docId = None
        self.status = "pending"

        self.name = name
        self.email = email
        self.address = address

        self.documents: list[AttachedDocumentModel] = []

    def add_document(self, document: AttachedDocumentModel):
        self.documents.append(document)

    def remove_document(self, docId: uuid.UUID):
        self.documents = [doc for doc in self.documents if doc.id != docId]

    def __str__(self):
        return f"FormJsonModel(form_id={self.form_id} name={self.name}, email={self.email}, address={self.address})"

    def validate(self):
        if not self.name:
            raise ValueError("Name is required")
        if not self.email:
            raise ValueError("Email is required")
        if not self.address1:
            raise ValueError("Address1 is required")
        if not self.address2:
            raise ValueError("Address2 is required")
        if not self.email.count("@") == 1:
            raise ValueError("Invalid email address")
        return True
