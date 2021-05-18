# Text-Translator
Text Translator for English to Arrernte


Proof of concept for Eng to Arr translator

Goals:
To create a Proof of concept text translator for Eng <> ECA (Central and Eastern Arrernte).
The project aims to be able to translate from one to the other. Focusing on text translations.

Single word translations will also be useful

Ideal end use case. API which translates text with high accuracy for primary use of website translations.

Unsure if I will use ML to achieve this goal or a simple word swap. For Proof of concept simple text swapping might be fine.

Current aims for translation in two modes. 1 to 1 word swap and sentence swapping with correct translation.
1 to 1 swap will show how the syntax is different, this could later be used with ML to improve syntax translation.

Current Limitations: 
I don't know the language myself and will need to rely on resources I have and can find.

No access to native speakers of Eastern and Central Arrernte. This might be solved however.


Pass in a body of text. Select starting language. Translate body of text into different specified language.

RESOURCES:
Eastern and Central Arrernte to English Dictionary - IAD Press 1994
https://arrernte-angkentye.online/ECALL.html?v=1.3

NOTES:
Character set for Eastern and Central Arrernte is the same as English.

TECH STACK:
Ubuntu 20.04.2 LTS
VIM 8.1

REQUIREMENTS: 
autopep8    1.5.7

Experimenting with Tensorflow for 'Neural machine translation with attention'.
*Tensorflow is licensed under Apache License 2.0 
