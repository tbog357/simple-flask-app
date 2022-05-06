from flask import Flask

# local import
from api.endpoint.routes import routes
from api.main.core.request_handler import handle_request

app = Flask(__name__)


@app.route("/", methods=["GET"])
@handle_request
def app_info():
    return {"app_info": "Simple Flask Application"}


@app.errorhandler(404)
@handle_request
def api_not_found(e):
    return {"error_message": "API not found"}


# Add routes
for blueprint, url_prefix in routes:
    app.register_blueprint(
        blueprint=blueprint,
        url_prefix=url_prefix,
    )

if __name__ == "__main__":
    app.run()
