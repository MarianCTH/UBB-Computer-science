import pickle
from src.repository.repository import Repository

class BinaryRepository(Repository):
    def __init__(self):
        super().__init__()
        self.__file_name = "students.bin"
        self.load_file()

    def load_file(self):
        with open(self.__file_name, "rb") as file:
            try:
                entities = pickle.load(file)
                super().save_entities(entities)
            except EOFError:
                return []
    def save_file(self):
        with open(self.__file_name, "wb") as file:
            pickle.dump(super().get_all(), file)
    def add_student(self, student):
        super().add_student(student)
        self.save_file()
    def delete_student(self, student_id):
        super().delete_student(student_id)
        self.save_file()
    def get_all(self):
        return super().get_all()
    def find_one_student(self, student_id):
        return super().find_one_student(student_id)

