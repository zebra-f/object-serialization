import datetime


def to_json(data):

    if isinstance(data, bytes):
        return {
            '__class__': 'bytes',
            '__value__': list(data)
        }
    
    if isinstance(data, datetime.datetime):
        return {
            '__class__': 'datetime',
            '__value__': str(data)
        }

    raise TypeError(repr(data) + ' is not JSON serializable')


def from_json(data):

    if '__class__' in data: 

        if data['__class__'] == 'datetime':
            return datetime.datetime.strptime(data['__value__'], "%Y-%m-%d %H:%M:%S")

        if data['__class__'] == 'bytes':
            return bytes(data['__value__'])            
    
    return data