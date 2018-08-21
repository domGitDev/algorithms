
def rotate(A, K):  
          
    def validate():
        if not isinstance(A, (list, tuple)) or not isinstance(K, int):
            raise TypeError(
                'Expected list or tuple and int, got %s and %s' 
                % (type(A), type(K)))
                
        length = len(A)
        if length < 0 or length > 100 or K < 0 or K > 100:
            raise ValueError(
                'Array length or roation value K not in [1, 100]')
                
        values = sorted(A)
        if length:
            if values[0] < -1000 and values[-1] > 1000:
                raise ValueError(
                    'Array value not in range [-1000, 1000]')
        return length

                    
    length = validate()
    if not length or length == 1: 
        return A
    
    if K >= length:
        invert = K / length
        if invert % 2 != 0 or invert == 1:
            A[::-1]
        K %= length
                    
    temp = A[-K:]
    return temp + A[:-K]
