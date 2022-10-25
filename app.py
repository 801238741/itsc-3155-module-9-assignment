from flask import Flask, redirect, render_template, request, Markup

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

movie_repository = get_movie_repository()

@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    

    return render_template('list_all_movies.html', list_movies_active=True, result = movie_repository.get_all_movies())


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    # After creating the movie in the database, we redirect to the list all movies page
  
    movieTitle = request.form.get('movieName', type=str)
    movieDirector = request.form.get('movieDirector', type=str)
    movieRating = request.form.get('rating', type=int)
    
    if movieTitle is None or movieDirector is None or movieRating is None or movieRating < 0 or movieRating > 5:
        message ="""<div class="alert alert-danger text-center" role="alert">Oops, You May Have Misentered Few Info. <br>Please Follow The Instructions On The Text-Box</div>"""
        return render_template('create_movies_form.html', create_rating_active=False, message=Markup(message))
    else:
        movie_repository.create_movie(movieTitle, movieDirector, movieRating)
        return render_template('list_all_movies.html', result=movie_repository.get_all_movies())

@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    movie_rating = ''
    # if form is submitted/page is visited with input
    if request.args:
        input_title = request.args.get('movie-name')
        found_movie = movie_repository.get_movie_by_title(input_title)
        # if movie not found, show message to add it to the database
        if not found_movie:
            return render_template('search_movies.html', search_active=True, submitted=True)
        # otherwise if movie is found show the title and rating
        return render_template('search_movies.html', search_active=True, movie=found_movie, submitted=True)
    # if page was visited normally/without submitting form show the normal page
    return render_template('search_movies.html', search_active=True)
