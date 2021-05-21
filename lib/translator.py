class Translator():
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.wordlist = dictionary.wordlist

    def translate_single_word(self, language, word):
        # Translate single word
        # Returning an array of words for when there are multiple
        # interpretations, we can print all variations
        found_words = []
        #wordlist returns wordlist [[Arrernte word], [English Word]]
        #Index [1] for english [0] for arrernte
        if language == '-en':
            for dict_word in self.wordlist:
                if word.lower() == dict_word[1].lower():
                    found_words.append(dict_word[0])
        elif language == '-ar':
            for dict_word in self.wordlist:
                if word.lower() == dict_word[0].lower():
                    found_words.append(dict_word[1])
        if not found_words:
            #Currently returning ? so that the user has some indication that the word wasn't found
            found_words.append("?")
        #Found words is being translated as an array
        return found_words

    def translate_direct(self, language, sentence):
        sentence = sentence.split()
        #We want to split up the compiled sentence given from the text-translator string.
        translated_words = []
        translated_sentence = ""
        #For each word, we are getting the single translation
        for word in sentence:
            translated_words.append(self.translate_single_word(language, word))

        for word_list in translated_words:
            if len(word_list) > 1:
                #Currently, words can return multiple spellings or interpretations.
                #To accomodate this, the code puts them in brackets seperated by a / so the user has some indication as to what word could be used.
                translated_sentence += "["
                for word in word_list:
                    if word == word_list[-1]:
                        translated_sentence += word
                    else:
                        translated_sentence += word + "/"
                translated_sentence += "] "
            else:
                translated_sentence += word_list[0] + " "
        #We are returning the translated sentence as a string here.
        return translated_sentence



# Need to split up to avoid duplication
# The below function would be used to find occurrences where the source word is in the translation text.
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
