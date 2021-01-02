import os


class BaseConfig(object):
    SERVICE_NAME = "tradingpigeon"
    SECRET_KEY = "Lp9tyDzUIzUfAX2ZP9qYwoRTRtZuGeSj"
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    REQUEST_ID_UNIQUE_VALUE_PREFIX = "API"


class LocalConfig(BaseConfig):
    pass


class ProductionConfig(BaseConfig):
    pass