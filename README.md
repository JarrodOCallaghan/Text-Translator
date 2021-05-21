# Text-Translator

## About

This project aims to implement a two way translator for English and Central Eastern Arrernte. Central Eastern Arrernte is a language from Alice Springs, Australia. It is primarily a spoken language and as a result there is limited digital resources.

Please note, when running the Tensorflow training function, access to a GPU with Cuda cores. For more information, see https://www.tensorflow.org/install/gpu.


### Goals
* The current goals include implementing a feedback loop to put direct translations into the implemented TensorFlow Neural Language Translation. Assisting with the dataset for the TensorFlow training model. This is because there is limited English - Central Eastern Arrernte examples.

* It would be useful to implement a syntax formatter in the code which could be used to feed into the TensorFlow Training Model.

* The project also aims to be able to translate large bodies of text in the future. For example, a news article or the text in a book. This is pending on an accurate consistent implementation of translation.

* Some of the code can be refactored. There is some duplication in the code which can be reduced, for example the translator has loops to search wordlist, this can be split up into its own functions. Also, there is potential for larger bodies of text to perform slowly due to O(n^2) complexity for each word is looked up individually. May need to look at a more suitable data structure to solve this issue.

* Refactor the tensorflow ml.py code so functions are split up more effectively.

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

#### Training the Translator

To save project space, the training checkpoint's haven't been included in the repo.
The project currently has removed the training function from being callable from the command line tool.
To run the training function, changed the following code in the file /lib/tensorflow_experiment/ml.py

```
path_to_file = 'lib/tensorflow_experiment/dataset/formatted-arrernte2.txt'
```
to
```
path_to_file = /dataset/formatted-arrernte2.txt
```

and at the bottom of the ml.py file, uncomment out the following:
```
#call_training()
```

When running this script from within the lib/tensorflow_experiment file, the script will train based on the formatted-arrernte2.txt text document.\
Please not that this changes the relative path for the formatted-arrernte2.txt script and you will need to change it back to run python ml-text-translator.py

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

This project is using autopep8 as its linter. To use the linter:

```
autopep8 --in-place --aggressive --aggressive <filename>
```

e.g.:

```
autopep8 --in-place --aggressive --aggressive lib/translator.py
```


### Tests

Tests can be ran from the main project directory using:

```
python -m unittest tests/test_project.py
```
All test cases are currently in the test_project.py file.

To run code coverage.py, under the project directory, use:

```
coverage run -m unittest tests/test_project.py
```
To view results, use:
```
coverage report
```

To generate A HTML page to view coverage results, use:
```
coverage html
```

### RESOURCES:

* Eastern and Central Arrernte to English Dictionary - IAD Press 1994
* https://arrernte-angkentye.online/ECALL.html?v=1.3
