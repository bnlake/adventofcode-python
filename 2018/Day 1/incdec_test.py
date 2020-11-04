import unittest

inc_dec = __import__('2018/Day 1/inc_dec')


class Test_TestIncrementDecrement(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(inc_dec.increment(2), 3)

    def test_decrement(self):
        self.assertEqual(inc_dec.decrement(2), 1)


if __name__ == '__main__':
    unittest.main()
