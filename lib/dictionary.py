import os, sys
from pathlib import Path

class Dictionary:
	def __init__(self):
		self.wordlist = self.get_wordlist()
		self.filepath

	def get_wordlist(filepath = "../data/ENG-ECA-Dictionary.txt"):
		wordlist_file = open(filepath, "r")
		wordlist_lines = wordlist_file.read().split('\n')
		print(wordlist_lines)
		for line in wordlist_lines:
			wordlist.append(line.split('\t'))

		print(wordlist)
		return wordlist


def get_wordlist(filepath = "../data/ENG-ECA-Dictionary.txt"):
	wordlist_file = open(filepath, "r")
	wordlist_lines = wordlist_file.read().split('\n')
	print(wordlist_lines)
	wordlist = []
	for line in wordlist_lines:
		wordlist.append(line.split('\t'))
	#print(wordlist)
	for word in wordlist:
		print("Arrernte word: %s, English word: %s"% (word[0], word[1]) )
	#return wordlist

get_wordlist()
