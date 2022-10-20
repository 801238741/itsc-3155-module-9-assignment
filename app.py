from flask import Flask, redirect, render_template, request, Markup

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

movie_repository = get_movie_repository()
movie_repository.create_movie("Spider-Man: No Way Home (2021)", "Marvel", "7.4")

@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    print(movie_repository.get_all_movies()[0].title)
    return render_template('list_all_movies.html', list_movies_active=True, movie_list=movie_repository)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    # After creating the movie in the database, we redirect to the list all movies page
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    movie_rating = ''
    if request.args:
        input_title = request.args.get('movie-name')
        found_movie = movie_repository.get_movie_by_title(input_title)
        if not found_movie:
            return render_template('search_movies.html', search_active=True, movie_found=False)
        movie_rating = found_movie.rating
        print(movie_rating)
        return render_template('search_movies.html', search_active=True, movie=found_movie, movie_found=True)
    return render_template('search_movies.html', search_active=True)
