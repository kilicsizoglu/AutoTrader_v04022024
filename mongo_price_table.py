from datetime import datetime

from mongoengine import Document, StringField, DateTimeField, FloatField


class CryptoPriceClass(Document):
    symbol = StringField(required=True, max_length=50)
    time = DateTimeField(default=datetime.utcnow)
    price = FloatField()
    volume = FloatField()
    predict_price = FloatField()
    macd = FloatField()
    signal = FloatField()
    yukselis_dusus = FloatField()
    rsi = FloatField()
    stochk = FloatField()
    stochd = FloatField()
    stochrsik = FloatField()
    stochrsid = FloatField()