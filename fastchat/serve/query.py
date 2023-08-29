# AHP # hugging face
from datasets import load_dataset
import os.path
prompts = []

# Load SST dataset
dataset = load_dataset("sst")

# Access train split
train_dataset = dataset["train"]

# Access text and labels from the train split
train_texts = train_dataset["sentence"]
train_labels = train_dataset["label"]

#     # Specify the path to the CSV file
#     csv_file = "sst_dataset.csv"

#     # Check if the CSV file exists
#     file_exists = os.path.isfile(csv_file)
print("LEN OF TRAIN: ", len(train_texts))
for text, label in zip(train_texts[:1], train_labels[:1]):#zip(train_texts[:5], train_labels[:5]):
    #writer.writerow([text, label])
    prompts.append([f''' Classify the following sentence as either positive or negative: "{text}"''', label])

#parser.add_argument("--prompts", type=list, default=prompts)