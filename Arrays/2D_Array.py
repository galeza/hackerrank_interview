def hourglassSum(arr):
    max_sum = -63
    for x in range(len(arr) - 2):
        for y in range(len(arr[x]) - 2):
            tem_sum = arr[x][y] + arr[x][y + 1] + arr[x][y + 2] + arr[x + 1][y + 1] + arr[x + 2][y] + arr[x + 2][
                y + 1] + arr[x + 2][y + 2]
            if tem_sum > max_sum:
                max_sum = tem_sum
    return max_sum


import unittest


class hourglassSumTesting(unittest.TestCase):
    def test_hourglassSum_1(self):
        matching = 19
        self.assertEqual(hourglassSum([[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0],
                                       [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]), matching)

    def test_hourglassSum_2(self):
        matching = 28
        self.assertEqual(
            hourglassSum([[-9, -9, -9, 1, 1, 1], [0, -9, 0, 4, 3, 2], [-9, -9, -9, 1, 2, 3], [0, 0, 8, 6, 6, 0],
                          [0, 0, 0, -2, 0, 0], [0, 0, 1, 2, 4, 0]]), matching)

    def test_hourglassSum_3(self):
        matching = -6
        self.assertEqual(
            hourglassSum(
                [[-1, -1, 0, -9, -2, -2], [-2, -1, -6, -8, -2, -5], [-1, -1, -1, -2, -3, -4], [-1, -9, -2, -4, -4, -5],
                 [-7, -3, -3, -2, -9, -9], [-1, -3, -1, -2, -4, -5]]), matching)


if __name__ == '__main__':
    unittest.main()

