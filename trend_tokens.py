from gensim.models.phrases import Phrases, Phraser
from pytrends.request import TrendReq
from nltk.tokenize import word_tokenize

# Define a list of queries
queries = [
    'the quick brown fox jumps over the lazy dog',
    'the quick brown fox jumps over the lazy dog again'
]

# Train a phrase detection model
phrases = Phrases(queries, min_count=1, threshold=1)

# Create a phraser object
phraser = Phraser(phrases)

# Generate queries for PyTrends
pytrends = TrendReq()
for query in queries:
    tokens = phraser[word_tokenize(query.lower())]
    pytrends.build_payload(kw_list=tokens)
    results = pytrends.interest_over_time()
    print(results)
