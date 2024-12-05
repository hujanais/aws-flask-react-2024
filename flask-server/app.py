from flask import Flask, jsonify, request
import jsonpickle

from decorators.auth_decorators import requires_authorization
from services.auth_service import AuthService
from services.db_service import DBService

app = Flask(__name__)

# Mock data for demonstration purposes
users = {1: {"id": 1, "name": "John Doe", "email": "john.doe@example.com"}}

forms = {
    1: {"formId": 1, "title": "Form 1", "description": "This is form 1"},
    2: {"formId": 2, "title": "Form 2", "description": "This is form 2"},
}


@app.route("/api/v1/login", methods=["GET"])
def login():
    AuthService().login()
    return jsonify({"message": "Login successful"}), 200


@app.route("/api/v1/logout", methods=["GET"])
@requires_authorization
def logout():
    AuthService().logout()
    return jsonify({"message": "Logout successful"}), 200


@app.route("/api/v1/user", methods=["GET"])
@requires_authorization
def get_user_profile():
    # Assuming the current user is always user with id 1 for this example
    user_id = 1
    user = users.get(user_id)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/api/v1/form/<int:formId>", methods=["GET"])
def get_form(formId):
    form = forms.get(formId)
    if form:
        return jsonify(form), 200
    else:
        return jsonify({"error": "Form not found"}), 404


if __name__ == "__main__":
    dbService = DBService()
    dbService.create_table()
    dbService.add_person()

    # dbService.add_user("Jane Doe", "jdoe@email.com")

    # form_data: FormJsonModel = FormJsonModel(
    #     name="sheedy",
    #     email="sheedy@email.com",
    #     address=FormAddressModel(address1="123 Main St", address2="Apt 101"),
    # )

    # new_document = AttachedDocumentModel(
    #     document_url="s3url", document_name="doc1", document_type=DocumentType.PASSPORT
    # )

    # form_data.add_document(new_document)
    # # docId = new_document.id
    # # form_data.remove_document(docId)

    # dbService.add_form(user_id=1, form_body=jsonpickle.dumps(form_data))
    # formObj = dbService.get_form(2)
    # print(formObj)
    # app.run(debug=True)
