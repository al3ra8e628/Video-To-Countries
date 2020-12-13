# Video-To-Countries

#### This is a tool that extract countries names that mentioned in youtube videos just by providing the video url and the language of the video, Supported Videos Languages Are English or Arabic.

## Modules

* **(service):**
  python back-end service which is responsible for processing the youtube file
* **(web-ui):**
  Angular web application that provide a web interface for sending the video processing request and export it as json
  when the process complete.

## Requirements

#### You can find the python packages in the [requirements.txt](service/requirements.txt) file

## Installing

#### A docker-compose deployment that can be deployed by running the [compose-run.sh](compose-run.sh) script.

## Third Party Libraries:

* Flask for creating a RestFul API

* Youtube-dl for downloading the youtube videos
* Azure(Speech-To-Text) for a converting the audio content to text
* polyglot(Name-Entity-Recognition) to extract the location related data from text

#### The following environment variables are required to connect to **`azure speech-to-text`** so don't forget to replace them with your own, expose them and change them in the docker-compose as well.

* the azure speech service `subscription key`:
  **AZURE_SPEECH_SUBSCRIPTION_KEY**
* the azure speech service `subscription region`:
  **AZURE_SPEECH_SUBSCRIPTION_REGION**

when running the docker-compose you can reach the application UI by visiting: **`http://localhost:9040/web-ui`**