# TODO: Feature 2
from src.repositories import movie_repository
def test_create_movie():
    movieDatabase = movie_repository.get_movie_repository()
    assert movieDatabase.get_all_movies() == []
    
    movie = movieDatabase.create_movie("Spongebob", "Melvin", 5)
    movie2 = movieDatabase.create_movie("software", "Mark", 2)
    assert len(movieDatabase.get_all_movies()) == 2
    assert movie.title == "Spongebob"
    assert movie.rating == 5
    assert movie.director == "Melvin"
    assert movie2.rating == 2
    assert movie2.director == "Mark"
