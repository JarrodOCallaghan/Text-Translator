class Translator():
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.wordlist = dictionary.wordlist

    def translate_single_word(self, language, word):
        # Translate single word
        # Returning an array of words for when there are multiple
        # interpretations, we can print all variations
        found_words = []
        if language == '-en':
            for dict_word in self.wordlist:
                if word.lower() == dict_word[1].lower():
                    found_words.append(dict_word[0])
        elif language == '-ar':
            for dict_word in self.wordlist:
                if word.lower() == dict_word[0].lower():
                    found_words.append(dict_word[1])
        if not found_words:
            found_words.append("?")
        return found_words

    def translate_direct(self, language, sentence):
        sentence = sentence.split()
        translated_words = []
        translated_sentence = ""
        for word in sentence:
            translated_words.append(self.translate_single_word(language, word))

        for word_list in translated_words:
            if len(word_list) > 1:
                translated_sentence += "["
                for word in word_list:
                    if word == word_list[-1]:
                        translated_sentence += word
                    else:
                        translated_sentence += word + "/"
                translated_sentence += "] "
            else:
                translated_sentence += word_list[0] + " "
        return translated_sentence



# Need to split up to avoid duplication
'''
    def search_single_word(self, language, word):
        # Translate single word
        found_words = ""
        if language == '-en':
            for dict_word in self.wordlist:
                if word.lower() in dict_word[1].lower():
                    if found_words == "":
                        found_words = dict_word[0]
                    else:
                        found_words = found_words + ", " + dict_word[0]
        elif language == '-ar':
            for dict_word in self.wordlist:
                if word.lower() in dict_word[0].lower():
                    if found_words == "":
                        found_words = dict_word[1]
                    else:
                        found_words = found_words + ", " + dict_word[1]
        if found_words == "":
            return "Unable to find word"
        else:
            return found_words

'''
