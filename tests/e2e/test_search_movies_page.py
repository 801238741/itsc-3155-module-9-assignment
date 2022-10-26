# TODO: Feature 3
from src.repositories.movie_repository import get_movie_repository
from app import app, movie_repository

def test_search_movies():
    # check repo is empty first
    assert movie_repository.get_all_movies() == []
    test_app = app.test_client()
    # go to search page
    search_page_resp = test_app.get('/movies/search')
    # check response code and main heading exists
    assert search_page_resp.status_code == 200
    assert b'<h1 class="mb-5">Search Movie Ratings</h1>' in search_page_resp.data
    # check movie details section doesn't show yet (before submitting)
    assert b'<div class="mt-3 text-center">' not in search_page_resp.data
    
    # add movie using post method
    movie_data_dictionary = {'movieName': "Tenet",
    'movieDirector': 'Christopher Nolan',
    'rating': 4}
    add_movie_resp = test_app.post('/movies', data = movie_data_dictionary, follow_redirects = True)
    assert add_movie_resp.status_code == 200
    #print(add_movie_resp.data)
    assert get_movie_repository().get_all_movies() != []

    # search movie
    movie_title = movie_data_dictionary['movieName']

    search_with_data_resp = test_app.get(f'/movies/search?movie-name={movie_title}')
    assert b'<h1 class="mb-5">Search Movie Ratings</h1>' in search_with_data_resp.data
    # check 'movie details' section shows now
    print(search_with_data_resp.data)
    assert b'<div class="mt-3 text-center">' in search_with_data_resp.data
    assert b'Tenet' in search_with_data_resp.data
    assert b'Christopher Nolan' in search_with_data_resp.data
    assert b'4' in search_with_data_resp.data



