import os
import time

import azure.cognitiveservices.speech as speechsdk

# AZURE_SPEECH_SUBSCRIPTION_KEY = os.getenv("AZURE_SPEECH_SUBSCRIPTION_KEY")
# AZURE_SPEECH_SUBSCRIPTION_REGION = os.getenv("AZURE_SPEECH_SUBSCRIPTION_REGION")

AZURE_SPEECH_SUBSCRIPTION_KEY = "48cce319739240a7b9d957f694a64221"
AZURE_SPEECH_SUBSCRIPTION_REGION = "eastasia"


def convert(file_path):
    speech_config = speechsdk.SpeechConfig(
        subscription=AZURE_SPEECH_SUBSCRIPTION_KEY,
        region=AZURE_SPEECH_SUBSCRIPTION_REGION
    )
    speech_config.enable_dictation()

    audio_config = speechsdk.audio.AudioConfig(filename=file_path)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    done = False

    def stop_cb(evt):
        print('CLOSING on {}'.format(evt))
        nonlocal done
        done = True

    all_results = []

    def handle_final_result(evt):
        all_results.append(evt.result.text + " ")

    speech_recognizer.recognized.connect(handle_final_result)
    speech_recognizer.session_stopped.connect(lambda evt: print(evt))

    speech_recognizer.session_stopped.connect(stop_cb)
    speech_recognizer.canceled.connect(stop_cb)

    speech_recognizer.start_continuous_recognition()

    while not done:
        print(all_results)
        time.sleep(1)

    speech_recognizer.stop_continuous_recognition()
    # os.remove(file_path)
    return "".join(all_results)