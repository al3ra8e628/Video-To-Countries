import time

from jsonpath_ng.ext import parse
from video_indexer import VideoIndexer

CONFIG = {
    'SUBSCRIPTION_KEY': '1b9899f438524a60af21946e9f9f8cac',
    'LOCATION': 'trial',
    'ACCOUNT_ID': '7f9a24ec-6ca5-4c18-8328-9b205fee7488'
}

video_indexer = VideoIndexer(
    vi_subscription_key=CONFIG['SUBSCRIPTION_KEY'],
    vi_location=CONFIG['LOCATION'],
    vi_account_id=CONFIG['ACCOUNT_ID']
)


def process(video_file_path, language):
    # video_id = vi.upload_to_video_indexer(
    #     input_filename=video_file_path,
    #     video_name=uuid.uuid4(),
    #     video_language="English")

    # video_id = 'a54015442b'
    video_id = '6fcd4b3231'

    video_info = fetch_video_info(
        video_id=video_id,
        language=language
    )

    while video_info['state'] is 'processing':
        time.sleep(2)
        video_info = fetch_video_info(video_id, language)

    speech_as_text = video_indexer.get_caption_from_video_indexer(
        video_id=video_id,
        video_language=language,
        caption_format="txt"
    )

    ocr_text = extract_ocr_text(video_info)

    return {
        "speech_as_text": speech_as_text.strip(),
        "ocr_text": ocr_text.strip()
    }


def fetch_video_info(video_id, language):
    video_info = video_indexer.get_video_info(
        video_id=video_id,
        video_language=language
    )
    return video_info


def extract_ocr_text(json_data):
    ocr_items_list = parse('$.videos[0].insights.ocr[*].text').find(json_data)

    ocr_final_values = []

    for item in ocr_items_list:
        temp_val = ("".join(item.value)).strip() + ","
        if temp_val not in ocr_final_values:
            ocr_final_values.append(temp_val)

    return "".join(ocr_final_values)

# https://www.geeksforgeeks.org/python-test-if-string-contains-element-from-list/