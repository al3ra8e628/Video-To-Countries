import logging
import os

from repositories.ProcessRepository import update_process
from tools import VideoIndexerInterface, ContriesFromTextExtractor
from tools import YoutubeVideoDownloder


def run(process):
    logging.info("starting video process with process id {}", process["process_id"])
    try:
        video_language = process["video_lang"]
        process_id = process["process_id"]

        update_process_status(process_id=process_id, status="DOWNLOADING")
        video_file_path = YoutubeVideoDownloder.download(process)

        update_process_status(process_id=process_id, status="PROCESSING")
        video_processing_result = VideoIndexerInterface.process(video_file_path,
                                                                process,
                                                                update_process_fun)

        countries_from_speech = ContriesFromTextExtractor.extract(text=video_processing_result['speech_as_text'],
                                                                  lang=video_language)

        countries_from_ocr = ContriesFromTextExtractor.extract(text=video_processing_result['ocr_text'],
                                                               lang=video_language)

        common_countries = get_shared_items(countries_from_speech, countries_from_ocr)

        update_process({
            "process_id": process_id,
            "status": "COMPLETED",
            "countries_form_speech": countries_from_speech,
            "countries_from_video": countries_from_ocr,
            "common_countries": common_countries})
        os.remove(video_file_path)
    except RuntimeError as e:
        logging.info("exception occurred on video processing {}", e)
        update_process({
            "process_id": process["process_id"],
            "status": "FAILED",
            "failingReason": str(e)
        })


def update_process_status(process_id, status):
    update_process({
        "process_id": process_id,
        "status": status
    })


def extract_countries_from_text(video_language, text):
    return ContriesFromTextExtractor.extract(text=text,
                                             lang=video_language)


def get_shared_items(countries_from_speech, countries_from_ocr):
    return list(set(countries_from_speech).intersection(countries_from_ocr))


def update_process_fun(process_updates):
    update_process(process_updates)
