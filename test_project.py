import unittest
from src.lib import translate_word

class TestDictionary(unittest.TestCase):
	def test_translate_ENG_Arr_Single_definition(self):
		#If an English word only has 1 Arrernte Word
		word = "a"
		translation = get_word_translation("eng", word)
		self.assertEqual(translation, "anyente")
	
	def test_translat_ENG_ARR_Multiple_definition(Self):
		#If an English word has multiple Arrernte Words
		word = "ache"
		translation = get_word_translation("eng", word)
		self.assertEqual(translation, ["arnteme","kwarneme","arlkweme"])


if __name__ == '__main__':
    unittest.main()
