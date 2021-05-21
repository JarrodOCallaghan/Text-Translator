import sys
import os
import lib.dictionary as d
import lib.tensorflow_experiment.ml as tf


'''
Split machine learning functionality into its own class while the training dataset is low.
Also splitting as the import lib.tensorflow_experiment.ml code was slowing translations as it loaded  in the tensorflow script
'''
def main():
    # Main menu for the program
    print("Text translator for English and Eastern Central Arrernte")
    menu(sys.argv)


def menu(arguments):
    if len(arguments) == 1:
        print(text_basic_help)
    elif arguments[1] == '-h' or arguments[1] == '--help':
        #-h or --help
        print(text_help)
    elif arguments[1] == '-ml':
        print("Machine Learning Translation [EXPERIMENTAL]")

        if len(arguments) == 2:
            # If language flag not included
            print("Please include source language as flags -en. The current training dataset only accomodates English to Arrernte")
        elif arguments[2] == '-en' or arguments[2] == '-ar':
            # Language flag included
            if len(arguments) == 3:
                # no word was provided
                print("Please enter a sentence to translate")
            else:
                print("Translating")
                i = 3
                to_translate = ""
                while i < len(arguments):
                    to_translate = to_translate + " " + arguments[i]
                    i += 1
                tf.translate(to_translate)
        else:
            print("Please include source language as flags -en or -ar")
    else:
        print("Unknown arguments given to the program")
        print(text_basic_help)


text_basic_help = "Help:\nMachine Learning Translating EXPERIMENTAL [-ml] [-en] <Body of text>\nExample: python3 text-translalor.py -ml -en Hello Earth!"

text_help = "Help:\n[EXPERIMENTAL] The machine learning translation is a work in progress still. It is implemented using Google's Tensor Flow. Due to the limited dataset, it may prove inaccurate.\nUsage: [-ml] [-en/-ar] <Body of text>\nExample: python3 text-translator.py -ml -en Hey! Over there!\n "
if __name__ == "__main__":
    main()
