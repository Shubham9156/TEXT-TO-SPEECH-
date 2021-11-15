# pdt to speech using gTTS, os

from gtts import gTTS 

import os

abc = open('sam.txt')

text = abc.read()

language = 'en'

obj = gTTS(text = text, lang = language, slow = False)

obj.save("sample.mp3")

os.system("sample.mp3")


