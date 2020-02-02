import json
import random

from src import EXAMPLE_JSON_FILE_PATH


def get():
    with open(EXAMPLE_JSON_FILE_PATH) as json_file:
        data = json.load(json_file)
    videos = data.get('categories', [{}])[0].get('videos', [])
    return random.choice(videos)
