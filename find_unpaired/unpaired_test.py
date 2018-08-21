import unittest
from unpaired import count_unpaired

class UnpairedTestCase(unittest.TestCase): 
    def test_count_unpaired(self):
        data = [9, 3, 9, 3, 9, 7, 9] 
        self.assertEqual(7, count_unpaired(data))
        
        data = [3, 5, 2, 2, 5, 5, 3, 5, 2, 3, 1]
        self.assertEqual(1, count_unpaired(data))
        
    def test_count_unpaired_single(self):
        data = [9] 
        self.assertEqual(9, count_unpaired(data))   
    
    def test_count_unpaired_bad_type(self): 
        with self.assertRaises(TypeError):
            count_unpaired(12)
            
        with self.assertRaises(TypeError):
            count_unpaired(None)
            
        with self.assertRaises(TypeError):
            count_unpaired(0.1)
            
        
    def test_count_unpaired_bad_values(self): 
        with self.assertRaises(ValueError):
            data = []
            count_unpaired(data)
            
        with self.assertRaises(ValueError):
            data = [1, 2]
            count_unpaired(data)    
            
        with self.assertRaises(ValueError):
            data = [-1, 1000000001]
            count_unpaired(data)
              
        with self.assertRaises(ValueError):
            data = [i for i in range(0, 1000000000, 10000)]
            count_unpaired(data)       

    
suite = unittest.TestLoader().loadTestsFromTestCase(UnpairedTestCase)
unittest.TextTestRunner(verbosity=2).run(suite)
