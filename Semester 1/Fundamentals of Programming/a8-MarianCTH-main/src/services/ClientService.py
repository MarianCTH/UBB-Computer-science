from src.domain.ClientDomain import Client
from src.exceptions.RepositoryExceptions import RepositoryException

class ClientService:
    def __init__(self, client_validator, client_repository):
        self.__validator = client_validator
        self.__repository = client_repository

    def add_client(self, client_id, name):
        new_client = Client(client_id, name)
        self.__validator.ValidateNewClient(new_client)
        self.__repository.add_client(new_client)

    def delete_client(self, client_id):
        self.__repository.delete_client(client_id)

    def update_client(self, client_id, new_client_name):
        self.__repository.update_client(client_id, new_client_name)

    def list_clients(self):
        clients = self.__repository.get_all()
        if len(clients) > 0:
            for key, client_object in clients.items():
                print(client_object)
        else:
            raise RepositoryException("There are no clients in the list !")

    def search(self, client_id, client_name):
        clients = self.__repository.get_all()
        found_clients = []
        if client_id:
            return self.__repository.find_one_client(client_id)
        elif client_name:
            for id, client in clients.items():
                if client_name.lower() in (client.GetName()).lower():
                    found_clients.append(client)
            if len(found_clients) > 0:
                return found_clients
            else:
                raise RepositoryException("There are no clients with this name !")

    def find_one_client(self, client_id):
        return self.__repository.find_one_client(client_id)