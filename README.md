# Text-Translator

## About

This project aims to implement a two way translator for English and Central Eastern Arrernte. Central Eastern Arrernte is a language from Alice Springs, Australia. It is primarily a spoken language and as a result there is limited digital resources.


### Goals
The current goals include implementing a feedback loop to put direct translations into the implemented TensorFlow Neural Language Translation. Assisting with the dataset for the TensorFlow training model. This is because there is limited English - Central Eastern Arrernte examples.

It would be useful to implement a syntax formatter in the code which could be used to feed into the TensorFlow Training Model.

The project also aims to be able to translate large bodies of text in the future. For example, a news article or the text in a book. This is pending on an accurate consistent implementation of translation.

### Limitations

Currently, some words dont translate directly into another and will instead translate to multiple words.
For example, the Arrernte word 'Ware' translates into 'Not much'. The current implementation of the single and multiple word translations wont be able to translate 'Not Much' back to 'Ware', instead it will look for 'not' and 'much' as their own words.

With the TensorFlow ML, there is a limited set of digital data available to use to train. So with a limited dataset, the ML implementation translation isn't accurate. Currently, the goals for the project outline how this can be solved.


### Getting Started


This project was developed using python 3.9.5.
https://www.python.org/downloads/

Navigate to the project directory and create a new python environment:

For Mac / Unix:
```
	python3 -m venv env
```
For Windows:
```
py -m venv env
```

After activating the environment:

For Mac / Unix:
```
source env/bin/activate
```
For Windows:
```
env/Scripts/activate.bat
```

#### Requirements

Requirements can be installed using:
```
pip install -r requirements.txt
```
This project has been worked on Ubuntu, Mac and Windows.

After setting up the python environment, the project can be ran using:
(The following commands will be show using unix, for windows use 'py' instead of 'python3')
```
python3 text-translator.py
```

### Translation functionality

The project includes its own English - Central Eastern Arrernte dictionary file in the /data folder. However this can be updated or changed for other languages, words and phrases.

There are three modes for translation:
* Single word
* Direct word
* Machine Learning

Single Word Translating is achieved by a word lookup in the Data/ENG-CEA-Dictionary.txt file.

It should be noted that the wordlist is a work in progress as there is no central digital dictionary to use and this is created from different resources.
The CEA Acronym stands for Central-Eastern Arrernte

Usage:
```
python text-translator.py [-s/--single-word] [-en/-ar] <word>.
```
Example:
```
python3 text-translator.py -s -en Hello
```


Direct translation is similar to the single word translation. Does not take into account syntax.

Usage:
```
python3 text-translator.py [-d/--direct] [-en/-ar] <Body of test>.
```

Example:

```
python3 text-translator.py -d -ar Werte ahelhe
```


The machine learning translation is a work in progress still. It is implemented using Google's Tensor Flow. Due to the limited dataset, it may prove inaccurate.

Usage:
```
python3 text-translator.py [-ml] [-en/-ar] <Body of text>
```

Example:
```
python3 text-translator.py -ml -en Hey! Over there!
```



### Tests

Tests can be ran from the main project directory using:

```
python -m unittest tests/test_project.py
```
All test cases are currently in the test_project.py file.


### RESOURCES:

* Eastern and Central Arrernte to English Dictionary - IAD Press 1994
* https://arrernte-angkentye.online/ECALL.html?v=1.3
