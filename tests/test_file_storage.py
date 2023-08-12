import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_new(self):
        obj = BaseModel()
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.storage.new(obj)
        self.assertEqual(self.storage._FileStorage__objects[key], obj)

    def test_save(self):
        obj = BaseModel()
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.storage.new(obj)
        self.storage.save()
        with open(FileStorage._FileStorage__file_path, "r") as file:
            data = file.read()
            self.assertTrue(key in data)

    def test_reload(self):
        obj = BaseModel()
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.storage.new(obj)
        self.storage.save()
        del self.storage
        new_storage = FileStorage()
        new_storage.reload()
        self.assertTrue(key in new_storage._FileStorage__objects)

    def test_reload_non_existent_file(self):
        self.storage.reload()

    def test_reload_invalid_data(self):
        with open(FileStorage._FileStorage__file_path, "w") as file:
            file.write("invalid json")
        self.assertRaises(ValueError, self.storage.reload)

    def test_reload_with_class_import_error(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        del self.storage
        with open(FileStorage._FileStorage__file_path, "r") as file:
            data = file.read()
        # Modify the class name to cause an ImportError during eval
        modified_data = data.replace("BaseModel", "NonExistentClass")
        with open(FileStorage._FileStorage__file_path, "w") as file:
            file.write(modified_data)
        with self.assertRaises(NameError):
            new_storage = FileStorage()
            new_storage.reload()


if __name__ == "__main__":
    unittest.main()
