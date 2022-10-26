# TODO: Feature 1
from flask.testing import FlaskClient

from src.repositories import movie_repository




def test_list_movie_page(test_app: FlaskClient):
    response = test_app.get('/movies')
    response_data = response.data

    print(response_data)
    assert b'<h1 class="h1 text-center mt-5 pt-5">No Moives Found In The Database. <a href="/movies/new">Click To Add Movies</a></h1>' in response_data

    # Adding movies using a post method
    movie_data_dictionary = {
    'movieName': "Tenet",
    'movieDirector': 'Christopher Nolan',
    'rating': 4}
    add_movie_resp = test_app.post('/movies', data = movie_data_dictionary, follow_redirects = True)

    allMovie = movie_repository.get_movie_repository()
    
    
    #Testing to see if the movies created above are in the response_data
    
    # Movie 1
    assert b'<td>Tenet</td>' in add_movie_resp.data
    assert b'<td>Christopher Nolan</td>' in add_movie_resp.data
    assert b'<td>4</td>' in add_movie_resp.data
    
    # Adding movies using methods
    allMovie.create_movie('Example Movie2', 'Example Director2', 5)
    allMovie.create_movie('Example Movie3', 'Example Director3', 2)
    response = test_app.get('/movies')
    response_data = response.data

    # Movie 2
    assert b'<td>Example Movie2</td>' in response_data
    assert b'<td>Example Director2</td>' in response_data
    assert b'<td>5</td>' in response_data
    
    # Movie 3
    assert b'<td>Example Movie3</td>' in response_data
    assert b'<td>Example Director3</td>' in response_data
    assert b'<td>2</td>' in response_data