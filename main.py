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
		print("To use program:")
	elif arguments[1] == '-h' or arguments[1] == '--help':
	#-h or --help
		print("Advanced Help")
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

	elif arguments[1] == '-oo' or arguments[1] == '--one-for-one':
		print("one for one translation")
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

text_basic_help = ""
text_help = "HELP TEXT"

if __name__ == "__main__":
	main()
