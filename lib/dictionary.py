import os, sys
from pathlib import Path
'''
This class acts as a dictionay object containing wordlist
wordlist [[Arrernte word], [English Word]]
'''

class Dictionary:

	def __init__(self):
		self.wordlist = self.get_wordlist()

	def get_wordlist(self, filepath = "data/ENG-ECA-Dictionary.txt"):
		#Filepath is currently set based on parent text-translator.py file
		wordlist_file = open(filepath, "r")
		wordlist_lines = wordlist_file.read().split('\n')
		wordlist_file.close()
		#print(wordlist_lines)
		new_wordlist = []
		for line in wordlist_lines:
			if line != "":
				new_wordlist.append(line.split('\t'))
		return new_wordlist
		#print(wordlist)
		#return wordlist
