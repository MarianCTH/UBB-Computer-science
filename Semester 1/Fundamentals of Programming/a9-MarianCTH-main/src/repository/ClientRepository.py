from src.exceptions.RepositoryExceptions import RepositoryException
class ClientRepository:
    def __init__(self):
        self.__clients = {}

    def add_client(self, client):
        if client.GetID() in self.__clients:
            raise RepositoryException("Client already exists !")
        self.__clients[client.GetID()] = client
    def delete_client(self, client_id):
        if client_id in self.__clients.keys():
            self.__clients.pop(client_id)
        else:
            raise RepositoryException("Client doesn't exist !")
    def update_client(self, client_id, new_client_name):
        if client_id in self.__clients.keys():
            if new_client_name != "":
                self.__clients[client_id].SetName(new_client_name)
            else:
                raise RepositoryException("Invalid new client name !")
        else:
            raise RepositoryException("Client doesn't exist !")
    def get_all(self):
        return self.__clients
    def set_all(self, new_clients):
        self.__clients = new_clients
    def find_one_client(self, client_id):
        if client_id in self.__clients:
            return self.__clients[client_id]
        raise RepositoryException("The client was not found !")