#!usr/bin/python3
"""All the test_cases for the city model class"""
import pep8
import unittest
import datetime
from models.review import Review
from models.engine.file_storage import FileStorage as fs


class TestModel(unittest.TestCase):
    """Test cases for all the base_model class and its methods"""
    def setUp(self):
        """Setup Classes which will allow me to avoid repetition of classes"""
        self.bsl = [Review(), Review()]

    def test_documentation(self):
        """Checking doctstring for all the class methods exists"""
        self.assertIsNotNone(Review.__doc__)

    def test_city_attributes(self):
        """Checking for all the valid attributes"""
        obj = self.bsl[0]
        obj.place_id = "ALX-CODE-STREET"
        obj.user_id = "332-322-mk-33"
        obj.text = "root"
        self.assertTrue(hasattr(obj, "place_id"))
        self.assertTrue(hasattr(obj, "user_id"))
        self.assertFalse(hasattr(obj, "state_id"))
        self.assertTrue(hasattr(obj, "text"))
        self.assertEqual(obj.__dict__["place_id"], "ALX-CODE-STREET")
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
        obj = self.bsl[1]
        self.assertEqual(obj.__str__(),
                         f"[{type(obj).__name__}] ({obj.id}) {obj.__dict__}")
        k = obj.to_dict()
        cp = Review(**k)
        self.assertEqual(cp.__str__(),
                         f"[{cp.__class__.__name__}] ({cp.id}) {cp.__dict__}")
        self.assertTrue(obj.__str__(), cp.__str__())
        cp.name = "drihman"
        self.assertNotEqual(obj.__str__(), cp.__str__())

    def test_updated_at_and_created_at(self):
        """Checking for all the validity test of the attributes"""
        self.assertNotEqual(self.bsl[0].updated_at, self.bsl[1].updated_at)
        self.assertNotEqual(self.bsl[0].created_at, self.bsl[1].created_at)
        old = self.bsl[0]
        new = self.bsl[0].save()
        self.assertNotEqual(old, new)

    def test_id_of_different_instances(self):
        """Testing the ids of two different instances"""
        self.assertTrue(self.bsl[0].id, str)
        self.assertTrue(self.bsl[1].id, str)
        self.assertNotEqual(self.bsl[0].id, self.bsl[1].id)

    def tearDown(self):
        """Cleaning up all the test cases that are not necessary needed"""
        for _x in self.bsl:
            del fs().all()[f"{_x.__class__.__name__}.{_x.id}"]
        fs().save()


if __name__ == '__main__':
    unittest.main()
