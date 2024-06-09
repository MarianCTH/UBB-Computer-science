from src.domain.MovieDomain import Movie
from src.exceptions.RepositoryExceptions import RepositoryException

class MovieService:
    def __init__(self, movie_validator, movie_repository):
        self.__validator = movie_validator
        self.__repository = movie_repository

    def add_movie(self, movie_id, title, description, genre):
        new_movie = Movie(movie_id, title, description, genre)
        self.__validator.ValidateNewMovie(new_movie)
        self.__repository.add_movie(new_movie)

    def delete_movie(self, movie_id):
        self.__repository.delete_movie(movie_id)

    def update_movie(self, movie_id, new_movie_title):
        self.__repository.update_movie(movie_id, new_movie_title)

    def list_movies(self):
        movies = self.__repository.get_all()
        if len(movies) > 0:
            for key, movie_object in movies.items():
                print(movie_object)
        else:
            raise RepositoryException("There are no movies in the list !")

    def search(self, movie_id, movie_title, movie_description, movie_genre):
        movies = self.__repository.get_all()
        found_movies = []
        if movie_id:
            return self.__repository.find_one_movie(movie_id)
        elif movie_title:
            for id, movie in movies.items():
                if movie_title.lower() in (movie.GetTitle()).lower():
                    found_movies.append(movie)
        elif movie_description:
            for id, movie in movies.items():
                if movie_description.lower() in (movie.GetDescription()).lower():
                    found_movies.append(movie)
        elif movie_genre:
            for id, movie in movies.items():
                if movie_genre.lower() in (movie.GetGenre()).lower():
                    found_movies.append(movie)
        if len(found_movies) > 0:
            return found_movies
        else:
            raise RepositoryException("There are no clients with this name !")

    def find_one_movie(self, movie_id):
        return self.__repository.find_one_movie(movie_id)