
def count_unpaired(elements):
                   
    def validate():   
        if not isinstance(elements, (list, tuple)):
            raise TypeError(
                'Expect list or tuple, got %s' % type(elements))
                
        num_elements = len(elements)    
        if num_elements < 1 or num_elements > 1000000:
            raise ValueError(
                'Array size out of range[1; 1,000,000]. num elements %s' 
                % num_elements)  
        if num_elements % 2 == 0:
            raise ValueError(
                'Expected odd numbers of elements, got %d' % num_elements)
                
        # sort list to get max and min values to check if is within range
        # is faster than checking repetitive inside a loop         
        values = sorted(elements)
        if num_elements:
            if values[0] < 1 or values[-1] > 1000000000:
                raise ValueError(
                    'Value out of range[1; 1,000,000,000]') 
                
        return values, num_elements
    
                   
    values, num_elements = validate()
    if num_elements == 1:
        return values[0]
        
    unpaired = []
    for item in values:    
        if item in unpaired:
            unpaired.remove(item)
        else:
            unpaired.append(item)
            
    return unpaired[0]  
    
        
               
    
    
        