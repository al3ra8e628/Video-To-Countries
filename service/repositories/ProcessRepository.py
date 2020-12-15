import uuid

processes = []


def save_process(process):
    process_id = str(uuid.uuid4())
    process = {
        "video_url": process["video_url"],
        "video_lang": get_video_lang_or_default_en(process),
        "process_id": process_id,
        "status": "STARTING"
    }
    processes.append(process)
    return process


def list_processes():
    return processes


def update_process(update_request):
    item_details = get_item_by_property_value("process_id", update_request["process_id"])
    if item_details is None:
        raise RuntimeError('cannot find process by provided process_id')

    item_index = item_details["index"]
    item = processes[item_index]
    for prop in update_request:
        item[prop] = update_request[prop]
    processes[item_index] = item
    return item


def fetch_process(process_id):
    by_process_id = get_item_by_property_value("process_id", process_id)
    if by_process_id is None:
        raise RuntimeError('cannot find process by provided process_id')
    return by_process_id["item"]


def is_process_duplicate(video_url):
    return get_item_by_property_value("video_url", video_url) is not None


def get_item_by_property_value(property_name, value):
    for i, item in enumerate(processes):
        if item[property_name] == value:
            result = {
                "index": i,
                "item": item
            }
            return result
    return None


def get_video_lang_or_default_en(process):
    return "en" if process["video_lang"] is None else str(process["video_lang"])
