from mongokit import *
import cfg, datetime
connection = Connection(cfg.MONGODB_HOST, cfg.MONGODB_PORT)

@connection.register
class Food(Document):
    __database__ = 'masseyhacks3'
    __collection__ = 'food'
    structure = {
        'name': unicode,
        'UPC': unicode,
        'expiry': datetime.date,
    }
    required_fields = ['name']

def test():
    food = connection.Food()
    food['name'] = u'Fried chicken'
    food['UPC'] = u'123456789012'
    food['expiry'] = datetime.date(2017, 5, 1)
