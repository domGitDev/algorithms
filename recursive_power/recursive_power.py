
def isEven(n):
    if n%2 == 0:
        return True
    return False


def power(base, exp):
    if exp == 0:
        return 1
    
    if exp < 0:
        return 1.0/power(base, -exp)
   
    if not isEven(exp):
        return power(base, exp-1) * base
    
    if isEven(exp):
        res = power(base, exp/2)
        return res * res
    
                   
