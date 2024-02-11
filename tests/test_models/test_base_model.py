#!/usr/bin/python3
""" Unittests for the BaseModel Class models/base_model.py"""
import os
import models
import json
import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """This class contains unittests for the BaseModel class."""
    def setUp(self):
        """Method that sets up the cases for testing"""
        self.my_model = BaseModel()
        self.my_model.name = "My_First_Model"
        self.my_model.my_number = 89
        self.id = self.my_model.id
        self.type_1 = datetime.datetime
        self.my_model_json = self.my_model.to_dict()

    def tearDown(self):
        """Method that cleans tests"""
        del self.my_model

    def test_init_(self):
        """Method that tests the __init__ method in BaseModel"""
        self.assertIsInstance(self.my_model, BaseModel)

    def test_new_attribue(self):
        """Method that tests the saving of attributes"""
        self.assertEqual(self.my_model.name, "My_First_Model")
        self.assertEqual(self.my_model.my_number, 89)

    def test_id(self):
        """Method that tests the id generating"""
        self.assertEqual(self.id, self.my_model.id)

    def test_id_unique(self):
        """Method that tests if each BaseModel instance has a unique id."""
        base_model1 = BaseModel()
        base_model2 = BaseModel()
        self.assertNotEqual(base_model1.id, base_model2.id)

    def test_str_representation(self):
        """Method that tests the __str__ method of BaseModel."""
        base_model = BaseModel()
        str_repr = str(base_model)
        self.assertIn("[BaseModel]", str_repr)
        self.assertIn(base_model.id, str_repr)
        self.assertIn(str(base_model.__dict__), str_repr)

    def test_created_at(self):
        """Method that tests the type of created_at"""
        self.assertEqual(self.type_1, type(self.my_model.created_at))

    def test_to_dict_created_at_isoformat(self):
        self.assertEqual(self.my_model_json['created_at'],
                         self.my_model.created_at.isoformat())

    def test_to_dict_updated_at_isoformat(self):
        self.assertEqual(self.my_model_json['updated_at'],
                         self.my_model.updated_at.isoformat())

    def test_save_updates_updated_at(self):
        prev_updated_at = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(prev_updated_at, self.my_model.updated_at)

    def test_to_dict(self):
        self.assertEqual(self.my_model_json, self.my_model.to_dict())

    def test_to_dict_contains_correct_keys(self):
        keys = ['id', 'created_at', 'updated_at', '__class__']
        for key in keys:
            self.assertIn(key, self.my_model_json)

    def test_to_dict_returns(self):
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertIsInstance(base_model_dict, dict)
        self.assertIn("__class__", base_model_dict)
        self.assertEqual(base_model_dict["__class__"], "BaseModel")
        self.assertIn("id", base_model_dict)
        self.assertIn("created_at", base_model_dict)
        self.assertIn("updated_at", base_model_dict)


if __name__ == '__main__':
    unittest.main()
