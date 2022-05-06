from flask import Flask
from api.endpoint.routes import routes

app = Flask(__name__)


@app.route("/")
def app_info():
    return "Simple customer application"


for blueprint, url_prefix in routes:
    app.register_blueprint(
        blueprint=blueprint,
        url_prefix=url_prefix,
    )

if __name__ == "__main__":
    app.run()
