import os, sys
from pathlib import Path



class Dictionary:
	def __init__(self):
		self.wordlist = self.get_wordlist()
		self.filepath

	def get_wordlist(filepath = "../data/ENG-ECA-Dictionary.txt"):
		wordlist_file = open(filepath, "r")
		wordlist_lines = wordlist_file.read().split('\n')
		for line in wordlist_lines:
			wordlist.append(line.split('\t'))

		print(wordlist)
		return wordlist


dictionary = Dictionary()
