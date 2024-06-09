from src.exceptions.RepositoryExceptions import RepositoryException
import pickle

class ClientRepository:
    def __init__(self):
        self.__clients = {}
        self.__file_name = "data/clients.bin"
        self.__load_file()

    def __load_file(self):
        try:
            read_file = open(self.__file_name, "rb")
            self.__clients = pickle.load(read_file)
            read_file.close()
        except EOFError:
            self.__clients = {}
    def __save_file(self):
        file_write = open(self.__file_name, "wb")
        pickle.dump(self.__clients, file_write)
        file_write.close()

    def add_client(self, client):
        if client.GetID() in self.__clients:
            raise RepositoryException("Client already exists !")
        self.__clients[client.GetID()] = client
        self.__save_file()
    def delete_client(self, client_id):
        if client_id in self.__clients.keys():
            self.__clients.pop(client_id)
            self.__save_file()
        else:
            raise RepositoryException("Client doesn't exist !")
    def update_client(self, client_id, new_client_name):
        if client_id in self.__clients.keys():
            if new_client_name != "":
                self.__clients[client_id].SetName(new_client_name)
            else:
                raise RepositoryException("Invalid new client name !")
            self.__save_file()
        else:
            raise RepositoryException("Client doesn't exist !")
    def get_all(self):
        return self.__clients
    def find_one_client(self, client_id):
        if client_id in self.__clients:
            return self.__clients[client_id]
        raise RepositoryException("The client was not found !")