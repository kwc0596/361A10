import requests, json, wikipedia, jsonify
def wiki_query(query):
    data = wikipedia.summary(query, sentences=2)
    dict2json = {}
    dict2json["data"] = data
    return (dict2json["data"])
