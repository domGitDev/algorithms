
import unittest
from permut_check import permutation_check

class PermuteCheckTest(unittest.TestCase):
    def test_permutation_check(self):   
        data = [1, 2, 3, 4, 5, 6]    
        self.assertEqual(True, permutation_check(data))
                
        data = [10, 3, 5, 4, 7, 6, 8, 9]
        self.assertEqual(False, permutation_check(data))
                
        data = [x for x in xrange(1, 1000000)]
        self.assertEqual(True, permutation_check(data))
        
    def test_permutation_check_bad_values(self):
        with self.assertRaises(ValueError):
            data = [1, 0, 3, 4, 5, 6] 
            permutation_check(data)
            
        with self.assertRaises(ValueError):
            data = [-1] 
            permutation_check(data)
            
        with self.assertRaises(ValueError):
            data = [1, 2000000000]
            permutation_check(data)
        
    def test_permutation_check_bad_types(self):
        with self.assertRaises(TypeError):
            permutation_check(None)
            
        with self.assertRaises(TypeError):
            permutation_check(1000)
            
        with self.assertRaises(TypeError):
            permutation_check(x for x in xrange(1, 10))            
            
        
   
suite = unittest.TestLoader().loadTestsFromTestCase(PermuteCheckTest)
unittest.TextTestRunner(verbosity=2).run(suite) 


