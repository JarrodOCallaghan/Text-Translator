import unittest
import lib.translate_word as t
import lib.word
import lib.dictionary as d

class TestDictionary(unittest.TestCase):
	def test_translate_ENG_Arr_Single_definition(self):
		#If an English word only has 1 Arrernte Word
		word = "a"
		translation = t.get_word_translation("eng", word)
		self.assertEqual(translation, "anyente")

	@unittest.skip("Skipping for testing")
	def test_translate_ENG_ARR_Multiple_definition(self):
		#If an English word has multiple Arrernte Words
		word = "ache"
		translation = t.get_word_translation("eng", word)
		self.assertEqual(translation, ["arnteme","kwarneme","arlkweme"])

class TestWordObject(unittest.TestCase):
	def test_word_init(self):
		try: 
			word_object = Word()
		except:
			self.fail("Unable to create error")

class TestDictionary(unittest.TestCase):
	def test_dictionary_init(self):
	#Check that creating a new dictionary object works
		try:
			dictionary_object = d.Dictionary();
		except:
			self.fail("Unable to create empty Dictionary Object.")
	
	def test_dictionary_init(self):
	#Check that a dictionary object isnt empty
		dictionary_object = Dictionary()
		assertTrue(dictionary_object.words().len() != 0)

	
if __name__ == '__main__':
    unittest.main()
