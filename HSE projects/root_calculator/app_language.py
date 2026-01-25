import json
import os

current = {}

def load(lang):
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, "languages", f"{lang}.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    current.clear()
    current.update(data)