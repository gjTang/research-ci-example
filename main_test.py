import unittest
import main


class MainTest(unittest.TestCase):
    def test_hw(self):
        ret = main.helloworld('Test')
        self.assertEqual(ret, 'Hello World! Test')

if __name__ == '__main__':
    unittest.main()