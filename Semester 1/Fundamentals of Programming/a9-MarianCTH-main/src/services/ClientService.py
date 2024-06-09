from src.domain.ClientDomain import Client
from src.exceptions.RepositoryExceptions import RepositoryException
from src.services.UndoRedoService import FunctionCall, Operation

class ClientService:
    def __init__(self, client_validator, client_repository, undo_redo_service):
        self.__validator = client_validator
        self.__repository = client_repository
        self.__undo_redo = undo_redo_service

    def add_client(self, client_id, name):
        new_client = Client(client_id, name)
        self.__validator.ValidateNewClient(new_client)
        self.__repository.add_client(new_client)

        redo = FunctionCall(self.add_client, client_id, name)
        undo = FunctionCall(self.delete_client, client_id)
        operation = Operation(redo, undo)
        self.__undo_redo.recordOperation(operation)

    def delete_client(self, client_id):
        get_name = self.find_one_client(client_id).GetName()

        self.__repository.delete_client(client_id)

        redo = FunctionCall(self.delete_client, client_id)
        undo = FunctionCall(self.add_client, client_id, get_name)
        operation = Operation(redo, undo)
        self.__undo_redo.recordOperation(operation)

    def update_client(self, client_id, new_client_name):
        last_name = self.find_one_client(client_id).GetName()

        self.__repository.update_client(client_id, new_client_name)

        redo = FunctionCall(self.update_client, client_id, new_client_name)
        undo = FunctionCall(self.update_client, client_id, last_name)
        operation = Operation(redo, undo)
        self.__undo_redo.recordOperation(operation)

    def list_clients(self):
        clients = self.__repository.get_all()
        if len(clients) > 0:
            return clients.items()
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