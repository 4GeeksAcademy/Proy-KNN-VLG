# your code here
from pickle import load
from flask import Flask,request,render_template
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"