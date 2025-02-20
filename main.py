from datasets import load_dataset
df = load_dataset("ai4privacy/pii-masking-200k")
print("Source")
print(df['train']['source_text'][0])
print("Target")
print(df['train']['target_text'][0])