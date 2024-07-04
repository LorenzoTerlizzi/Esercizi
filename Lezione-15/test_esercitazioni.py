import unittest
from esercitazioni import longest_palindrome

class Test(unittest.TestCase):
    def setUp(self):
        self.s0 = "abccccdd"
        self.s1 = "gthyjyyhht"
        self.s2 = "abcabcabc"
        self.s3 = "girgh5yafd"
    def test_palindorme(self):
        self.assertEqual(longest_palindrome(self.s0), len(self.s0))
        self.assertEqual(longest_palindrome(self.s1), len(self.s0))
        self.assertEqual(longest_palindrome(self.s2), len(self.s0))
        self.assertEqual(longest_palindrome(self.s3), len(self.s0))



if __name__ == "__main__":
    unittest.main()