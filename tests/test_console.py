#!/usr/bin/python3
"""Module for TestHBNBCommand class."""


from models.engine.file_storage import FileStorage
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

    def test_help_show(self):
        with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("help show")
        expected_output = """string representation of object"""
        self.assertEqual(expected_output, file.getvalue()[:-1])

    def test_help(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
        s = """
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

"""
        self.assertEqual(s, f.getvalue())

    def test_create_with_missing_class_name(self):
        with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("create")
        expected_output = "** class name missing **\n"
        self.assertEqual(expected_output, file.getvalue())

    def test_show_with_missing_class_name(self):
        with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("show")
        expected_output = "** class name missing **"
        self.assertEqual(expected_output, file.getvalue()[:-1])

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

    def test_help_EOF(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
        s = 'Captures Control+D by the User\n'
        self.assertEqual(s, f.getvalue())

    def test_help_quit(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
        s = 'Quit command to exit the program\n'
        self.assertEqual(s, f.getvalue())

    def test_help_create(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
        s = 'Creates a new instance of BaseModel\n'
        self.assertEqual(s, f.getvalue())

    def test_help_show(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
        s = 'string representation of objects\n'
        self.assertEqual(s, f.getvalue())

    def test_help_destroy(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
        s = 'deletes an instance based on the class name and id\n'
        self.assertEqual(s, f.getvalue())

    def test_help_all(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
        s = 'Prints all instances based on the class name\n'
        self.assertEqual(s, f.getvalue())

    def test_help_count(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help count")
        s = 'Counts the instances of a class.\n'
        self.assertEqual(s, f.getvalue())

    def test_help_update(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
        s = 'updates an object\n'
        self.assertEqual(s, f.getvalue())

    def test_do_quit(self):
        """Tests quit commmand."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
        msg = f.getvalue()
        self.assertTrue(len(msg) == 0)
        self.assertEqual("", msg)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit garbage")
        msg = f.getvalue()
        self.assertTrue(len(msg) == 0)
        self.assertEqual("", msg)


if __name__ == '__main__':
    unittest.main()
