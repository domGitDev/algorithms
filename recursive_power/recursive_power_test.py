import unittest
from recursive_power import power


class PowerTest(unittest.TestCase):
    
    def test_power(self):
        self.assertEqual(power(3, 0), 1)
        
        self.assertEqual(power(3, 2), 9)
        
        self.assertEqual(power(3, -1), 1.0/3)
        
        self.assertEqual(power(-3, 2), 9)


suite = unittest.TestLoader().loadTestsFromTestCase(PowerTest)
unittest.TextTestRunner(verbosity=2).run(suite)
