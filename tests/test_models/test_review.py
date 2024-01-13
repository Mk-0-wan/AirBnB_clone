#!usr/bin/python3
"""All the test_cases for the city model class"""
import pep8
import unittest
import datetime
from models.review import Review


class TestModel(unittest.TestCase):
    """Test cases for all the base_model class and its methods"""

    def test_documentation(self):
        """Checking doctstring for all the class methods exists"""
        self.assertIsNotNone(Review.__doc__)

    def test_city_attributes(self):
        """Checking for all the valid attributes"""
        obj = Review()
        obj.place_id = "ALX-CODE-STREET"
        obj.user_id = "332-322-mk-33"
        obj.text = "root"
        self.assertTrue(hasattr(obj, "place_id"))
        self.assertTrue(hasattr(obj, "user_id"))
        self.assertFalse(hasattr(obj, "state_id"))
        self.assertTrue(hasattr(obj, "text"))
        self.assertEqual(obj.__dict__["place_id"], "ALX-CODE-STREET")
        self.assertEqual(obj.created_at, obj.updated_at)
        self.assertEqual(type(obj.updated_at), type(datetime.datetime.now()))

    def test_pycodestyle(self):
        """Testing for pycodestyle implementation"""
        pycode_pass = pep8.StyleGuide(quite=True)
        record = pycode_pass.check_files(
                ['./models/review.py',
                 './tests/test_models/test_review.py'])
        self.assertEqual(record.total_errors, 0, "errors found")

    def test_string_format_method(self):
        """Checking for the string format matches the expected criteria"""
        obj = Review()
        self.assertEqual(obj.__str__(),
                         f"[{type(obj).__name__}] ({obj.id}) {obj.__dict__}")
        k = obj.to_dict()
        cp = Review(**k)
        self.assertEqual(cp.__str__(),
                         f"[{cp.__class__.__name__}] ({cp.id}) {cp.__dict__}")
        self.assertTrue(obj.__str__(), cp.__str__())
        cp.name = "drihman"
        self.assertNotEqual(obj.__str__(), cp.__str__())
