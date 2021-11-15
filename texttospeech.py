# text to speech using gTTS, os


from gtts import gTTS 

import os

text = "HEllo guys."

language = 'en'

obj = gTTS(text = text, lang = language, slow = False)

obj.save("sample.mp3")

os.system("sample.mp3")
