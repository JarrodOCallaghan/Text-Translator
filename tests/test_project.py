import unittest
import lib.translator as t
import lib.dictionary as d

class Test_Dictionary(unittest.TestCase):

	def test_dictionary_creation(self):
		try:
			dictionary = d.Dictionary()
		except:
			self.fail("Unable to create Dictionary")

	def test_get_wordlist(self):
		dictionary = d.Dictionary()
		wordlist = dictionary.get_wordlist()
		self.assertNotEqual(len(wordlist), 0)

	def test_get_wordlist_file_does_not_exist(self):
		with self.assertRaises(FileNotFoundError):
			dictionary = d.Dictionary()
			wordlist = dictionary.get_wordlist(" ")





class Test_single_translator(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.dictionary = d.Dictionary()
		cls.wordlist = cls.dictionary.get_wordlist()
		cls.translator = t.Translator(cls.dictionary)

	def test_single_word_en_one_response(self):
		self.assertEqual(self.translator.translate_single_word('-en', 'ground'), ['ahelhe'])

	def test_single_word_en_multiple_response(self):
		self.assertEqual(self.translator.translate_single_word('-en', 'throat'), ['ahentye','ite','pmulpere','pmwelpere'])
	def test_single_word_ar_unknown_response(self):
		self.assertEqual(self.translator.translate_single_word('-ar', 'NOTAWORD'), ['?'])

	def test_single_word_en_unknown_response(self):
		self.assertEqual(self.translator.translate_single_word('-en', 'NOTAWORD'), ['?'])

	def test_single_word_ar_one_response(self):
		self.assertEqual(self.translator.translate_single_word('-ar', 'ulte'), ['side'])

	def test_single_word_ar_multiple_response(self):
		self.assertEqual(self.translator.translate_single_word('-ar', 'tyelpme'), ['chips of wood', 'splinter'])

	@unittest.skip("ToDo")
	def test_eng_single_word_with_Special_character(self):
		dictionary = d.Dictionary()
		language = "-en"
		word = "Hello!"
		translation = dictionary.lookup_word(language,word)
		self.assertEqual(translation, "Werte!")

class Test_String_Translator(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.dictionary = d.Dictionary()
		cls.wordlist = cls.dictionary.get_wordlist()
		cls.translator = t.Translator(cls.dictionary)

	def test_string_en_no_alt_words(self):
		self.assertEqual(self.translator.translate_direct('-en', 'wind tail fire'), 'rlke tile ure ')

	def test_string_en_with_alt_words(self):
		self.assertEqual(self.translator.translate_direct('-en', 'wind good fire'),'rlke [mwarre/mwerre] ure ')

	def test_string_en_nothing_found(self):
		self.assertEqual(self.translator.translate_direct('-en', 'String'), "? ")

	def test_string_ar_no_alt_words(self):
		self.assertEqual(self.translator.translate_direct('-ar', 'rlke tile ure'),'wind tail fire ')

	def test_string_ar_with_alt_words(self):
		self.assertEqual(self.translator.translate_direct('-ar', 'rlke mwerre ure'),'wind [good/well/useable/proper/safe] fire ')

	def test_string_ar_nothing_found(self):
		self.assertEqual(self.translator.translate_direct('-ar', 'String'), "? ")

class Test_dictionary(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.dictionary = d.Dictionary()
		cls.wordlist = cls.dictionary.get_wordlist()
		cls.translator = t.Translator(cls.dictionary)

	def test_dictionary_init(self):
	#Check that creating a new dictionary object works
		try:
			dictionary_object = d.Dictionary()
		except:
			self.fail("Unable to create empty Dictionary Object.")

if __name__ == '__main__':
    unittest.main()
