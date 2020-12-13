FROM python:3.8

WORKDIR /app

RUN apt-get update && apt-get upgrade -y
RUN apt-get install ffmpeg -y

COPY . /app

RUN pip install -r requirements.txt
RUN pip install -U git+https://github.com/aboSamoor/polyglot.git@master
RUN polyglot download embeddings2.en
RUN polyglot download ner2.en
RUN polyglot download embeddings2.ar
RUN polyglot download ner2.ar

CMD python service.py