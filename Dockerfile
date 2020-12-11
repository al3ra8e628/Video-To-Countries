FROM python:3.7

WORKDIR /

COPY lib ./

RUN pip3 install --upgrade youtube_dl
RUN pip3 install --upgrade SpeechRecognition
RUN pip3 install --upgrade azure-cognitiveservices-speech
RUN pip3 install --upgrade AudioSegment
RUN pip3 install --upgrade geograpy3
RUN pip3 install --upgrade newspaper3k
RUN pip3 install --upgrade Flask

#RUN python3 service.py
CMD [ "python", "lib/service.py" ]