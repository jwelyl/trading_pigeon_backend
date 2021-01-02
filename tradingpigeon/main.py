from flask import Flask
from flask_request_id_header.middleware import RequestID

from tradingpigeon import app

CONFIG_NAME_MAPPER = {
    "local": "config.LocalConfig",
    "production": "config.ProductionConfig",
}


def create_app(flask_config: str = "local") -> Flask:
    app.config.from_object(CONFIG_NAME_MAPPER[flask_config])
    RequestID(app)
    return app


@app.route("/")
def hello_world():
    print(app.config["EMAIL_ID"])
    return "Hello, World!"
