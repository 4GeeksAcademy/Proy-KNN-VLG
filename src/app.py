# your code here
from pickle import load
from flask import Flask,request,render_template
from sklearn.feature_extraction.text import TfidfVectorizer
# no supervisado
from sklearn.neighbors import NearestNeighbors

app = Flask(__name__)

model = load(open("/workspaces/Proy-KNN-VLG/src/KNN_recomendations_movies.sav", "rb"))

@app.route("/")