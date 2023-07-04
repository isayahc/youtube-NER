from gensim.models.phrases import Phrases, Phraser
from nltk.tokenize import word_tokenize
import nltk 

nltk.download('punkt')
# Define a list of sentences
sentences = [
    'the quick brown fox jumps over the lazy dog',
    'the quick brown fox jumps over the lazy dog again'
]

# Tokenize the sentences
tokenized_sentences = [word_tokenize(sentence.lower()) for sentence in sentences]

# Train a phrase detection model
phrases = Phrases(tokenized_sentences, min_count=1, threshold=1)

# Create a phraser object
phraser = Phraser(phrases)

# Apply phrase detection to the tokenized sentences
phrased_sentences = [phraser[sentence] for sentence in tokenized_sentences]

# Print the results
print(phrased_sentences)
