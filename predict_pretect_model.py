from datetime import datetime

from mongoengine import Document, StringField, DateTimeField, FloatField


class PredictProtectModel(Document):
    symbol = StringField(required=True, max_length=50)
    time = DateTimeField(default=datetime.utcnow)
    price = FloatField()
    volume = FloatField()
    second_price = FloatField()
    end_status = StringField()
    macd = FloatField()
    signal = FloatField()
    rsi = FloatField()