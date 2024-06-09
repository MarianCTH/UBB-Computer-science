"""
Manage a list of students. Each student has an id (integer, unique), a name (string) and a group (positive integer). 
Provide the following features:
    - Add a student. Student data is read from the console.
    - Display the list of students.
    - Filter the list so that students in a given group (read from the console) are deleted from the list.
    - Undo the last operation that modified program data. This step can be repeated. The user can undo only those operations made during the current run of the program.
"""

from src.repository.memory_repository import MemoryRepository
from src.repository.json_repository import JSONRepository
from src.repository.binary_repository import BinaryRepository
from src.services.services import Services
from src.ui.ui import UI
from src.validators.student_validator import StudentValidator

def main():
    repository = MemoryRepository()
    validator = StudentValidator()
    services = Services(validator, repository)
    user_interface = UI(services)
    user_interface.initialize()

if __name__ == '__main__':
    main()