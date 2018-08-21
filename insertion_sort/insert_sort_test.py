import unittest
import random
from insert_sort import insert_sort


class InsertSortTest(unittest.TestCase):
    
    def test_insert_sort(self):
        data = [3, 5, 7, 11, 13, 2, 9, 6]
        output = [2, 3, 5, 6, 7, 9, 11, 13]
        self.assertEqual(output, insert_sort(data=data))
        
        data = tuple([22, 11, 99, 88, 9, 7, 42])
        output = [7, 9, 11, 22, 42, 88, 99]
        self.assertEqual(output, insert_sort(data=data))
        
    def test_insert_sort_large(self):
        data = set([random.randint(1, 1000) for i in range(1, 1000)])
        output = sorted(list(data))
        self.assertEqual(output, insert_sort(data=data))
        
    def test_insert_sort_empty(self):
        self.assertEqual([], insert_sort(data=[]))
        
    def test_insert_sort_type(self):
        with self.assertRaises(TypeError):
            insert_sort(data='zfsggf')
            
        with self.assertRaises(TypeError):
            insert_sort(data=(i for i in xrange(10)))


suite = unittest.TestLoader().loadTestsFromTestCase(InsertSortTest)
unittest.TextTestRunner(verbosity=2).run(suite)

