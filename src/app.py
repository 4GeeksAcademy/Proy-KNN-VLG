# your code here
import pandas as pd
from pickle import load
from flask import Flask,request,render_template
from sklearn.feature_extraction.text import TfidfVectorizer
# no supervisado
from sklearn.neighbors import NearestNeighbors

app = Flask(__name__)

model = load(open(r"KNN_recomendations_movies.sav", "rb"))

df=pd.read_csv(r"clean_data.csv")
vectorizer = TfidfVectorizer()
df_vectorized = vectorizer.fit_transform(df["tags"])

def recommend(movie):
    movie_index = df[df["title"] == movie].index[0]
    distances,indices = model.kneighbors(df_vectorized[movie_index])
    movie_list = [(df["title"][i],distances[0][j]) for j,i in enumerate(indices[0])]
    #sorted(list(enumerate(distances)), reverse = True , key = lambda x: x[1])[1:6]
    
    #for i,distances in movie_list:
      #  print("movie:{}".format(i))
    return movie_list[1:]
            

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":

        # Obtain values from form
        movie_name = str(request.form["movie"])
        prediction = recommend(movie_name)
    else:
        prediction = None

    return render_template("index.html", prediction = prediction)