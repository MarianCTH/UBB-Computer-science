class Client:
    def __init__(self, client_id, name):
        self.__client_id = client_id
        self.__name = name

    def __str__(self):
       return f"[ID: {self.__client_id}] {self.__name}"

    def GetID(self):
        return self.__client_id

    def GetName(self):
        return self.__name

    def SetID(self, new_client_id):
        self.__client_id = new_client_id

    def SetName(self, new_client_name):
        self.__name = new_client_name

