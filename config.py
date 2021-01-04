import os


class BaseConfig(object):
    """
    flask app의 config의 base class입니다.
    base class of flask app's config
    """

    SERVICE_NAME = "tradingpigeon"
    SECRET_KEY = os.getenv("APP_SECRET_KEY")
    EMAIL_ID = os.getenv("EMAIL_ID")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
    NAVER_EMAIL_SMTP_URL = "smtp.naver.com"
    NAVER_EMAIL_SMTP_PORT = 587
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    REQUEST_ID_UNIQUE_VALUE_PREFIX = "API"
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(PROJECT_ROOT, "example.db")}?check_same_thread=False'


class LocalConfig(BaseConfig):
    """
    local에서 flask app의 config입니다.
    flask app's config in local
    """

    pass


class ProductionConfig(BaseConfig):
    """
    production에서 flask app의 config입니다.
    flask app's config in production
    """

    pass