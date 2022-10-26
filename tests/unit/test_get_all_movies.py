# TODO: Feature 1
from src.repositories import movie_repository

def test_movie_model():

    allMovie = movie_repository.get_movie_repository()

    # Checks if the database is empty
    assert len(allMovie.get_all_movies()) == 0

    # Adding two exmaple movie
    allMovie.create_movie("Example Movie", 'Example Direactor', 5)
    allMovie.create_movie("Example Movie2", 'Example Direactor2', 4)

    # Checks updated database 
    assert len(allMovie.get_all_movies()) != 0

    # Checks if the movies on the database matches with movies created
    assert allMovie.get_all_movies()[0].title == 'Example Movie'
    assert allMovie.get_all_movies()[0].director == 'Example Direactor'
    assert allMovie.get_all_movies()[0].rating == 5
    
    assert allMovie.get_all_movies()[1].title == 'Example Movie2'
    assert allMovie.get_all_movies()[1].director == 'Example Direactor2'
    assert allMovie.get_all_movies()[1].rating == 4