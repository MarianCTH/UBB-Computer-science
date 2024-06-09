from src.repository.repository import Repository
import json

class JSONRepository(Repository):
    def __init__(self):
        super().__init__()
        self.__file_name = "students.json"
        self.load_file()

    def load_file(self):
        with open(self.__file_name, "r") as file:
            data = file.read()
            entities = json.loads(data)
            super().save_entities(entities)
    def save_file(self):
        with open(self.__file_name, "w") as file:
            serialized_data = {
                key: student.toDict() for key, student in (super().get_all()).items()
            }
            file.write(json.dumps(serialized_data, indent=2))
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
