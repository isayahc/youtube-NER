# !pip install transformers

import torch
from transformers import BertTokenizer, BertForTokenClassification

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForTokenClassification.from_pretrained('bert-base-uncased', num_labels=3)

text = "The quick brown fox jumps over the lazy dog. The high man lights up another joint."
tokens = tokenizer.tokenize(text)
input_ids = tokenizer.convert_tokens_to_ids(tokens)
attention_mask = [1] * len(input_ids)

input_tensor = torch.tensor([input_ids])
attention_tensor = torch.tensor([attention_mask])

with torch.no_grad():
    output = model(input_tensor, attention_mask=attention_tensor)

label_indices = torch.argmax(output[0], axis=2)

tokens = tokenizer.convert_ids_to_tokens(input_tensor[0])
new_tokens, new_labels = [], []
for token, label_idx in zip(tokens, label_indices[0]):
    if token.startswith("##"):
        new_tokens[-1] = new_tokens[-1] + token[2:]
    else:
        new_labels.append(label_idx)
        new_tokens.append(token)

for token, label in zip(new_tokens, new_labels):
    print("{}\t{}".format(label, token))
