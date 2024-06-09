from src.errors.validator_errors import ValidatorExceptions

class StudentValidator:
    def __init__(self):
        pass
    def validate_new_student(self, student):
        errors = ""

        if student.getID() < 0:
            errors += "Invalid ID !\n"
        if student.getName() == "":
            errors += "Invalid name !\n"
        if student.getGroup() < 0:
            errors += "Invalid group !\n"

        if errors != "":
            raise ValidatorExceptions(errors)
