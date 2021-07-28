# Challenge Link: https://discuss.codecademy.com/t/extreme-tolerant-string-matching-python-challenge-not-for-beginners/583300

from basic import *
from intermediate import *
from hard import *
from extreme import *
from bonus import *

import unittest

class TolerantStringMatchingTest(unittest.TestCase):

    def test_basicChallenge_true_1(self):
        self.assertTrue(basicMatch("Codecademy taught me to code", "code"))

    def test_basicChallenge_true_2(self):
        self.assertTrue(basicMatch("A really long string", "on"))

    def test_basicChallenge_true_3(self):
        self.assertTrue(basicMatch("CaseInsEnSiTiVE", "caseinsensitive"))


    def test_basicChallenge_false_1(self):
        self.assertFalse(basicMatch("Welcome to the internet", "hello"))




    def test_intermediateChallenge_true_1(self):
        self.assertTrue(intermediateMatch("Codecademy is great", "codecademy", []))

    def test_intermediateChallenge_true_2(self):
        self.assertTrue(intermediateMatch("Codec%65demy is great", "codecademy", [["%65", "A"]]))
        
    def test_intermediateChallenge_true_3(self):
        self.assertTrue(intermediateMatch("Codec%65demy is great", "codec%65demy", [["%65", "A"]]))
        
    def test_intermediateChallenge_true_4(self):
        self.assertTrue(intermediateMatch("Codec%65demy is great", "codecademy", [["%65", "A"], ["%67", "D"]]))
        
    def test_intermediateChallenge_true_5(self):
        self.assertTrue(intermediateMatch("Co%67ec%65demy is great", "codec%65demy", [["%65", "A"], ["%67", "D"]]))
        
    def test_intermediateChallenge_true_6(self):
        self.assertTrue(intermediateMatch("Co%67eca%68emy is great", "codecademy", [["%67", "D"], ["%68", "D"]]))

    def test_intermediateChallenge_true_7(self):
        self.assertTrue(intermediateMatch("Co%67eca%67emy is great", "co%67ecademy", [ ["%67", "D"]]))
        
    def test_intermediateChallenge_true_8(self):
        self.assertTrue(intermediateMatch("Co%67eca%67emy is goo%67", "codeca%67emy is good", [["%67", "D"]]))


    def test_intermediateChallenge_false_1(self):
        self.assertFalse(intermediateMatch("abc%6efg", "abcdefg", [["e", "d"], ["%6", "e"]]))
        
    def test_intermediateChallenge_false_2(self):
        self.assertFalse(intermediateMatch("Codecademy is great", "codec%65demy", [["%65", "A"]]))




    def test_hardChallenge_true_1(self):
        self.assertTrue(hardMatch("Codecademy is great", "codecademy", []))
        
    def test_hardChallenge_true_2(self):
        self.assertTrue(hardMatch("Codec%65demy is great", "codecademy", [["%65", "A"]]))
        
    def test_hardChallenge_true_3(self):
        self.assertTrue(hardMatch("Codec%65demy is great", "codecademy", [["%65", "$"], ["$", "A"]]))
        
    def test_hardChallenge_true_4(self):
        self.assertTrue(hardMatch("abc%6efg", "abcdefg", [["e", "d"], ["%6", "e"]]))
        
    def test_hardChallenge_true_5(self):
        self.assertTrue(hardMatch("Co$ec%65E$$$ is great", "codecadem$", [["%65", "$"], ["$", "m"], ["$", "E"], ["E", "D"], ["D", "A"]]))

    def test_hardChallenge_true_6(self):
        self.assertTrue(hardMatch("Codec%65demy is great", "codecademy", [["%65", "$"], ["$", "D"], ["D", "A"]]))


    def test_hardChallenge_false_1(self):
        self.assertFalse(hardMatch("Codec%65demy is great", "codecademy", [["%65", "$10"], ["$10", "B"]]))




    def test_extremeChallenge_true_1(self):
        self.assertTrue(extremeMatch("$1cademy is great", "codecademy", [["$2", "co"], ["$1", "code"]]))
              
    def test_extremeChallenge_true_3(self):
        self.assertTrue(extremeMatch("%1 is great", "codecademy", [["%1", "codecademy"], ["%68", "D"]]))
        
    def test_extremeChallenge_true_4(self):
        self.assertTrue(extremeMatch("%1 is great", "codecademy", [["%1", "codecademy"], ["codecademy", "%2"], ["%2", "%1"]]))

    def test_extremeChallenge_true_5(self):
        self.assertTrue(extremeMatch("abcd%6fg", "abc%6efg", [["%6", "d"], ["d", "e"], ["e", "%6"]]))

    def test_extremeChallenge_true_6(self):
        self.assertTrue(extremeMatch("dbcd%6fg", "abc%6efg", [["%6", "d"], ["d", "e"], ["e", "%6"], ["d", "a"]]))

    def test_extremeChallenge_true_7(self):
        self.assertTrue(extremeMatch("%1 is great", "code", [["%1", "code"], ["co", "d"], ["d", "code"], ["code", "%1"]]))

    def test_extremeChallenge_true_8(self):
        self.assertTrue(extremeMatch("%10 is great", "codecademy", [["%1", "random"], ["%10", "codecademy"]]))

    def test_extremeChallenge_true_10(self):
        self.assertTrue(extremeMatch("code", "codecademy", [["c", "codecademy"]]))

    def test_extremeChallenge_true_11(self):
        self.assertTrue(extremeMatch("%1 is great", "code", [["%1", "codecademy"], ["%68", "D"]]))
        

    def test_extremeChallenge_false_1(self):
        self.assertFalse(extremeMatch("%1 is great", "code", [["%1", "co"], ["%68", "D"]]))
        
    def test_extremeChallenge_false_2(self):
        self.assertFalse(extremeMatch("%1 is great", "code", [["%1", "co"], ["co", "d"], ["d", "%1"]]))

    def test_extremeChallenge_false_3(self):
        self.assertFalse(extremeMatch("abcd%6fg", "%6bc%6efg", [["%6", "d"], ["d", "e"], ["e", "%6"], ["d", "a"]]))




    def test_bonusChallenge_true_1(self):
        self.assertEqual(bonusMatch("Codecademy is great", "codecademy", []), (True, (0, 10)))
        
    def test_bonusChallenge_true_2(self):
        self.assertEqual(bonusMatch("Codec%65demy is great", "codecademy", [["%65", "A"]]), (True, (0, 12)))
        
    def test_bonusChallenge_true_3(self):
        self.assertEqual(bonusMatch("Codec%65demy is great", "codecademy", [["%65", "$10"], ["$10", "A"]]), (True, (0, 12)))
        
    def test_bonusChallenge_true_4(self):
        self.assertEqual(bonusMatch("Co%67ecademy teaches me to code", "code", [["%67", "d"], ["d", "a"]]), (True, (0, 6)))
        

    def test_bonusChallenge_false_1(self):
        self.assertEqual(bonusMatch("Codec%65demy is great", "codecademy", [["%65", "$10"], ["$10", "B"]]), (False, None))




    # Not handling these yet.
    # def test_superExtremeChallenge_true_1(self):
    #     self.assertTrue(extremeMatch("$1 is great", "codecademy", [["$1", "code$2"], ["$2", "$3emy"], ["$3", "cad"]]))

    # def test_superExtremeChallenge_true_2(self):
    #     self.assertTrue(extremeMatch("$1 is great", "codecademy", [["$1", "code$2"], ["$2", "$3"], ["$3", "cad$3"], ["$3", "emy"]]))

    # def test_superExtremeChallenge_true_3(self):
    #     self.assertTrue(extremeMatch("$2decademy is great", "codecademy", [["$1", "code"], ["$2", "co"]]))
  
    # def test_superExtremeChallenge_true_4(self):
    #     self.assertTrue(extremeMatch("$1 is great", "codecademy", [["$1", "code$2"], ["$2", "cademy"]]))

    # def test_superExtremeChallenge_true_5(self):
    #     self.assertTrue(extremeMatch("$1 is great", "codecademy", [["$1", "code$2"], ["$2", "$3emy"], ["$3", "$4"], ["$4", "$2"], ["$2", "cad"]]))

    # def test_superExtremeChallenge_true_6(self):
    #     self.assertTrue(extremeMatch("1", "aaaaaaaa", [["1", "a"], ["a", "11"]]))

    # def test_superExtremeChallenge_true_7(self):
    #     self.assertTrue(extremeMatch("1", "aa1aa11aa", [["1", "a"], ["a", "11"]]))

    # def test_superExtremeChallenge_true_8(self):
    #     self.assertTrue(extremeMatch("code", "codecodecodecodecodecademy", [["code", "codecode"], ["code", "cademy"]]))




    # def test_lookBackExtremeChallenge_true_1(self):
    #     self.assertTrue(extremeMatch("%%656", "code", [["%65", "6"], ["%66", "code"]]))

    # def test_lookBackExtremeChallenge_true_2(self):
    #     self.assertTrue(extremeMatch("$%6%6%6%6%6%65", "code", [["%65", "5"], ["$%65", "code"]]))




unittest.main(exit = False)
