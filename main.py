import urllib.request
import json
import nltk
import os

# First Time Setup
def read_jsonl(file_path):
    data = []
    with open(file_path, 'r', encoding="utf8") as file:
        for line in file: data.append(json.loads(line))
    return data

data_url = "https://huggingface.co/datasets/ai4privacy/pii-masking-300k/resolve/main/data/train/1english_openpii_30k.jsonl"
data_path = "./cache/1english_openpii_30k.jsonl"
nltk_data_path = os.path.join(os.path.expanduser("~"), "AppData/Roaming/nltk_data")
if not (os.path.exists("./cache")): os.mkdir("./cache")
if not (os.path.exists(data_path)): urllib.request.urlretrieve(data_url, data_path)
else: data_file = read_jsonl(data_path)
if not (os.path.exists(nltk_data_path)): nltk.download()

# Actual Data Processing

stop_words = set(nltk.corpus.stopwords.words('english'))

def tokenize_and_filter(sample):

    mini_filter = sample.replace("\\n", " ").replace("'", " ").replace(",", " ")
    # Use NLTK tokenize to split
    tokenized_example = nltk.word_tokenize(mini_filter)
    # Change to lower case and get rid of any punctuations
    lower_tokenized_ex = [w.lower() for w in tokenized_example if not any(c in "[]" for c in w)]
    # Get rid of stop words.
    filtered_ex = [w for w in lower_tokenized_ex if w not in stop_words]

    print(sample)
    print(tokenized_example)
    print(lower_tokenized_ex)
    print(filtered_ex)
    return filtered_ex


# for i in range(100):

i = 31
example_src = data_file[i]['source_text']
example_tgt = data_file[i]['target_text']
filtered_src = tokenize_and_filter(example_src)
filtered_tgt = tokenize_and_filter(example_tgt)
if len(filtered_src) < len(filtered_tgt):
    print("IDX:", i)
    print(example_src)
    print(example_tgt)
    print(filtered_src)
    print(filtered_tgt)
    print(len(filtered_src))
    print(len(filtered_tgt))