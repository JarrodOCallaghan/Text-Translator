import sys
import os
import lib.dictionary as d
import lib.translator as t
#import lib.tensorflow_experiment.ml as tf

def main():
    # Main menu for the program
    print("Text translator for English and Eastern Central Arrernte")
    dictionary = d.Dictionary()
    translator = t.Translator(dictionary)
    menu(sys.argv, dictionary, translator)


def menu(arguments, dictionary, translator):

    # Options:
    # No arguments given, print basic help (sys.argv only has python file name
    # as arg[0])
    if len(arguments) == 1:
        print(text_basic_help)
    elif arguments[1] == '-h' or arguments[1] == '--help':
        #-h or --help
        print(text_help)
    elif arguments[1] == '-s' or arguments[1] == '--single-word':
        # Single text using -s or --single-word
        if len(arguments) == 2:
            # If language flag not included
            print("Please include source language as flags -en or -ar")
        elif arguments[2] == '-en' or arguments[2] == '-ar':
            # Language flag included
            if len(arguments) == 3:
                # no word was provided
                print("Please enter word to translate")
            else:
                if len(arguments) >= 5:
                    #Warning user that additional words will be ignored, only processing first word.
                    #In the future, there is the potential to only use the direct translaton as direct translation on a single word gives the same result
                    print("Multiple words detected, only translating the first word")
                print(
                    translator.translate_single_word(
                        arguments[2], arguments[3]))
                #Here we are printing the array provided from translator. This shows text in []. In the future we could loop through the results and print in a nicer format.
        else:
            print("Please include source language as flags -en or -ar")

    elif arguments[1] == '-d' or arguments[1] == '--direct':
        print("Direct translation: ")
        if len(arguments) == 2:
            # If language flag not included
            print("Please include source language as flags -en or -ar")
        elif arguments[2] == '-en' or arguments[2] == '-ar':
            # Language flag included
            if len(arguments) == 3:
                # no word was provided
                print("Please enter a sentence to translate")
            else:
                #Looping through all additional arguments as these will be treated as words to be translated
                i = 3
                to_translate = ""
                while i < len(arguments):
                    to_translate = to_translate + " " + arguments[i]
                    i += 1
                print(translator.translate_direct(arguments[2], to_translate))
        else:
            print("Please include source language as flags -en or -ar")
    elif arguments[1] == '-ml':
        #Split the machine learning translator into its own function as it is still a work in process while the dataset is small.
        #Also noticed that the -s and -d translations were slow due to importing the tensorflow lib.
        print("To use the TensorFlow translation [EXPERIMENTAL], please use the python script: ml-text-translation.")
        print("Example:\npython3 ml-text-translation.py -en word")
    else:
        print("Unknown arguments given to the program")
        print(text_basic_help)


#created strings for the help text as they are used a few times in the menu
text_basic_help = "Help: [-h/--help]\nSingle word: [-s/--single-word] [-en/-ar] <word>.\nDirect translation [-d/--direct] [-en/-ar] <Body of test>.\nMachine Learning Translating EXPERIMENTAL [-ml] [-en] using ml-text-translator.py<Body of text>\nExample: python3 text-translalor.py -d -ar Werte ahelhe!"

text_help = "Help: [-h/--help]\nSingle Word Translating is achieved by a word lookup in the Data/ENG-CEA-Dictionary.txt file. It should be noted that the wordlist is a work in progress as there is no central digital dictionary to use and this is created from different resources. The CEA Acronym stands for Central-Eastern Arrernte\nUsage: [-s/--single-word] [-en/-ar] <word>.\nExample: python3 text-translator.py -s -en Hello\n\nDirect translation is similar to the single word translation. Does not take into account syntax.\nUsage [-d/--direct] [-en/-ar] <Body of test>.\nExample: python3 text-translator.py -d -ar Werte ahelhe!\n\n[EXPERIMENTAL] The machine learning translation is a work in progress still. It is implemented using Google's Tensor Flow. It has been split up into its own python script to improve single and direct translation not requiring to import the TensorFlow library. Due to the limited dataset, it may prove inaccurate.\nUsage: [-ml] [-en/-ar] <Body of text>\nExample: python3 ml-text-translator.py -ml -en Hey! Over there!\n "
if __name__ == "__main__":
    main()
