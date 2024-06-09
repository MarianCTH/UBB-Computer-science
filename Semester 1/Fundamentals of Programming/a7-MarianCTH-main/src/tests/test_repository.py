from unittest import TestCase
from src.domain.student import Student
from src.repository.repository import Repository
from src.errors.repository_errors import RepositoryExceptions
class TestRepository(TestCase):
    def setUp(self):
        self.__repository = Repository()

    def test_add_student(self):
        student1 = Student('1', "Marian", '912')
        self.__repository.add_student(student1)
        self.assertEqual(len(self.__repository.get_all()), 1, "There should be one student in the repository!")

        student2 = Student('1', "Test", '915')
        with self.assertRaises(RepositoryExceptions):
            self.__repository.add_student(student2)

    def test_get_all(self):
        student1 = Student('1', "Marian", '913')
        self.__repository.add_student(student1)
        students = self.__repository.get_all()
        self.assertEqual(students["1"].getName(), "Marian", "Error: get_all()")

    def test_delete_student(self):
        student1 = Student('1', "Marian", "912")
        self.__repository.add_student(student1)
        self.assertRaises(RepositoryExceptions, self.__repository.delete_student, "2")
        self.__repository.delete_student("1")
        self.assertEqual(len(self.__repository.get_all()), 0, "There should be 0 students in the repository")