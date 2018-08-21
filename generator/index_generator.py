
class IndexGenerator(object):
    
    def __init__(self, indexes, max_index):
        self.indexes = indexes
        self.max_index = max_index
    
    @staticmethod    
    def _validate_list(indexes):
        if not isinstance(indexes, (tuple, list)):
            raise TypeError(
                'Expected list or tuple, got %s' % type(indexes))      
        if not indexes: return indexes

        others = [x for x in indexes if not isinstance(x, int)] 
        if others:
            raise ValueError('Not integer: %s' % others)     
        values = sorted(indexes)
        if values[0] < 0:
            raise ValueError(
                'Given array contains negative value for index')
        return values
    
    @staticmethod    
    def _validate_integer(max_index):
        if not isinstance(max_index, int):
            raise TypeError(
                'Expected integer, got %s' % type(max_index))
        if max_index < 0:
            raise ValueError('Given value for Max Index is negative')
        return max_index
    
    @property
    def max_index(self):
        return self._max_index
    
    @max_index.setter
    def max_index(self, max_index):       
        self._max_index = self._validate_integer(max_index)              
    
    @property    
    def indexes(self):
        return self._indexes
    
    @indexes.setter
    def indexes(self, indexes):
        self._indexes = self._validate_list(indexes) 
        
    def __iter__(self):
        while True:
            self._max_index += 1
            if self._max_index < self._indexes[-1]:
                self._max_index = self._indexes[-1] + 1
            yield self._max_index
            
    def next(self):
        return next(self.__iter__())    
    



    



