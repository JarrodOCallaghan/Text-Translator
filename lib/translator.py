class Translator():
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.wordlist = dictionary.wordlist
    def translate_single_word(self, language, word):
        #Translate single word
        found_words = ""
        if language == '-en':
            for dict_word in self.wordlist:
                if word.lower() in dict_word[1].lower():
                    found_words = found_words + ", " + dict_word[0]
        elif language == '-ar':
            for dict_word in self.wordlist:
                if word.lower() in dict_word[0].lower():
                    found_words = found_words + ", " + dict_word[1]
        if found_words == "":
            return "Unable to find word"
        else:
            return found_words


    def translate_direct(self, language, sentence):
        #Do somthing
        sentence = sentence.split()
        translated_sentence = ""
        for word in sentence:
            translated_sentence = translated_sentence + self.translate_single_word(language, word)
        return translated_sentence
