import pickle
import os

from src.repository.ClientRepository import ClientRepository


class ClientRepositoryBinary(ClientRepository):
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

    def add_client(self, client):
        super().add_client(client)
        self.__save_file()

    def delete_client(self, client_id):
        super().delete_client(client_id)
        self.__save_file()

    def update_client(self, client_id, new_client_name):
        super().update_client(client_id,new_client_name)
        self.__save_file()

    def get_all(self):
        return super().get_all()
    def find_one_client(self, client_id):
        return super().find_one_client(client_id)
