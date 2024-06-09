import pickle
import os
from src.repository.MovieRepository import MovieRepository

class MovieRepositoryBinary(MovieRepository):
    def __init__(self, file_path):
        super().__init__()
        data_directory = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
        self.__file_name = os.path.join(data_directory, file_path)
        self.__load_file()

    def __load_file(self):
        try:
            read_file = open(self.__file_name, "rb")
            super().set_all(pickle.load(read_file))
            read_file.close()
        except EOFError:
            super().set_all({})
    def __save_file(self):
        file_write = open(self.__file_name, "wb")
        pickle.dump(super().get_all(), file_write)
        file_write.close()

    def add_movie(self, movie):
        super().add_movie(movie)
        self.__save_file()

    def delete_movie(self, movie_id):
        super().delete_movie(movie_id)
        self.__save_file()
    def update_movie(self, movie_id, new_movie_title):
        super().update_movie(movie_id,new_movie_title)
        self.__save_file()
    def get_all(self):
        return super().get_all()
    def find_one_movie(self, movie_id):
        return super().find_one_movie(movie_id)
