import logging

from polyglot.downloader import downloader

downloader.supported_tasks(lang="ar")
downloader.supported_tasks(lang="en")

from polyglot.text import Text


def extract(text):
    countries = []
    text = Text(text)
    for sentence in text.sentences:
        logging.info("Named Entity Recognition Started On The Following Text: {}", sentence)
        for entity in sentence.entities:
            if entity.tag == 'I-LOC' and \
                    entity[0] not in countries:
                countries.append(entity[0])
    return countries
