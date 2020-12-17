FROM python:3.8

WORKDIR /app

RUN apt-get update && apt-get upgrade -y
RUN apt-get install ffmpeg -y

COPY . /app

RUN pip install -r requirements.txt

CMD python service.py