from datasets import Dataset

prompt = """Below is a story. Please summarize this in my style.

### Story:
{}

### Summary:
{}
""" + tokenizer.eos_token

finetuning_examples = []
for pair in FILES:
    with open(pair.format("story"), "r") as file:
        story = "".join(file.readlines())
    with open(pair.format("summary"), "r") as file:
        summary = "".join(file.readlines())
    finetuning_examples.append({
        "text": prompt.format(story, summary)
    })

dataset = Dataset.from_list(finetuning_examples)
