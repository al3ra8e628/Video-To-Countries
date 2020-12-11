import geograpy
import nltk

# TODO: move laoding these files to somewhere else,
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')


def extract(text):
    return geograpy.get_place_context(text=text)
