#!/usr/bin/python3

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_init_with_kwargs(self):
        data = {
            "id": "123",
            "created_at": "2023-08-01T12:00:00",
            "updated_at": "2023-08-01T13:00:00"
        }
        instance = BaseModel(**data)
        self.assertEqual(instance.id, "123")
        self.assertEqual(instance.created_at, datetime(2023, 8, 1, 12, 0, 0))
        self.assertEqual(instance.updated_at, datetime(2023, 8, 1, 13, 0, 0))

    def test_init_without_kwargs(self):
        instance = BaseModel()
        self.assertIsNotNone(instance.id)
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)

    def test_str_representation(self):
        instance = BaseModel()
        str_repr = str(instance)
        self.assertIn("[BaseModel]", str_repr)
        self.assertIn(instance.id, str_repr)

    def test_save_method(self):
        instance = BaseModel()
        original_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(original_updated_at, instance.updated_at)

    def test_to_dict_method(self):
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertIsInstance(instance_dict, dict)
        self.assertEqual(instance_dict["__class__"], "BaseModel")
        self.assertIn("id", instance_dict)
        self.assertIn("created_at", instance_dict)
        self.assertIn("updated_at", instance_dict)

    def test_to_dict_created_at_format(self):
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertTrue("created_at" in instance_dict)
        self.assertIsInstance(instance_dict["created_at"], str)
        datetime.strptime(instance_dict["created_at"], "%Y-%m-%dT%H:%M:%S")

    def test_to_dict_updated_at_format(self):
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertTrue("updated_at" in instance_dict)
        self.assertIsInstance(instance_dict["updated_at"], str)
        datetime.strptime(instance_dict["updated_at"], "%Y-%m-%dT%H:%M:%S")

    def test_new_instance_unique_id(self):
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_init_with_invalid_created_at(self):
        with self.assertRaises(ValueError):
            data = {"created_at": "invalid_datetime_format"}
            instance = BaseModel(**data)
            print(instance)

    def test_init_with_invalid_updated_at(self):
        with self.assertRaises(ValueError):
            data = {"updated_at": "invalid_datetime_format"}
            instance = BaseModel(**data)
            print(instance)


if __name__ == '__main__':
    unittest.main()
