#!usr/bin/python3
"""All the test_cases for the city model class"""
import pep8
import unittest
import datetime
from models.city import City


class TestModel(unittest.TestCase):
    """Test cases for all the base_model class and its methods"""

    def test_documentation(self):
        """Checking doctstring for all the class methods exists"""
        self.assertIsNotNone(City.__doc__)

    def test_city_attributes(self):
        """Checking for all the valid attributes"""
        obj = City()
        obj.name = "victor"
        obj.state_id = "11-11-111"
        self.assertTrue(hasattr(obj, "name"))
        self.assertTrue(hasattr(obj, "state_id"))
        self.assertNotEqual(obj.__dict__["name"], "Vax")
        self.assertEqual(obj.created_at, obj.updated_at)
        self.assertEqual(type(obj.updated_at), type(datetime.datetime.now()))

    def test_pycodestyle(self):
        """Testing for pycodestyle implementation"""
        pycode_pass = pep8.StyleGuide(quite=True)
        record = pycode_pass.check_files(
                ['./models/city.py',
                 './tests/test_models/test_city.py'])
        self.assertEqual(record.total_errors, 0, "errors found")

    def test_string_format_method(self):
        """Checking for the string format matches the expected criteria"""
        obj = City()
        self.assertEqual(obj.__str__(),
                         f"[{type(obj).__name__}] ({obj.id}) {obj.__dict__}")
        k = obj.to_dict()
        cp = City(**k)
        self.assertEqual(cp.__str__(),
                         f"[{cp.__class__.__name__}] ({cp.id}) {cp.__dict__}")
        self.assertTrue(obj.__str__(), cp.__str__())
        cp.name = "drihman"
        self.assertNotEqual(obj.__str__(), cp.__str__())
