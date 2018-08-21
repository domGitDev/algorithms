import unittest
from index_generator import IndexGenerator

class IndexGeneratorTest(unittest.TestCase):
    
    def test_index_gen(self):
        data = [x for x in range(5)]
        it = IndexGenerator(data, 4)
        self.assertEqual([5, 6, 7, 8], [it.next() for i in range(4)])

    def test_index_gen_bad_value(self): 
        with self.assertRaises(ValueError):       
            data = [-x if x < 4 else x for x in range(1, 9)]
            it = IndexGenerator(data, 1)
            
        with self.assertRaises(ValueError):
            data = []
            it = IndexGenerator(data, -1) 
            
    def test_index_gen_bad_type(self):
        with self.assertRaises(TypeError):
            IndexGenerator(None, 1)
            
        with self.assertRaises(TypeError):
            IndexGenerator('fggfgd', 4)
            
        with self.assertRaises(TypeError):
            IndexGenerator(set([1, 4, 5]))
            
        with self.assertRaises(TypeError):
            IndexGenerator([1, 'g', None, 1.6, 4, 5])
                

suite = unittest.TestLoader().loadTestsFromTestCase(IndexGeneratorTest)
unittest.TextTestRunner(verbosity=2).run(suite)


