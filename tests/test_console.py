import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import os


class TestHBNBCommand(unittest.TestCase):
    test_random_attributes = {
        "strfoo": "barfoo",
        "intfoo": 248,
        "floatfoo": 9.8
    }

    attribute_values = {
        str: "foobar108",
        int: 1008,
        float: 1.08
    }

    reset_values = {
        str: "",
        int: 0,
        float: 0.0
    }
    
    def setUp(self):
        """Sets up test cases."""
        self.console = HBNBCommand()
        if os.path.isfile("file.json"):
            os.remove("file.json")
        self.resetStorage()

    def tearDown(self):
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_help(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("help")
        expected_output = """
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

"""
        self.assertEqual(expected_output, file.getvalue())


    
    def test_help_show(self):
        with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("help show")
        expected_output = """string representation of object\n"""
        self.assertEqual(expected_output, file.getvalue())

    
    def test_create_with_valid_class(self):
         """Assert that output contains an ID"""
        with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("create BaseModel")
        expected_output = ""
        self.assertEqual(expected_output, file.getvalue()[:-1])


   
    def test_create_with_missing_class_name(self):
        with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("create")
        expected_output = "** class name missing **\n"
        self.assertEqual(expected_output, file.getvalue())

    
    def test_show_with_valid_class_and_id(self):
        """Assert that output contains the object"""
        with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("create BaseModel")
            obj_id = file.getvalue().strip()
            self.console.onecmd(f"show BaseModel {obj_id}")
            self.assertEqual(obj_id, file.getvalue())

   
    def test_show_with_missing_class_name(self):
        with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("show")
        expected_output = "** class name missing **\n"
        self.assertEqual(expected_output, file.getvalue()[:-1])

   
    def test_all_with_valid_class_name(self, mock_stdout):
        """Assert that output contains the object"""
         with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("create BaseModel")
            obj_id = file.getvalue().strip()
            self.console.onecmd(f"all BaseModel")
            self.assertEqual(obj_id, file.getvalue())

    def test_all_with_invalid_class_name(self):
        with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("all InvalidClass")
        expected_output = "** class doesn't exist **\n"
        self.assertEqual(expected_output, file.getvalue())


    def test_update_with_invalid_class_name(self):
         with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd('update InvalidClass 123 name "New Name"')
        expected_output = "** class doesn't exist **\n"
        self.assertEqual(expected_output, file.getvalue())

    



if __name__ == '__main__':
    unittest.main()
