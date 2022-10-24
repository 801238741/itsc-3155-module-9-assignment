

from flask import Flask, redirect, render_template, request, Markup
from src.models import movie

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
    
    moiveTitle = request.form.get('MoiveTitle')
    moiveDireactor = request.form.get('direcatorName')
    moiveRating = request.form.get('rating', type=int)
    
    if moiveTitle is None or moiveDireactor is None or moiveRating is None or moiveRating < 0 or moiveRating > 5:
        message ="""<div class="alert alert-danger text-center" role="alert">Oops, You May Have Mis-Enter Few Info. <br>Please Follow The Instructions On The Text-Box</div>"""
        return render_template('create_movies_form.html', create_rating_active=False, message=Markup(message))
    else:
        movie_repository.create_movie(moiveTitle, moiveDireactor, moiveRating)
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    userSearch = request.args.get('searchTitle')
    movieRating = movie_repository.get_movie_by_title(userSearch)
    
   
            
    if not movieRating:
         message ="""<div class="alert alert-danger text-center" role="alert">Add moive?</div>"""
         return render_template('search_movies.html', search_active=False, message=Markup(message))
    else:
          movieRating
        
    return render_template('search_movies.html', search_active=True, movieRating=movieRating)
  


