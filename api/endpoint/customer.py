from crypt import methods
from flask import request, Blueprint
from api.customer.customer import Customer

# Local import
from api.main.core.request_handler import handle_request
from api.model.model_customer import ModelCustomer

customer_blueprint = Blueprint(
    name="customer",
    import_name=__name__,
)


@customer_blueprint.route("/create", methods=["POST"])
@handle_request
def create_customer():
    customer_data = request.get_json()
    model_customer = ModelCustomer.__init_from_dict__(customer_data)
    customer = Customer(model_customer)
    return customer.create()


@customer_blueprint.route("/read", methods=["POST"])
@handle_request
def read_customer():
    customer_data = request.get_json()
    model_customer = ModelCustomer.__init_from_dict__(customer_data)
    customer = Customer(model_customer)
    return customer.read()


@customer_blueprint.route("/update", methods=["POST"])
@handle_request
def update_cusomter():
    customer_data = request.get_json()
    model_customer = ModelCustomer.__init_from_dict__(customer_data)
    customer = Customer(model_customer)
    return customer.update()


@customer_blueprint.route("/delete", methods=["POST"])
@handle_request
def delete_customer():
    customer_data = request.get_json()
    model_customer = ModelCustomer.__init_from_dict__(customer_data)
    customer = Customer(model_customer)
    return customer.delete()
