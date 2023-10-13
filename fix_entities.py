from pymongo import MongoClient
import re
import json

client = MongoClient("mongodb://localhost:27017")

db = client["resumeparser"]

collection = db["tds"]
collection2 = db["tds2"]

training_data_json = list(collection.find({}, {"_id": 0}))

fixed = 0


def trim_entity_spans(data: list) -> list:
    """Removes leading and trailing white spaces from entity spans.

    Args:
        data (list): The data to be cleaned in spaCy JSON format.

    Returns:
        list: The cleaned data.
    """
    global fixed
    invalid_span_tokens = re.compile(r"\s")

    # cleaned_data = []
    text, entities = data["text"], data["entities"]

    valid_entities = []
    for start, end, label in entities:
        print("processing...", start, end, label)
        valid_start = start
        valid_end = end
        while valid_start < len(text) and invalid_span_tokens.match(text[valid_start]):
            valid_start += 1
        while valid_end > 1 and invalid_span_tokens.match(text[valid_end - 1]):
            valid_end -= 1
        if valid_start != start or valid_end != end:
            fixed += 1
        valid_entities.append([valid_start, valid_end, label])

    return {"text": text, "entities": valid_entities}


def pasre_ents(td):
    text = td["text"]
    ents = td["entities"]

    values = []
    for ent in ents:
        value = text[ent[0] : ent[1]]
        if value.endswith(" ") or value.startswith(" "):
            print("⚠ Space detetcted ", value)
        values.append({ent[2]: value})

    return values


for td in training_data_json:
    cleantd = trim_entity_spans(td)
    if json.dumps(td) != json.dumps(cleantd):
        print("found a corrupt entity")
    else:
        cleantd["values"] = pasre_ents(cleantd)
        collection2.insert_one(cleantd)

print(f" Total {fixed} Entities Fixed")
