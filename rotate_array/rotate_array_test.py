import unittest
from rotate_array import rotate

class RotateTestCase(unittest.TestCase): 
    def test_rotate(self):
        data = [4, 3, 9, 8, 5, 7, 9] 
        output = [8, 5, 7, 9, 4, 3, 9]
        self.assertEqual(output, rotate(data, 4))
        
        data = [3, 8, 9, 7, 6]
        output = [9, 7, 6, 3, 8]
        self.assertEqual(output, rotate(data, 3))
        
    def test_rotate_empty(self):
        self.assertEqual([], rotate([], 1))  
        
    def test_rotate_single(self):
        self.assertEqual([7], rotate([7], 5)) 
            
    def test_rotate_bad_values(self):
        with self.assertRaises(ValueError):
            data = [x for x in range(1, 120)]
            rotate(data, 3)
            
        with self.assertRaises(ValueError):       
            data = [x for x in range(-2000, 2000, 100)]
            rotate(data, 3)
          
    def test_rotate_bad_types(self):
        with self.assertRaises(TypeError):
            rotate(None, 2)
        
        with self.assertRaises(TypeError):
            rotate(100, None)
               

suite = unittest.TestLoader().loadTestsFromTestCase(RotateTestCase)
unittest.TextTestRunner(verbosity=2).run(suite)
