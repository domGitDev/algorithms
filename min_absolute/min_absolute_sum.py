
def min_abs_sum(A):
    
    def validate():
        if not isinstance(A, (tuple, list)):
            raise TypeError('Expected tuple or list, got %s' % type(A))
        
        length = len(A)
        if length > 20000:
            return None, length
        values = sorted(A)
        if values[0] <= -100 or values[-1] >= 100:
            return None, length
        return values, length 
    
    max_val = 0    
    values, length = validate()
    if not values:
        return 0
    
    for i, val in enumerate(A):
        A[i] = abs(val)
        max_val = max(A[i], max_val)
        
    total = sum(A)
    count = [0] * (max_val+1)
    for i, val in enumerate(A):
        count[val] += 1
    
    dp = [-1] * (total+1)
    dp[0] = 0
    
    for a in xrange(1, max_val+1):
        if count > 0:
            for j in xrange(total):
                if dp[j] >= 0:
                    dp[j] = count[a]
                elif (j >= a and dp[j-a] > 0):
                    dp[j] = dp[j-a] - 1
                    
    res = total
    for i in xrange(total // 2 + 1):
        if dp[i] > 0:
            res = min(res, total - 2 * i)
            
    return res, dp
    
    
"""
data = [-6, 6, 6, 4, 2, 1, -2, 6]
print min_abs_sum(data)

data = [1, 5, -2, 2]
print min_abs_sum(data)

data = [1, 4, 1, -1, 1, -5]
print min_abs_sum(data)
"""






