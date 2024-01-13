#!/usr/bin/python3
"""All the test_cases for the city model class"""
import pep8
import unittest
import datetime
from models.user import User


class TestModel(unittest.TestCase):
    """Test cases for all the base_model class and its methods"""

    def test_documentation(self):
        """Checking doctstring for all the class methods exists"""
        self.assertIsNotNone(User.__doc__)

    def test_city_attributes(self):
        """Checking for all the valid attributes"""
        obj = User()
        obj.first_name = "victor"
        obj.last_name = "mk"
        obj.password = "root"
        obj.email = "mklinux@gmail.com"
        self.assertTrue(hasattr(obj, "last_name"))
        self.assertTrue(hasattr(obj, "first_name"))
        self.assertFalse(hasattr(obj, "state_id"))
        self.assertTrue(hasattr(obj, "email"))
        self.assertTrue(hasattr(obj, "password"))
        self.assertNotEqual(obj.__dict__["last_name"], "Vax")
        self.assertNotEqual(obj.created_at, obj.updated_at)
        self.assertEqual(type(obj.updated_at), type(datetime.datetime.now()))

    def test_pycodestyle(self):
        """Testing for pycodestyle implementation"""
        pycode_pass = pep8.StyleGuide(quite=True)
        record = pycode_pass.check_files(
                ['./models/user.py',
                 './tests/test_models/test_user.py'])
        self.assertEqual(record.total_errors, 0, "errors found")

    def test_string_format_method(self):
        """Checking for the string format matches the expected criteria"""
        obj = User()
        self.assertEqual(obj.__str__(),
                         f"[{type(obj).__name__}] ({obj.id}) {obj.__dict__}")
        k = obj.to_dict()
        cp = User(**k)
        self.assertEqual(cp.__str__(),
                         f"[{cp.__class__.__name__}] ({cp.id}) {cp.__dict__}")
        self.assertTrue(obj.__str__(), cp.__str__())
        cp.name = "drihman"
        self.assertNotEqual(obj.__str__(), cp.__str__())
