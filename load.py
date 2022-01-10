import json
from serialization_module import from_json


with open('basic.json', 'r', encoding='utf-8') as f:
    entry_example = json.load(f, object_hook=from_json)

print(entry_example)

