import re
from googletrans import Translator

translator = Translator()
print(translator.translate('salom').text)

def translate(word, lang='en'):
    return translator.translate(word, lang).text

def language(word):
    return translator.detect(word).lang