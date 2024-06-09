import unittest
from src.domain.student import Student

class TestStudent(unittest.TestCase):
    def test_constructor(self):
        student = Student('1', 'John', '912')
        self.assertEqual(student.getID(), '1', "ID should be '1'")
        self.assertEqual(student.getName(), 'John', "Name should be 'John'")
        self.assertEqual(student.getGroup(), '912', "Group should be '912'")

    def test_str_method(self):
        student = Student('1', 'John', '912')
        expected_str = "1 : John (Group 912)"
        self.assertEqual(str(student), expected_str, "str method should return the expected string")

    def test_toDict_method(self):
        student = Student('1', 'John', '912')
        expected_dict = {'id': '1', 'name': 'John', 'group': '912'}
        self.assertEqual(student.toDict(), expected_dict, "toDict method should return the expected dictionary")

if __name__ == '__main__':
    unittest.main()
