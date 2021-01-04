from inflection import camelize
from marshmallow import validate
from marshmallow_enum import EnumField
from tradingpigeon.extension import ma
from tradingpigeon.mappings import models


class BaseSchema(ma.SQLAlchemyAutoSchema):
    """
    Schema의 Base입니다.
    Base of Schema.
    """

    def on_bind_field(self, field_name, field_obj):
        """
        바인딩될 때 Camel Case와 Snake Case를 변환해줍니다.
        Converting between Camel Case and Snake Case when Binding.
        """
        field_obj.data_key = camelize(field_obj.data_key or field_name, False)


class TradingCodeSchema(BaseSchema):
    """
    TradingCode 모델의 Schema입니다.
    Schema of Trading Code model.
    """

    class Meta:
        model = models.TradingCode

    id = ma.auto_field(
        validate=validate.Range(min=1, error="Id must be bigger than 1")
    )
    code = ma.auto_field(validate=validate.Length(min=4, max=10))
    trading_type = EnumField(models.TradingType, data_key="tradingType")