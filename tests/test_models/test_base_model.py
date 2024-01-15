#!/usr/bin/python3
"""All the test_cases for the base model class"""
import pep8
import unittest
import datetime
from models.base_model import BaseModel as bm
from models.engine.file_storage import FileStorage as fs


class TestModel(unittest.TestCase):
    """Test cases for all the base_model class and its methods"""
    def setUp(self):
        """Setup Classes which will allow me to avoid repetition of classes"""
        self.bl = [bm(), bm()]

    def test_documentation(self):
        """Checking doctstring for all the class methods exists"""
        self.assertIsNotNone(bm.__doc__)
        self.assertIsNotNone(bm.save.__doc__)
        self.assertIsNotNone(bm.to_dict.__doc__)
        self.assertIsNotNone(bm.__str__.__doc__)
        self.assertIsNotNone(bm.__init__.__doc__)

    def test_base_model_methods(self):
        """Checking if all base model methods exist"""
        self.assertTrue(hasattr(bm, "save"))
        self.assertTrue(hasattr(bm, "__init__"))
        self.assertTrue(hasattr(bm, "__str__"))
        self.assertTrue(hasattr(bm, "to_dict"))

    def test_base_model_attribute(self):
        """Testing for all the attributes instances"""
        obj = self.bl[0]
        obj.new_name = "Max"
        self.assertTrue(hasattr(obj, "new_name"))
        self.assertFalse(hasattr(obj, "age"))
        self.assertNotEqual(obj.__dict__["new_name"], "Vax")
        self.assertEqual(type(obj.updated_at), type(datetime.datetime.now()))

    def test_base_save(self):
        """Testing the base model save method"""
        obj = self.bl[0]
        obj.name = "Pax"
        old_id = obj.id
        before = obj.updated_at
        dct_len = len(obj.__dict__)
        obj.save()
        after = obj.updated_at
        self.assertNotEqual(before, after)
        self.assertTrue(obj.id, old_id)
        self.assertTrue(dct_len, len(obj.__dict__))

    def test_base_to_dict(self):
        """Checking the base model to_dict method"""
        obj = self.bl[0]
        dct = obj.to_dict()
        self.assertTrue(type(dct), dict)
        self.assertTrue(type(dct["created_at"]), str)
        self.assertTrue(type(dct["updated_at"]), str)
        self.assertTrue(hasattr(dct, "__class__"))
        self.assertTrue(dct["__class__"], obj.__class__.__name__)
        self.assertTrue(obj.id, dct["id"])

    def test_base_model_kwargs(self):
        """Test for kwargs arguments when they are passed"""
        obj = self.bl[0]
        old_id = obj.id
        attr = obj.to_dict()
        new_obj = bm(**attr)

        self.assertNotEqual(obj, new_obj)
        self.assertTrue(new_obj.id, old_id)
        self.assertEqual(obj.created_at, new_obj.created_at)

        new_obj.stat = "Good"
        new = new_obj.to_dict()
        cp = bm(**new)
        self.assertTrue(hasattr(cp, "stat"))
        self.assertTrue(cp, new_obj)
        self.assertTrue(type(cp.created_at), datetime)
        self.assertIsNot(cp, new_obj)

    def test_string_format_method(self):
        """Checking for the string format matches the expected criteria"""
        obj = self.bl[0]
        self.assertEqual(obj.__str__(),
                         f"[{type(obj).__name__}] ({obj.id}) {obj.__dict__}")

        k = obj.to_dict()
        cp = bm(**k)
        self.assertEqual(cp.__str__(),
                         f"[{cp.__class__.__name__}] ({cp.id}) {cp.__dict__}")
        self.assertTrue(obj.__str__(), cp.__str__())

        cp.name = "drihman"
        self.assertNotEqual(obj.__str__(), cp.__str__())

    def test_pycodestyle(self):
        """Testing for pycodestyle implementation"""
        pycode_pass = pep8.StyleGuide(quite=True)
        record = pycode_pass.check_files(
                ['./models/base_model.py',
                 './tests/test_models/test_base_model.py'])
        self.assertEqual(record.total_errors, 0, "errors found")

    def test_updated_at_and_created_at(self):
        """Checking for all the validity test of the attributes"""
        self.assertNotEqual(self.bl[0].updated_at, self.bl[1].updated_at)
        self.assertNotEqual(self.bl[0].created_at, self.bl[1].created_at)
        old = self.bl[0]
        new = self.bl[0].save()
        self.assertNotEqual(old, new)

    def test_id_of_different_instances(self):
        """Testing the ids of two different instances"""
        self.assertTrue(self.bl[0].id, str)
        self.assertTrue(self.bl[1].id, str)
        self.assertNotEqual(self.bl[0].id, self.bl[1].id)

    def tearDown(self):
        """Cleaning up all that not necessary needed"""
        for _x in self.bl:
            del fs().all()[f"{_x.__class__.__name__}.{_x.id}"]
        fs().save()


if __name__ == '__main__':
    unittest.main()
