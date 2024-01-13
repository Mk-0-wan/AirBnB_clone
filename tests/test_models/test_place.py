#!/usr/bin/python3
"""All the test_cases for the city model class"""
import pep8
import unittest
import datetime
from models.place import Place
from models.city import City
from models.user import User
from models.amenity import Amenity


class TestModel(unittest.TestCase):
    """Test cases for all the base_model class and its methods"""
    user = User()
    city = City()
    amenity = Amenity()

    def test_documentation(self):
        """Checking doctstring for all the class methods exists"""
        self.assertIsNotNone(Place.__doc__)

    def test_city_attributes(self):
        """Checking for all the valid attributes"""
        obj = Place()
        obj.name = "victor"
        obj.city_id = self.city.__dict__["id"]
        obj.user_id = self.user.__dict__["id"]
        obj.description = "Just a bunch of text"
        obj.number_rooms = 22
        obj.number_bathrooms = 22
        obj.max_guest = 22
        obj.price_by_night = 22
        obj.latitude = 0.0236
        obj.longitude = 37.9062
        obj.amenity_ids = [self.amenity.id]

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
        self.assertEqual(obj.__dict__["city_id"], self.city.id)
        self.assertEqual(obj.user_id, self.user.id)
        self.assertTrue(type(obj.description), str)
        self.assertTrue(type(obj.latitude), float)
        self.assertTrue(type(obj.longitude), float)
        self.assertTrue(type([
            obj.number_rooms,
            obj.number_bathrooms,
            obj.max_guest,
            obj.price_by_night]), int)
        self.assertTrue(type(obj.amenity_ids), list)
        self.assertNotEqual(obj.created_at, obj.updated_at)
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
        obj = Place()
        self.assertEqual(obj.__str__(),
                         f"[{type(obj).__name__}] ({obj.id}) {obj.__dict__}")

        k = obj.to_dict()
        cp = Place(**k)
        self.assertEqual(cp.__str__(),
                         f"[{cp.__class__.__name__}] ({cp.id}) {cp.__dict__}")
        self.assertTrue(obj.__str__(), cp.__str__())

        cp.name = "drihman"
        self.assertNotEqual(obj.__str__(), cp.__str__())
