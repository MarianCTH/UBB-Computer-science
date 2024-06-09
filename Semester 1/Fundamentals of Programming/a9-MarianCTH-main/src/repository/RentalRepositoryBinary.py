import pickle
import os
from src.repository.RentalRepository import RentalRepository

class RentalRepositoryBinary(RentalRepository):
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

    def add_rental(self, rental):
        super().add_rental(rental)
        self.__save_file()
    def delete_rental(self, rental_id):
        super().delete_rental(rental_id)
        self.__save_file()
    def update_rental(self, rental_id):
        super().update_rental(rental_id)
        self.__save_file()
    def get_all(self):
        return super().get_all()