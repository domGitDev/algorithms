

def permutation_check(elements):
       
    def validate():
        if not isinstance(elements, (tuple, list)):
            raise TypeError(
                'Expected list or tuple, got %s.' % type(elements))
        
        length = len(elements)     
        if not length: 
            return False
        
        if length >= 1000000:
            raise ValueError(
                'Array length not in range [1 : 1000000]')
               
        elements[:] = sorted(elements)
        if elements[0] < 1 or elements[-1] >= 1000000000:
            raise ValueError(
                'Array values not in range [1 : 1000000000]')
        return True

    def ispermutation():
        for i, val in enumerate(elements, 1):
            if i != val:
                return False
        return True

    valid = validate()    
    if not valid or not ispermutation():
        return False
    return True
       

 
