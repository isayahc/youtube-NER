import spacy
from sklearn.cluster import KMeans
import numpy as np

# Load the English language model
nlp = spacy.load('en_core_web_sm')

# Define a function to extract word vectors from text
def extract_word_vectors(text):
    doc = nlp(text)
    vectors = []
    for token in doc:
        if not token.is_stop and token.is_alpha:
            vectors.append(token.vector)
    return np.array(vectors)

# Define a function to cluster word vectors
def cluster_word_vectors(vectors, n_clusters=5):
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(vectors)
    return kmeans.labels_

# Define a function to extract entities from text
def extract_entities(text):
    vectors = extract_word_vectors(text)
    labels = cluster_word_vectors(vectors)
    entities = []
    for i, label in enumerate(labels):
        if label != 0:
            entities.append((text.split()[i], label))
    return entities

# Example usage
text = "I watched The Godfather starring Marlon Brando last night"
entities = extract_entities(text)
print(entities)
