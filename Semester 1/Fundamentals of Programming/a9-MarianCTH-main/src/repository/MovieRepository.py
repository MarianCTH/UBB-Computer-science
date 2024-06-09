from src.exceptions.RepositoryExceptions import RepositoryException

class MovieRepository:
    def __init__(self):
        self.__movies = {}

    def add_movie(self, movie):
        if movie.GetID() in self.__movies:
            raise RepositoryException("Movie with this ID already exists !")
        self.__movies[movie.GetID()] = movie

    def delete_movie(self, movie_id):
        if movie_id in self.__movies.keys():
            self.__movies.pop(movie_id)
        else:
            raise RepositoryException("Movie doesn't exist !")
    def update_movie(self, movie_id, new_movie_title):
        if movie_id in self.__movies.keys():
            if new_movie_title != "":
                self.__movies[movie_id].SetTitle(new_movie_title)
            else:
                raise RepositoryException("Invalid new movie title !")
        else:
            raise RepositoryException("Movie with this ID doesn't exist !")
    def get_all(self):
        return self.__movies
    def set_all(self, new_movies):
        self.__movies = new_movies
    def find_one_movie(self, movie_id):
        if movie_id in self.__movies:
            return self.__movies[movie_id]
        raise RepositoryException("The movie was not found !")
