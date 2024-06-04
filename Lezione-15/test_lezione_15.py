import unittest
from lezione_9_anagram import anagram

class UnittestAnagram(unittest.TestCase):
    def test_anagram(self):
        reader = open('Lezione-15/test.txt')
        s = reader.readline()
        t = reader.readline()
        reader.close()
        self.assertTrue(anagram(s, t))



if __name__ == "__main__":
    unittest.main()