import unittest
import lib.translator as t
import lib.word as w
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


class Test_Word(unittest.TestCase):
	def test_new_word(self):
		try:
			word = w.Word("A","B")
		except:
			self.fail("Unable to create word object")


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
