import urllib.request
import json
import os

import json

def read_jsonl(file_path):
    data = []
    with open(file_path, 'r', encoding="utf8") as file:
        for line in file:
            data_str = json.loads(line)
            data.append(data_str)
    return data

data_url = "https://huggingface.co/datasets/ai4privacy/pii-masking-300k/resolve/main/data/train/1english_openpii_30k.jsonl"
data_path = "./cache/1english_openpii_30k.jsonl"
if not (os.path.exists("./cache")): os.mkdir("./cache")
if not (os.path.exists(data_path)): urllib.request.urlretrieve(data_url, data_path)
else: data_file = read_jsonl(data_path)
print(data_file[0]['source_text'])
print(data_file[0]['target_text'])