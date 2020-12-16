import logging

from youtube_dl import YoutubeDL


def download(process_details):
    out_file_path = "temp/" + process_details["process_id"]

    with YoutubeDL({
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': out_file_path,
        'progress_hooks': [progress_hook],
    }) as ydl:
        ydl.download([process_details["video_url"]])

    return out_file_path + ".mp4"


def progress_hook(d):
    if d['status'] == 'downloading':
        logging.info("downloading... {}", d['_percent_str'])
    if d['status'] == 'finished':
        logging.info("Done downloading...")
