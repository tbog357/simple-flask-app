from flask import request, Blueprint
from api.customer.customer import Customer

# Local import
from api.main.core.request_handler import handle_request

customer_blueprint = Blueprint(
    name="customer",
    import_name=__name__,
)


@customer_blueprint.route("/create")
@handle_request
def create_customer():
    customer_data = request.get_json()
    customer = Customer(**customer_data)
    return customer.create()


@customer_blueprint.route("/read")
@handle_request
def read_customer():
    customer_data = request.get_json()
    customer = Customer(**customer_data)
    return customer.read()


@customer_blueprint.route("/update")
@handle_request
def update_cusomter():
    customer_data = request.get_json()
    customer = Customer(**customer_data)
    return customer.update()


@customer_blueprint.route("/delete")
@handle_request
def delete_customer():
    customer_data = request.get_json()
    customer = Customer(**customer_data)
    return customer.delete()
