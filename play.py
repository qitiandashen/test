from plus import count
import unittest
class TestCount(unittest.TestCase):
    def setUp(self):
        print('test start')
    def test_add(self):
       j=count(2,6)
       self.assertEqual(j.add(),9)
    def tearDown(self):
        print('test end')
if __name__=='__main__':
    unittest.main()

