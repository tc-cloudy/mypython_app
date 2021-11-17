from flask import Flask, request, Response
import json

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

# @app.route("/hello")
# def world():
#     return "<h1>Hello World!!</>"

movie_db = {
   "1" : { "name" : "Stargate", "release_date": "1994" },
   "2" : { "name" : "Star Wars", "release_date" : "1977" },
   "3" : { "name" : "Bring It On", "release_date" : "2001" } 
}


@app.route("/movies")
def movies():
    return json.dumps(movie_db)

@app.route("/movie/<movie_id>")
def get_movie(movie_id):
    return json.dumps(movie_db[movie_id])

@app.route("/movie/add", methods=['POST'])
def add_movie():
    req_data = request.get_json()
    movie = req_data['movie']

    new_movie = { "4" : movie }
    movie_db.update(new_movie)
    return "Movie was added successfully"

if __name__ == "__main__":
    app.run(host='127.0.0.1')




if __name__ == "__main__":
    app.run(host='127.0.0.1')
