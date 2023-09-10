# IMP GLOBAL VARIABLES
prompts = []
few_shot_prompts = ()
file_name = "./TEST_dataset.csv"



# AHP # hugging face
from datasets import load_dataset
import os.path




# Load SST dataset
dataset = load_dataset("sst")

# Access train split
test_dataset = dataset["test"]

# Access text and labels from the train split
test_texts = test_dataset["sentence"]
test_labels = test_dataset["label"]

print("LEN OF TRAIN: ", len(test_texts))
for text, label in zip(test_texts[:], test_labels[:]):#zip(train_texts[:5], train_labels[:5]):
    #writer.writerow([text, label])
    prompts.append([f''' Classify the following sentence as either positive or negative: "{text}"''', label])

#parser.add_argument("--prompts", type=list, default=prompts)




few_shot_prompts =     ( # FEW SHOT LEARNING
            (
                "USER",
                ''' Classify the following sentence as either positive or negative: “that loves its characters and communicates something rather beautiful about human nature.” ''',
            ),
            (
                "ASSISTANT",
                "The answer is positive.",
            ),
            (
                "USER",
                '''Classify the following sentence as either positive or negative: “demonstrates that the director of such hollywood blockbusters as patriot games can still turn out a small, personal film with an emotional wallop.”''',
            ),
            (
                "ASSISTANT",
                "The answer is positive.",
            ),
            (
                "USER",
                '''Classify the following sentence as either positive or negative: “swimming is above all about a young woman’s face, and by casting an actress whose face projects that woman’s doubts and yearnings, it succeeds.”''',
            ),
            (
                "ASSISTANT",
                "The answer is positive.",
            ),
            (
                "USER",
                '''Classify the following sentence as either positive or negative: “for those moviegoers who complain that ’they don’t make movies like they used to anymore.’”''',
            ),
            (
                "ASSISTANT",
                "The answer is negative.",
            ),
            (
                "USER",
                '''Classify the following sentence as either positive or negative: “which half of dragonfly is worse: the part where nothing’s happening, or the part where something’s happening.”''',
            ),
            (
                "ASSISTANT",
                "The answer is negative.",
            ),
            (
                "USER",
                ''' Classify the following sentence as either positive or negative: “the plot is nothing but boilerplate cliches from start to finish.”''',
            ),
            (
                "ASSISTANT",
                "The answer is negative.",
            ),
        )


