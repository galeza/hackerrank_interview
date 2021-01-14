def rotLeft(a, d):
    return a[d:] + a[:d]


import unittest


class rotLeftTesting(unittest.TestCase):
    def test_rotLeft_1(self):
        matching = [5, 1, 2, 3, 4]
        self.assertEqual(rotLeft([1, 2, 3, 4, 5], 4), matching)

    def test_rotLeft_2(self):
        matching = [41, 73, 89, 7, 10, 1, 59, 58, 84, 77, 77, 97, 58, 1, 86, 58, 26, 10, 86, 51]
        self.assertEqual(rotLeft([77, 97, 58, 1, 86, 58, 26, 10, 86, 51, 41, 73, 89, 7, 10, 1, 59, 58, 84, 77], 10),
                         matching)

    def test_rotLeft_3(self):
        matching = [87, 97, 33, 47, 70, 37, 8, 53, 13, 93, 71, 72, 51, 100, 60]
        self.assertEqual(rotLeft([33, 47, 70, 37, 8, 53, 13, 93, 71, 72, 51, 100, 60, 87, 97], 13), matching)


if __name__ == '__main__':
    unittest.main()
