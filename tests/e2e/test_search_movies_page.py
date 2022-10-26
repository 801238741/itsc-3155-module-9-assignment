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
    movie_title = str(movie_data_dictionary['movieName'])
    
    # search movie
    search_with_data_resp = test_app.get(f'/movies/search', query_string={'movie-name': movie_title})
    assert b'<h1 class="mb-5">Search Movie Ratings</h1>' in search_with_data_resp.data
    assert search_with_data_resp.status_code == 200
    # check 'movie details' section shows now
    assert b'<div class="mt-3 text-center">' in search_with_data_resp.data
    assert b'<span class="text-decoration-underline fw-normal">' in search_with_data_resp.data
    assert b'<div class="card w-25 mx-auto">' in search_with_data_resp.data
    assert b'Tenet' in search_with_data_resp.data
    assert b'Christopher Nolan' in search_with_data_resp.data
    assert b'4' in search_with_data_resp.data
    assert movie_repository.get_movie_by_title(movie_title).title == 'Tenet'
    assert movie_repository.get_movie_by_title(movie_title).rating == 4
    assert movie_repository.get_movie_by_title(movie_title).director == 'Christopher Nolan'

    # search a non-existing movie
    search_not_found_resp = test_app.get('/movies/search', query_string = {'movie-name' : 'fake'})
    assert search_not_found_resp.status_code == 200
    print(search_not_found_resp.data)
    assert b'<h1 class="mb-5">Search Movie Ratings</h1>' in search_not_found_resp.data
    assert b'No Movie Found!' in search_not_found_resp.data
    # check movie doesn't show
    assert b'fake' not in search_not_found_resp.data



