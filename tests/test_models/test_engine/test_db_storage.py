#!/usr/bin/python3
""" """
import unittest
from models.engine.db_storage import DBStorage


class Test_DatabaseStorage(unittest.TestCase):
    """ tests for DBStorage """
    def test_dbstorage(self):
        storage = DBStorage()
        self.assertIsInstance(storage, DBStorage)
        self.assertEqual(1, 1)
