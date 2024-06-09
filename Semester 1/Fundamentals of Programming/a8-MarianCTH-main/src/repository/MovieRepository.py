import pickle

from src.exceptions.RepositoryExceptions import RepositoryException


class MovieRepository:
    def __init__(self):
        self.__movies = {}
        self.__file_name = "data/movies.bin"
        self.__load_file()

    def __load_file(self):
        try:
            read_file = open(self.__file_name, "rb")
            self.__movies = pickle.load(read_file)
            read_file.close()
        except EOFError:
            self.__movies = {}
    def __save_file(self):
        file_write = open(self.__file_name, "wb")
        pickle.dump(self.__movies, file_write)
        file_write.close()

    def add_movie(self, movie):
        if movie.GetID() in self.__movies:
            raise RepositoryException("Movie with this ID already exists !")
        self.__movies[movie.GetID()] = movie
        self.__save_file()

    def delete_movie(self, movie_id):
        if movie_id in self.__movies.keys():
            self.__movies.pop(movie_id)
            self.__save_file()
        else:
            raise RepositoryException("Movie doesn't exist !")
    def update_movie(self, movie_id, new_movie_title):
        if movie_id in self.__movies.keys():
            if new_movie_title != "":
                self.__movies[movie_id].SetTitle(new_movie_title)
            else:
                raise RepositoryException("Invalid new movie title !")
            self.__save_file()
        else:
            raise RepositoryException("Movie with this ID doesn't exist !")
    def get_all(self):
        return self.__movies
    def find_one_movie(self, movie_id):
        if movie_id in self.__movies:
            return self.__movies[movie_id]
        raise RepositoryException("The movie was not found !")