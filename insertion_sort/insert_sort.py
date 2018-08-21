import functools


def validate(func):
    @functools.wraps(func)    
    def wrapper(*args, **kwargs):
        if 'data' in kwargs:
            if not isinstance(kwargs['data'], (tuple, list, set)):
                raise TypeError(
                    'Expected list or tuple, got %s.' % type(kwargs['data']))
            kwargs['data'] = list(kwargs['data'])
        return func(*args, **kwargs) 
    return wrapper
    

@validate
def insert_sort(data):
    """ Insert Sort algorithm 
        param data: list, tuple or set
        return: ascendent ordered list
    """
    def insert(data, rindex, value):
        for i in xrange(rindex, -2, -1):
            if value > data[i]:
                break
            data[i+1] = data[i]
        data[i+1] = value
        return data
        
    if not data:
        return []
    
    length = len(data)
    for i in xrange(length-1):
        insert(data, rindex=i, value=data[i+1])
        
    return data



