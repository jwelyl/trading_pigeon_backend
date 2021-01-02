import os


class BaseConfig(object):
    SERVICE_NAME = "tradingpigeon"
    SECRET_KEY = os.getenv("APP_SECRET_KEY")
    EMAIL_ID = os.getenv("EMAIL_ID")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    REQUEST_ID_UNIQUE_VALUE_PREFIX = "API"


class LocalConfig(BaseConfig):
    pass


class ProductionConfig(BaseConfig):
    pass