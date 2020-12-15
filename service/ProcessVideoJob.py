import logging
import os

from repositories.ProcessRepository import update_process
from tools import ContriesFromTextExtractor
from tools import VideoIndexerInterface


def run(process):
    logging.info("starting video process with process id {}", process["process_id"])
    try:
        # update_process({
        #     "process_id": process["process_id"],
        #     "status": "DOWNLOADING"
        # })
        # # download youtube video as wav file
        # file_path = YoutubeAsWavDownloder.download(process["video_url"])
        # # convert wav file to text

        video_file_path = "temp/countries-across-asia-report-covid-19-spikes_no_audio.mp4"

        update_process({
            "process_id": process["process_id"],
            "status": "PROCESSING"
        })

        video_processing_result = VideoIndexerInterface \
            .process(video_file_path, process["video_lang"])

        countries_from_speech = ContriesFromTextExtractor.extract(
            video_processing_result['speech_as_text'])

        countries_from_ocr = ContriesFromTextExtractor.extract(
            video_processing_result['ocr_text'])

        update_process({
            "process_id": process["process_id"],
            "status": "COMPLETED",
            "countries_form_speech": countries_from_speech,
            "countries_from_ocr": countries_from_ocr,
            "shared_countries": get_shared_items(
                countries_from_speech, countries_from_ocr
            )})

        os.remove(video_file_path)
    except RuntimeError as e:
        logging.info("exception occurred on video processing {}", e)
        update_process({
            "process_id": process["process_id"],
            "status": "FAILED",
            "failingReason": str(e)
        })


def get_shared_items(countries_from_speech,
                     countries_from_ocr):
    pass
