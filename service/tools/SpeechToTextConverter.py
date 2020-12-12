# AZURE_SPEECH_SUBSCRIPTION_KEY = os.getenv("AZURE_SPEECH_SUBSCRIPTION_KEY")
# AZURE_SPEECH_SUBSCRIPTION_REGION = os.getenv("AZURE_SPEECH_SUBSCRIPTION_REGION")


def convert(file_path):
    # speech_config = speechsdk.SpeechConfig(
    #     subscription=AZURE_SPEECH_SUBSCRIPTION_KEY,
    #     region=AZURE_SPEECH_SUBSCRIPTION_REGION
    # )
    # speech_config.enable_dictation()
    #
    # audio_config = speechsdk.audio.AudioConfig(filename=file_path)
    # speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    # done = False
    #
    # def stop_cb(evt):
    #     print('CLOSING on {}'.format(evt))
    #     nonlocal done
    #     done = True
    #
    # all_results = []
    # speech_recognizer.recognized.connect(lambda evt: all_results.append(evt.result.text + " "))
    # speech_recognizer.session_stopped.connect(lambda evt: print(evt))
    #
    # speech_recognizer.session_stopped.connect(stop_cb)
    # speech_recognizer.canceled.connect(stop_cb)
    #
    # speech_recognizer.start_continuous_recognition()
    #
    # while not done:
    #     print(all_results)
    #     time.sleep(1)
    #
    # speech_recognizer.stop_continuous_recognition()
    # # TODO: uncomment this line when no need for keeping the files
    # # os.remove(file_path)
    # # return "".join(all_results)
    return "It's what history demands from the United States of America. It's what the future asks of you. You graduate Health Department is the best health Department in the United States of America. But I'll tell you that the previous administration radical threat was the greatest threat to United States of America and he tried getting everybody to recognize it. There weren't listening when he was talking. No, he had about. God bless our United States of America. Thank you."
