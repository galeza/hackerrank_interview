def repeatedString(s, n):
    if len(s) == 1 and s[0] == 'a':
        return n
    a_in_string = s.count('a')
    quotient = n // len(s)
    remainder = n % len(s)
    counter_a = a_in_string * quotient
    for letter in s[:remainder]:
        if letter == 'a':
            counter_a += 1
    return counter_a


import unittest


class repeatedStringTesting(unittest.TestCase):
    def test_repeatedString_1(self):
        matching = 7
        self.assertEqual(repeatedString("aba", 10), matching)

    def test_repeatedString_2(self):
        matching = 1000000000000
        self.assertEqual(repeatedString("a", 1000000000000), matching)

    def test_repeatedString_3(self):
        matching = 588525
        self.assertEqual(repeatedString("aab", 882787), matching)

    def test_repeatedString_4(self):
        matching = 7
        self.assertEqual(repeatedString("aba", 11), matching)

    def test_repeatedString_5(self):
        matching = 41107102139
        self.assertEqual(repeatedString(
            "ojowrdcpavatfacuunxycyrmpbkvaxyrsgquwehhurnicgicmrpmgegftjszgvsgqavcrvdtsxlkxjpqtlnkjuyraknwxmnthfpt",
            685118368975), matching)

    def test_repeatedString_5(self):
        matching = 0
        self.assertEqual(repeatedString(
            "x",
            970770), matching)

if __name__ == '__main__':
    unittest.main()


