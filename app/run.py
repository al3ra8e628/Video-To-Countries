import ContriesFromTextExtractor
import SpeechToTextConverter
import YoutubeAsWavDownloder


def run():
    # best_video_for_such_test = "https://www.youtube.com/watch?v=5pOFKmk7ytU"
    best_video_for_such_test = "https://www.youtube.com/watch?v=YSi6XWgT3_8"

    # download youtube video as wav file
    file_name = YoutubeAsWavDownloder.download(best_video_for_such_test)
    # convert wav file to text
    text = SpeechToTextConverter.convert(file_name)
    # extract countries from text
    result = ContriesFromTextExtractor.extract(text)
    # print output countries
    print(result.countries)


# if __name__ == '__main__':
#     run()
