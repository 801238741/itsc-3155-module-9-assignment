# TODO: Feature 2
from src.models.movie import Movie
from src.repositories import movie_repository
from app import app
import pytest

client = app.test_client()
movieDatabase = movie_repository.get_movie_repository()
def test_myForm():
    response = client.post("/movies", data={"movieName": "Spongebob", "movieDirector": "Bob Allan", "rating": 3})
    assert response.status_code == 200

    assert type(movieDatabase.get_all_movies()[0]) == Movie
    with pytest.raises(IndexError):
        type(movieDatabase.get_all_movies()[1])

    assert movieDatabase.get_all_movies()[0].title == "Spongebob"
    assert movieDatabase.get_all_movies()[0].director == "Bob Allan"
    assert movieDatabase.get_all_movies()[0].rating == 3

    client.post("/movies", data={"movieName": "Nemo", "movieDirector": "Melvin", "rating": 1})
    assert movieDatabase.get_all_movies()[1].title != "Spongebob"
    assert movieDatabase.get_all_movies()[1].director == "Melvin"
    assert movieDatabase.get_all_movies()[1].rating == 1