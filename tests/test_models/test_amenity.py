#!/usr/bin/python3
""" amenity tests """
import os
import unittest
import pycodestyle
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel, Base


class Test_Amenity(unittest.TestCase):
    """ tests for Amenity subclass of BaseModel """
    @classmethod
    def setUp(self):
        """ preparation method to be performed before each test """
        self.amenity1 = Amenity(name='test')
        self.amenity2 = Amenity(name='water')
        self.amenity3 = Amenity(**self.amenity1.to_dict())
        storage.save()

    @classmethod
    def tearDown(self):
        """ cleanup method to be performed following each test """
        del self.amenity1
        del self.amenity2
        del self.amenity3
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_doc_string(self):
        """ tests module docstring """
        self.assertTrue(len(Amenity.__doc__) > 0)

    def test_pycodestyle(self):
        """ tests module pycodestyle formatting standard compliance """
        style = pycodestyle.StyleGuide(quiet=True)
        self.assertEqual(
            style.check_files(['models/amenity.py']).total_errors,
            0,
            "Found code style errors (and warnings)."
        )

    def test_class_attribute_initialization(self):
        """ verifies attributes initialized with correct value & type """
        self.assertEqual(type(self.amenity1.name), str)
        self.assertEqual(type(self.amenity2.name), str)
        self.assertEqual(type(self.amenity3.name), str)
        self.assertEqual(self.amenity1.name, "test")
        self.assertEqual(self.amenity2.name, "water")
        self.assertEqual(self.amenity3.name, "test")

    def test_type_subclass(self):
        """ tests correct type/subclass heirarchy """
        self.assertEqual(type(self.amenity1), Amenity)
        self.assertTrue(isinstance(self.amenity1, Amenity))
        self.assertTrue(issubclass(self.amenity1.__class__, BaseModel))
        self.assertTrue(issubclass(self.amenity1.__class__, Base))


if __name__ == "__main__":
    unittest.main()
