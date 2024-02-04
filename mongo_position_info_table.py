from datetime import datetime

from mongoengine import Document, StringField, DateTimeField, FloatField


class CryptoPositionInfoClass(Document):
    symbol = StringField(required=True, max_length=50)
    type = StringField(required=True, max_length=50)
    price = FloatField()
    price_sb = FloatField()
    earning = FloatField()
    earning_status = StringField(required=True, max_length=50)