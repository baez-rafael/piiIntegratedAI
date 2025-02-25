import urllib.request
import os

data_url = "https://huggingface.co/datasets/ai4privacy/pii-masking-300k/resolve/main/data/train/1english_openpii_30k.jsonl"
data_path = "./cache/1english_openpii_30k.jsonl"
if not (os.path.exists("./cache")): os.mkdir("./cache")
if not (os.path.exists(data_path)): urllib.request.urlretrieve(data_url, data_path)