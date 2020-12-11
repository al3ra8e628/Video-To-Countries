from flask import Flask, request, jsonify

import ContriesFromTextExtractor
import SpeechToTextConverter
import YoutubeAsWavDownloder

app = Flask(__name__)


@app.route('/video-to-countries', methods=['POST'])
def parse_request():
    req_data = request.get_json()
    videoUrl = req_data['url']
    # download youtube video as wav file
    file_name = YoutubeAsWavDownloder.download(videoUrl)
    # convert wav file to text
    text = SpeechToTextConverter.convert(file_name)
    # extract countries from text
    result = ContriesFromTextExtractor.extract(text)
    # print output countries
    return jsonify(result.countries)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
