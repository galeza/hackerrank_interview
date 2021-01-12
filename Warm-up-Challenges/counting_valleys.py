def countingValleys(steps, path):
    counter_valley = 0
    level = 0
    for x in range(0,steps):
        if path[x] == "U":
            level +=1
            if level==0:
                counter_valley+=1
        else:
            level-=1
    return counter_valley

import unittest


class countingValleysTesting(unittest.TestCase):
    def test_valley_1(self):
        matching = 1
        self.assertEqual(countingValleys(8, "UDDDUDUU"), matching)

    def test_valley_2(self):
        matching = 2
        self.assertEqual(countingValleys(12, "DDUUDDUDUUUD"), matching)

if __name__ == '__main__':
    unittest.main()
