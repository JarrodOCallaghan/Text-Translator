import sys
import os

def main():
##Main menu for the program
	print("Text translator for English and Eastern Central Arrernte")
	menu(sys.argv)

def menu(arguments):

	#Options:
	#No arguments given, print basic help (sys.argv only has python file name as arg[0])
	if len(arguments) == 1:
		print(text_basic_help)
	elif arguments[1] == '-h' or arguments[1] == '--help':
	#-h or --help
		print(text_help)
	elif arguments[1] == '-s' or arguments[1] == '--single-word':
	#Single text using -s or --single-word
		print("SWT")
		if len(arguments) == 2:
			#If language flag not included
			print("Please include source language as flags -en or -ar")
		elif  arguments[2] == '-en' or arguments[2] == '-ar':
			#Language flag included
			if len(arguments) == 3:
				#no word was provided
				print("Please enter word to translate")
			else:
				if len(arguments) >= 5:
					print("Multiple words detected, only translating the first word")
				else:
					print("Translating")
		else:
			print("Please include source language as flags -en or -ar")

	elif arguments[1] == '-d' or arguments[1] == '--direct':
		print("Direct translation")
		if len(arguments) == 2:
			#If language flag not included
			print("Please include source language as flags -en or -ar")
		elif  arguments[2] == '-en' or arguments[2] == '-ar':
			#Language flag included
			if len(arguments) == 3:
				#no word was provided
				print("Please enter a sentence to translate")
			else:
				print("Translating")
		else:
			print("Please include source language as flags -en or -ar")
	elif arguments[1] == '-ml':
		print("Machine Learning Translation")

		if len(arguments) == 2:
			#If language flag not included
			print("Please include source language as flags -en or -ar")
		elif  arguments[2] == '-en' or arguments[2] == '-ar':
			#Language flag included
			if len(arguments) == 3:
				#no word was provided
				print("Please enter a sentence to translate")
			else:
				print("Translating")
		else:
			print("Please include source language as flags -en or -ar")
	else:
		print("Unknown arguments given to the program")
		print(text_basic_help)

text_basic_help = "Help: [-h/--help]\nSingle word: [-s/--single-word] [-en/-ar] <word>.\nDirect translation [-d/--direct] [-en/-ar] <Body of test>.\nMachine Learning Translating [-ml] [-en/-ar] <Body of text>\nExample: python3 main.py -d -ar Werte ahelhe!"

text_help = "Help: [-h/--help]\nSingle Word Translating is achieved by a word lookup in the Data/ENG-CEA-Dictionary.txt file. It should be noted that the wordlist is a work in progress as there is no central digital dictionary to use and this is created from different resources. The CEA Acronym stands for Central-Eastern Arrernte\nUsage: [-s/--single-word] [-en/-ar] <word>.\nExample: python3 text-translator.py -s -en Hello\n\nDirect translation is similar to the single word translation. Does not take into account syntax.\nUsage [-d/--direct] [-en/-ar] <Body of test>.\nExample: python3 text-translator.py -d -ar Werte ahelhe!\n\nThe machine learning translation is a work in progress still. It is implemented using Google's Tensor Flow. Due to the limited dataset, it may prove innacurate.\nUsage: [-ml] [-en/-ar] <Body of text>\nExample: python3 text-translator.py -ml -en Hey! Over there!"
if __name__ == "__main__":
	main()
