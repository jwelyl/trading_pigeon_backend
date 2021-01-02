from flask import Flask, request
from flask_request_id_header.middleware import RequestID

from tradingpigeon import app
from tradingpigeon.service.mail_service import MailService

CONFIG_NAME_MAPPER = {
    "local": "config.LocalConfig",
    "production": "config.ProductionConfig",
}


def create_app(flask_config: str = "local") -> Flask:
    app.config.from_object(CONFIG_NAME_MAPPER[flask_config])
    RequestID(app)
    return app


@app.route("/", methods=["GET"])
def hello_world():
    print(app.config["EMAIL_ID"])
    return "Hello, World!"


@app.route("/api/mail/naver", methods=["POST"])
def mail_test():
    mail_service = MailService()

    request_json = request.get_json()
    response = mail_service.send_mail_by_default(
        request_json["toMail"], request_json["subject"], request_json["text"]
    )

    return response