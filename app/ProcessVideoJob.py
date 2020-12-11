import logging

from repositories.ProcessRepository import update_process
from tools import YoutubeAsWavDownloder, SpeechToTextConverter, ContriesFromTextExtractor


def run(process):
    logging.info("starting video process with process id {}", process["process_id"])
    try:
        # download youtube video as wav file
        file_name = YoutubeAsWavDownloder.download(process["video_url"])
        # convert wav file to text
        text = SpeechToTextConverter.convert(file_name)
        # extract countries from text
        result = ContriesFromTextExtractor.extract(text)
        #

        # update process to completed
        update_process({
            "process_id": process["process_id"],
            "status": "COMPLETED",
            "countries": result.countries
        })
    except RuntimeError as e:
        logging.info("exception occurred on video processing {}", e)
        update_process({
            "process_id": process["process_id"],
            "status": "FAILED",
            "failingReason": str(e)
        })
