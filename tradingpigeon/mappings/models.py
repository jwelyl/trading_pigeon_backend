import enum
from sqlalchemy.ext.declarative import declared_attr
from inflection import underscore
from tradingpigeon.extension import db


class TradingType(enum.IntEnum):
    """
    상장된 주식의 타입입니다.
    Type of trading.
    """

    KOSPI = 0
    KOSDAQ = 1
    NASDAQ = 2
    SNP = 3


class BaseModel(object):
    """
    Base Model입니다.
    Base of Model.
    """

    default_table_args = {"mysql_charset": "utf8mb4"}

    __table_args__ = default_table_args

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    @declared_attr
    def __tblename__(cls) -> str:
        return underscore(cls.__name__)

    def __eq__(self, o: object) -> bool:
        if self.id is None or o is None:
            return False
        return self.id == o.id


class TradingCode(BaseModel, db.Model):
    """
    주식 코드의 모델입니다.
    Model of trading code.
    """

    code = db.Column(db.String(255), nullable=False)
    trading_type = db.Column(db.Enum(TradingType), default=0, index=True)
