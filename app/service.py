import threading

from flask import Flask, request, jsonify

import ProcessVideoJob
from repositories import ProcessRepository

app = Flask(__name__)


@app.route('/processes', methods=['POST'])
def start_process():
    req_data = request.get_json()
    video_url = str(req_data['url'])

    # TODO: uncomment this when finish developing
    # if ProcessRepository.is_process_duplicate(video_url):
    #     return jsonify({
    #         "violation": "Video Already Processed"
    #     }), 400

    process = ProcessRepository.save_process(video_url)
    process_video_job = threading.Thread(target=ProcessVideoJob.run,
                                         args=(process,))
    process_video_job.start()
    return process


@app.route('/processes', methods=['GET'])
def list_processes():
    return jsonify(ProcessRepository.list_processes())


@app.route('/processes/<process_id>', methods=['GET'])
def get_process_details(process_id):
    return jsonify(ProcessRepository.fetch_process(process_id))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
