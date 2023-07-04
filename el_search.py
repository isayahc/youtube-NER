from gensim.models.phrases import Phrases, Phraser
from elasticsearch import Elasticsearch
from srt_to_text import srt_to_list
from nltk.tokenize import word_tokenize

# Define a list of documents
documents = [
    'the quick brown fox jumps over the lazy dog',
    'the quick brown fox jumps over the lazy dog again'
]

# Train a phrase detection model
phrases = Phrases(documents, min_count=1, threshold=1)

# Create a phraser object
phraser = Phraser(phrases)

# Generate queries for Elasticsearch
queries = []
for document in documents:
    tokens = phraser[word_tokenize(document.lower())]
    query = {
        'query': {
            'match': {
                'text': ' '.join(tokens)
            }
        }
    }
    queries.append(query)

# Connect to Elasticsearch
es = Elasticsearch()

# Index the documents
for i, document in enumerate(documents):
    es.index(index='my_index', id=i, body={'text': document})

# Search for phrases in the documents
for query in queries:
    results = es.search(index='my_index', body=query)
    print(results)
