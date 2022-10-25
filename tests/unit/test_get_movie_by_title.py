# TODO: Feature 3
from src.repositories import movie_repository
def test_movie_search():
    movie_repo = movie_repository.get_movie_repository()
    empty_list = []
    # check repo is empty first
    print("checking repo is empty...")
    assert movie_repo.get_all_movies() == empty_list
    assert len(movie_repo.get_all_movies()) == 0
    # add movie to repo
    movie = movie_repo.create_movie("Interstellar", "Christopher Nolan", 5)
    assert len(movie_repo.get_all_movies()) != 0
    assert movie_repo.get_all_movies()[0] == movie
    # search for movie in repo
    found_movie = movie_repo.get_movie_by_title("Interstellar")
    assert found_movie == movie
    assert found_movie.title == movie.title
    assert found_movie.director == movie.director
    assert found_movie.rating == movie.rating


