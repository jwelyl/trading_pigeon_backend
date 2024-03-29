import os
from flask import Flask
from tradingpigeon.main import create_app

try:
    config = os.environ["FLASK_CONFIG"]
except KeyError:
    config = "local"

app: Flask = create_app(flask_config=config)
print(f" * App Mode : {config}")

from tradingpigeon.extension import db
from tradingpigeon.mappings import models

with app.app_context():
    db.create_all()
    db.session.commit()
