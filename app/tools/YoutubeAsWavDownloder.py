import logging
import os
import subprocess
import uuid

from youtube_dl import YoutubeDL


def download(url):
    file_name = "temp/" + str(uuid.uuid4())
    mp3_file_path = file_name + ".mp3"

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': mp3_file_path,
        'progress_hooks': [progress_hook],
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'prefer_ffmpeg': True,
        'keepvideo': False
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    wav_file_path = file_name + ".wav"
    subprocess.call(['ffmpeg', '-i', mp3_file_path, wav_file_path])
    os.remove(mp3_file_path)
    return wav_file_path


def progress_hook(d):
    if d['status'] == 'downloading':
        logging.info("downloading {} percent {} downloading...",
                     d['filename'], d['_percent_str'])
    if d['status'] == 'finished':
        logging.info("Done downloading...")
