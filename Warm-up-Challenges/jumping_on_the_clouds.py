def jumpingOnClouds(c):
    jumps = 0
    position = 0
    while position < len(c)-1:
        if position+2 < len(c) and c[position + 2] == 0:
            jumps += 1
            position += 2
        elif position+1 < len(c) and c[position + 1] == 0:
            jumps += 1
            position += 1

    return jumps

import unittest
class jumpingOnCloudsTesting(unittest.TestCase):
    def test_jumpingOnClouds_1(self):
        matching = 4
        self.assertEqual(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]), matching)

    def test_jumpingOnClouds_2(self):
        matching = 3
        self.assertEqual(jumpingOnClouds([0, 0, 0, 0, 1, 0]), matching)

    def test_jumpingOnClouds_3(self):
        matching = 3
        self.assertEqual(jumpingOnClouds([0, 0, 0, 1, 0, 0]), matching)
if __name__ == '__main__':
    unittest.main()