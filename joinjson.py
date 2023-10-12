import glob
import json
from pymongo import MongoClient

flist = glob.glob("data\output3\*.json")

print(f"Total {len(flist)} files found ")

client = MongoClient("mongodb://localhost:27017")

db = client["resumeparser"]

collection = db["tds"]


def savetherecord(record):
    newrecord = None

    if "text" in record.keys():
        ents = record["entities"]["entities"]
        # record["entities"] = ents
        newrecord = {"text": record["text"], "entities": ents}

    if "annotations" in record.keys():
        if len(record["annotations"]) > 0:
            text = record["annotations"][0][0]
            ents = record["annotations"][0][1]["entities"]
            newrecord = {"text": text, "entities": ents}
        else:
            print(record["annotations"])

    if newrecord != None:
        collection.insert_one(newrecord)


def processdata(record):
    if type(record) == dict:
        # print(record.keys())
        savetherecord(record)
    elif type(record) == list:
        for r in record:
            processdata(r)
    pass


for f in flist:
    with open(f, "r", encoding="utf-8") as fp:
        jsondata = json.load(fp)
        # print(type(jsondata))
        if type(jsondata) == list:
            # get list of resumes
            for record in jsondata:
                processdata(record)
            pass
        elif type(jsondata) == dict:
            # get one record
            processdata(jsondata)
            pass

# database => [collections]
# collection  => [documents]
# doument => {json object}
# _id => creation timestamp
