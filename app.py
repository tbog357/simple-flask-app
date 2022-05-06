import logging
from flask import Flask

# local import
from api.main.core.logger import JsonLoggingFormatter

from api.endpoint.routes import routes
from api.main.core.request_handler import handle_request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def app_info():
    return {"app_info": "Simple Flask Application"}


@app.errorhandler(404)
def api_not_found(e):
    return {"error_message": "API not found"}


# Add routes
for blueprint, url_prefix in routes:
    app.register_blueprint(
        blueprint=blueprint,
        url_prefix=url_prefix,
    )

if __name__ == "__main__":
    loggingFileHandler = logging.FileHandler(filename="logs/app.log")
    loggingFileHandler.setFormatter(JsonLoggingFormatter())

    app_logger = logging.getLogger("app_logger")
    app_logger.setLevel(logging.INFO)
    app_logger.addHandler(loggingFileHandler)

    app.run()
