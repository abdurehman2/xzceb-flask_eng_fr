import unittest
import sys
sys.path.insert(1, "/home/project/xzceb-flask_eng_fr/final_project/machinetranslation/")
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def testEnglishToFrench(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(english_to_french("Hello"), "Salut")

    def testFrenchToEnglish(self):
        self.assertEqual(french_to_english("Salut"), "Hi")
        self.assertNotEqual(english_to_french("Bonjour"), "Hi")

if __name__ == '__main__':
    unittest.main()
