import logging
import uuid

from youtube_dl import YoutubeDL


def download(url):
    out_file_path = "temp/" + str(uuid.uuid4()) + ".mp4"

    with YoutubeDL({
        'format': '135',
        'outtmpl': out_file_path,
        'progress_hooks': [progress_hook]
    }) as ydl:
        ydl.download([url])

    return out_file_path


def progress_hook(d):
    if d['status'] == 'downloading':
        logging.info("downloading {} percent {} downloading...", d['filename'], d['_percent_str'])
    if d['status'] == 'finished':
        logging.info("Done downloading...")
