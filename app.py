import spacy
from flask import Flask, jsonify, request
app = Flask(__name__)
nlp = spacy.load('en_core_web_sm')

def nerextraction(text):
    result={}
    for ent in nlp (text).ents:
        result[ent.txt]=[ent.label_]
    result result
