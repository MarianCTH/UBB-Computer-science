from .menu_options import *
from src.errors.repository_errors import RepositoryExceptions
from src.errors.validator_errors import ValidatorExceptions

class UI:
    def __init__(self, service):
        self.__service = service
    def printMenuOptions(self):
        for key, option in options.items():
            print(f"{key} : {option}")
    def getUserChoice(self):
        return input("Please enter your choice:\n>> ")
    def initialize(self):
        self.printMenuOptions()

        while True:
            user_choice = self.getUserChoice()
            if options[user_choice] == ADD_A_STUDENT:
                try:
                    new_student_id = int(input("ID: "))
                    new_student_name = input("Name: ")
                    new_student_group = int(input("Group: "))
                    self.__service.add_student(new_student_id, new_student_name, new_student_group)
                    print("Student added successfully !")
                except ValueError as ve:
                    print(f"Value error: {ve}")
                except RepositoryExceptions as re:
                    print(f"Repository error: {re}")
                except ValidatorExceptions as ve:
                    print(f"Validator error: {ve}")
            elif options[user_choice] == DISPLAY_STUDENT_LIST:
                for s in self.__service.display_students().values():
                    print(s)
            elif options[user_choice] == FILTER_STUDENTS:
                try:
                    group = int(input("The group you want to delete: "))
                    self.__service.filter_students(group)
                except ValueError as ve:
                    print(f"Value error: {ve}")
                except RepositoryExceptions as re:
                    print(f"Repository error: {re}")
            elif options[user_choice] == UNDO:
                self.__service.undo_last_operation()