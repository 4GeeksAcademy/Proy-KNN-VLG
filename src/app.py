# your code here
import pandas as pd
from pickle import load
from flask import Flask,request,render_template
from sklearn.feature_extraction.text import TfidfVectorizer
# no supervisado
from sklearn.neighbors import NearestNeighbors

app = Flask(__name__)

model = load(open("KNN_recomendations_movies.sav", "rb"))

df=pd.read_csv("/workspaces/Proy-KNN-VLG/src/clean_data.csv")

def recommend(movie):
    movie_index = df[df["title"] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse = True , key = lambda x: x[1])[1:6]
    
    for i in movie_list:
        print(df.iloc[i[0]].title)


@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":

        # Obtain values from form
        movie_name = str(request.form["movie"])
        prediction = recommend(movie_name)
    else:
        prediction = None

    return render_template("index.html", prediction = prediction)