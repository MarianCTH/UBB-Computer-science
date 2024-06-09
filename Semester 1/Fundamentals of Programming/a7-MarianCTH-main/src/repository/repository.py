from src.errors.repository_errors import RepositoryExceptions
class Repository:
    def __init__(self):
        self.__entities = {}

    def add_student(self, student):
        if student.getID() in self.__entities:
            raise RepositoryExceptions("Student already exists !")
        else:
            self.__entities[student.getID()] = student

    def delete_student(self, student_id):
        if student_id in self.__entities:
            self.__entities.pop(student_id)
        else:
            raise RepositoryExceptions("Student doesn't exist !")

    def get_all(self):
        return self.__entities

    def find_one_student(self, student_id):
        if student_id in self.__entities:
            return self.__entities[student_id]
        raise RepositoryExceptions("No student found !")

    def save_entities(self, entities):
        self.__entities = entities
