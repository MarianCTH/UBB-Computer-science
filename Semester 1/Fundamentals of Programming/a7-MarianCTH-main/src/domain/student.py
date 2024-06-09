class Student:
    def __init__(self, id, name, group):
        self.__id = id
        self.__name = name
        self.__group = group

    def __str__(self):
        return f"{self.__id} : {self.__name} (Group {self.__group})"

    def getID(self):
        return self.__id

    def getName(self):
        return self.__name

    def getGroup(self):
        return self.__group

    def toDict(self):
        return {
            'id': self.__id,
            'name': self.__name,
            'group': self.__group
        }
