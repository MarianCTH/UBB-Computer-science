import copy

from src.domain.student import Student
from src.errors.repository_errors import RepositoryExceptions


class Services:
    def __init__(self, validator, repository):
        self.__validator = validator
        self.__repository = repository
        self.__undo = []

    def add_student(self, id, name, group):
        student = Student(id, name, group)
        self.__validator.validate_new_student(student)
        try:
            self.__repository.find_one_student(id)
        except RepositoryExceptions:
            self.__undo.append(copy.deepcopy(self.__repository))
        self.__repository.add_student(student)

    def display_students(self):
        return self.__repository.get_all()

    def filter_students(self, group):
        students_to_remove = []
        students = self.__repository.get_all()

        for student in students.values():
            if student.getGroup() == group:
                students_to_remove.append(student.getID())

        if len(students_to_remove) > 0:
            self.__undo.append(copy.deepcopy(self.__repository))
        for id_student in students_to_remove:
            self.__repository.delete_student(id_student)

    def undo_last_operation(self):
        if len(self.__undo) > 0:
            self.__repository = self.__undo.pop()
