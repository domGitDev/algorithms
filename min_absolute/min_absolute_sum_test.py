import unittest
from min_absolute_sum import min_abs_sum


class MinAbsSumTest(unittest.TestCase):
    
    def test_min_abs_sum(self):
        data = [-6, 6, 6, 4, 2, 1, -2, 6]
        self.assertEqual((1, [1, 1, 1, 1, -1, -1, 1, -1]), min_abs_sum(data))
    
        data = [1, 4, 1, -1, 1, -5]
        self.assertEqual((1, [1, 1, 1, 1, 1, 1]), min_abs_sum(data))
        
        data = [1, 5, 2, -2]        
        self.assertEqual((0, [-1, 1, -1, 1]), min_abs_sum(data))
        
        data = [1,1,3,3,3,3,3,5]
        self.assertEqual((0, [-1, -1, -1, 1, 1, 1, -1, 1]), min_abs_sum(data))
        
    def test_min_abs_sum_bad_type(self):
        with self.assertRaises(TypeError):
            min_abs_sum('ghdhhf')
        
        with self.assertRaises(TypeError):
            min_abs_sum(x for x in xrange(20))
            
    def test_min_abs_sum_bad_values(self):
        with self.assertRaises(ValueError):
            min_abs_sum([-200, 1])
            
        with self.assertRaises(ValueError):
            min_abs_sum([x for x in xrange(21000)])       


suite = unittest.TestLoader().loadTestsFromTestCase(MinAbsSumTest)
unittest.TextTestRunner(verbosity=2).run(suite)
        
