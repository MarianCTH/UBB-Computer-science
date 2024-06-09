from src.exceptions.ValidatorException import ValidatorException
class ClientValidator:
    def __init__(self):
        pass
    def ValidateNewClient(self, client):
        errors = ""
        if client.GetID() < 0:
            errors += "Invalid ID !\n"
        if client.GetName() == "":
            errors += "Invalid name !\n"
        if errors != "":
            raise ValidatorException(errors)