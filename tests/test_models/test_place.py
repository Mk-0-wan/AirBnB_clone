#!/usr/bin/python3
"""All the test_cases for the city model class"""
import pep8
import unittest
import datetime
from models.place import Place
from models.engine.file_storage import FileStorage as fs


class TestModel(unittest.TestCase):
    """Test cases for all the base_model class and its methods"""
    def setUp(self):
        """Setup Classes which will allow me to avoid repetition of classes"""
        self.bsl = [Place(), Place()]

    def test_documentation(self):
        """Checking doctstring for all the class methods exists"""
        self.assertIsNotNone(self.bsl[0].__doc__)

    def test_city_attributes(self):
        """Checking for all the valid attributes"""
        obj = self.bsl[0]
        obj.name = "victor"
        obj.city_id = "29f8b803-9b68-4623-87cc-be930005d53f"
        obj.user_id = "462e0218-96b6-4116-bda5-878bd58a5aa4"
        obj.description = "Just a bunch of text"
        obj.number_rooms = 22
        obj.number_bathrooms = 22
        obj.max_guest = 22
        obj.price_by_night = 22
        obj.latitude = 0.0236
        obj.longitude = 37.9062
        obj.amenity_ids = ["9eff232a-c739-4800-bf33-da61ea766c8f",
                           "462e0218-96b6-4116-bda5-878bd58a5aa4"]

        self.assertTrue(hasattr(obj, "name"))
        self.assertTrue(hasattr(obj, "city_id"))
        self.assertTrue(hasattr(obj, "user_id"))
        self.assertTrue(hasattr(obj, "amenity_ids"))
        self.assertTrue(hasattr(obj, "description"))
        self.assertTrue(hasattr(obj, "number_rooms"))
        self.assertTrue(hasattr(obj, "number_bathrooms"))
        self.assertTrue(hasattr(obj, "max_guest"))
        self.assertTrue(hasattr(obj, "price_by_night"))
        self.assertTrue(hasattr(obj, "latitude"))
        self.assertTrue(hasattr(obj, "longitude"))
        self.assertTrue(type(obj.description), str)
        self.assertTrue(type(obj.latitude), float)
        self.assertTrue(type(obj.longitude), float)
        self.assertTrue(type([
            obj.number_rooms,
            obj.number_bathrooms,
            obj.max_guest,
            obj.price_by_night]), int)
        self.assertTrue(type(obj.amenity_ids), list)
        self.assertEqual(type(obj.updated_at), type(datetime.datetime.now()))

    def test_pycodestyle(self):
        """Testing for pycodestyle implementation"""
        pycode_pass = pep8.StyleGuide(quite=True)
        record = pycode_pass.check_files(
                ['./models/place.py',
                 './tests/test_models/test_place.py'])
        self.assertEqual(record.total_errors, 0, "errors found")

    def test_string_format_method(self):
        """Checking for the string format matches the expected criteria"""
        obj = self.bsl[0]
        self.assertEqual(obj.__str__(),
                         f"[{type(obj).__name__}] ({obj.id}) {obj.__dict__}")

        k = obj.to_dict()
        cp = Place(**k)
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
        """Cleaning up all that not necessary needed"""
        for _x in self.bsl:
            del fs().all()[f"{_x.__class__.__name__}.{_x.id}"]
        fs().save()


if __name__ == '__main__':
    unittest.main()
