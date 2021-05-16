#Code from: https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/text/nmt_with_attention.ipynb#scrollTo=AOpGoE2T-YXS
#Following Neural machine translation with attention
import tensorflow as tf

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from sklearn.model_selection import train_test_split

import unicodedata
import re
import numpy as np
import os
import io
import time


path_to_file = '/home/jarrod/Documents/Text-Translator/tensorflow_experiment/dataset/formatted-arrernte2.txt'
dirname = os.path.dirname(path_to_file)

def unicode_to_ascii(s):
	return ''.join(c for c in unicodedata.normalize('NFD', s)
		if unicodedata.category(c) != 'Mn')
	

def preprocess_sentence(w):
  w = unicode_to_ascii(w.lower().strip())

  # creating a space between a word and the punctuation following it
  # eg: "he is a boy." => "he is a boy ."
  # Reference:- https://stackoverflow.com/questions/3645931/python-padding-punctuation-with-white-spaces-keeping-punctuation
  w = re.sub(r"([?.!,¿])", r" \1 ", w)
  w = re.sub(r'[" "]+', " ", w)

  # replacing everything with space except (a-z, A-Z, ".", "?", "!", ",")
  w = re.sub(r"[^a-zA-Z?.!,¿-]+", " ", w)

  w = w.strip()

  # adding a start and an end token to the sentence
  # so that the model know when to start and stop predicting.
  w = '<start> ' + w + ' <end>'
  return w



'''
eng_sentence = u"Yes, I'm alright"
arr_sentence = u"Ye, ayenge mwerre"
print(preprocess_sentence(eng_sentence))
print(preprocess_sentence(arr_sentence).encode('utf-8'))
'''
# 1. Remove the accents
# 2. Clean the sentences
def create_dataset(path, num_examples):
	lines = io.open(path, encoding='UTF-8').read().strip().split('\n')
	word_pairs = [[preprocess_sentence(w) for w in line.split('\t')]
		for line in lines[:num_examples]]
	
	return zip(*word_pairs)



eng, arr = create_dataset(path_to_file, None)
print(eng[-1])
print(arr[-1])



def tokenize(lang):
	lang_tokenizer = tf.keras.preprocessing.text.Tokenizer(filters='')
	lang_tokenizer.fit_on_texts(lang)
	
	tensor = lang_tokenizer.texts_to_sequences(lang)
	tensor = tf.keras.preprocessing.sequence.pad_sequences(tensor, padding='post')
	
	return tensor, lang_tokenizer

def load_dataset(path, num_examples):
	# creating cleaned input, output pairs
	targ_lang, inp_lang = create_dataset(path, num_examples=None)

	input_tensor, inp_lang_tokenizer = tokenize(inp_lang)
	target_tensor, targ_lang_tokenizer = tokenize(targ_lang)

	return input_tensor, target_tensor, inp_lang_tokenizer, targ_lang_tokenizer

num_examples = 1000
input_tensor, target_tensor, inp_lang, targ_lang = load_dataset(path_to_file, num_examples)
max_length_targ, max_length_inp, = target_tensor.shape[1], input_tensor.shape[1]

# Creating training and validation sets using an 80-20 split
input_tensor_train, input_tensor_val, target_tensor_train, target_tensor_val = train_test_split(input_tensor, target_tensor, test_size=0.2)

# Show length
print(len(input_tensor_train), len(target_tensor_train), len(input_tensor_val), len(target_tensor_val))

def convert(lang, tensor):
	for t in tensor:
		if t != 0:
			print(f'{t} ----> {lang.index_word[t]}')

print("Input Language; index to word mapping")
convert(inp_lang, input_tensor_train[0])
print()
print("Target Language; index to word mapping")
convert(targ_lang, target_tensor_train[0])

BUFFER_SIZE = len(input_tensor_train)
BATCH_SIZE = 64
steps_per_epoch = len(input_tensor_train)//BATCH_SIZE
embedding_dim = 256
units = 1024
vocab_inp_size = len(inp_lang.word_index)+1
vocab_tar_size = len(targ_lang.word_index)+1
dataset = tf.data.Dataset.from_tensor_slices((input_tensor_train, target_tensor_train)).shuffle(BUFFER_SIZE)
dataset = dataset.batch(BATCH_SIZE, drom_remainder=True)

example_input_batch, example_target_batch = next(iter(dataset))
example_input_batch.shape, example_target_batch.shape

