import json
import os

def load_test_data(path=None):
    if not path:
        path = os.path.join(os.path.dirname(__file__), '..', 'data', 'test_data.json')
    with open(path, "r") as file:
        return json.load(file)
