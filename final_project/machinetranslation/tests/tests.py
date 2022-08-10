import unittest
from translator import english_to_french, french_to_english

class test_english_to_french(unittest.TestCase):
    def test_english_to_french(self): 
        self.assertEqual(english_to_french("Hello"), "Bonjour") # test when hello given as input the output is Bonjour.
        self.assertEqual(english_to_french(0), '0')  # test for null
        
        
class test_french_to_english(unittest.TestCase): 
    def test_french_to_english(self): 
        self.assertEqual(french_to_english("Bonjour"), "Hello") # test when Bonjour given as input the output is Hello.
        self.assertEqual(french_to_english(0), '0')  # test for null

unittest.main()
