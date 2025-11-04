import json
from interfaces.storage import Storage

class JSONStorage(Storage):
    def __init__(self, file_path):
        self.file_path = file_path

    def save(self, data):
        with open(self.file_path, "w") as f:
            json.dump(data, f)

    def load(self):
        with open(self.file_path, "r") as f:
            return json.load(f)
