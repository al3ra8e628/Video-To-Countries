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
* geopy for getting the countries name by its cities names in side it
* Azure(VideoIndexer)  Speech To Text(STT) Extracting the Speech from the video as text
* Azure(VideoIndexer)  Optical Character Recognition(OCR) for extracting the displayed words showed in the video
* Azure(TextAnalytics) Name Entity Recognition(NER) to extract location data from texts

#### The following environment variables are required to connect to **`azure web-services`** so don't forget to replace them with your own, expose them and change them in the docker-compose as well.

* the azure text analytics `subscription key`:
  **AZURE_TEXT_ANALYTICS_SUBSCRIPTION_KEY**
* the azure text analytics `subscription region`:
  **AZURE_TEXT_ANALYTICS_SUBSCRIPTION_REGION**
* the azure video indexer `subscription key`:
  **AZURE_VIDEO_INDEXER_SUBSCRIPTION_KEY**
* the azure video indexer `subscription location`:
  **AZURE_VIDEO_INDEXER_LOCATION**
* the azure video indexer `subscription accountID`:
  **AZURE_VIDEO_INDEXER_ACCOUNT_ID**

when running the docker-compose you can reach the application UI by visiting: **`http://localhost:9040/web-ui`**