import spacy
from typing import List, Dict

def entity_recognition(text:str,model:str='en_core_web_lg') -> None:
    nlp = spacy.load(model)

    # Process the text
    doc = nlp(text)

    # Print the named entities found in the text
    for entity in doc.ents:
        print(f"{entity.text} ({entity.label_})")


def alt_entity_recognition(text:str,model:str='en_core_web_lg',entity_types:List[str]=None) -> Dict[str,List[str]]:
    nlp = spacy.load(model)

    # Process the text
    doc = nlp(text)

    ent_list = [i.text for i in doc.ents if i.label_ in entity_types]

    unique_ent_list = list(set(ent_list))
    return unique_ent_list

    # Collect the named entities found in the text
    entities = {}
    for entity in doc.ents:
        if entity_types is None or entity.label_ in entity_types:
            if entity.label_ not in entities:
                entities[entity.label_] = []
            entities[entity.label_].append(entity.text)
    return entities


if __name__ == '__main__':
    # Test the function with a sample text
    # entity_recognition("Apple Inc. decided to hire Tim Cook on August 24, 2011.")
    model = 'en_core_web_lg'
    alt_entity_recognition()