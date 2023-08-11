import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    @patch('sys.stdout', new_callable=StringIO)
    def test_help_show(self, mock_stdout):
        self.console.onecmd("help show")
        expected_output = """string representation of object\n"""
        self.assertIn(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_with_valid_class(self, mock_stdout):
        """Assert that output contains an ID"""
        self.console.onecmd("create BaseModel")
        self.assertIn("", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_with_missing_class_name(self, mock_stdout):
        self.console.onecmd("create")
        expected_output = "** class name missing **\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_with_valid_class_and_id(self, mock_stdout):
        """Assert that output contains the object"""
        self.console.onecmd("create BaseModel")
        obj_id = mock_stdout.getvalue().strip()
        self.console.onecmd(f"show BaseModel {obj_id}")
        self.assertIn(obj_id, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_with_missing_class_name(self, mock_stdout):
        self.console.onecmd("show")
        expected_output = "** class name missing **\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_all_with_valid_class_name(self, mock_stdout):
        """Assert that output contains the object"""
        self.console.onecmd("create BaseModel")
        obj_id = mock_stdout.getvalue().strip()
        self.console.onecmd(f"all BaseModel")
        self.assertIn(obj_id, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_all_with_invalid_class_name(self, mock_stdout):
        self.console.onecmd("all InvalidClass")
        expected_output = "** class doesn't exist **\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)


    @patch('sys.stdout', new_callable=StringIO)
    def test_update_with_invalid_class_name(self, mock_stdout):
        self.console.onecmd('update InvalidClass 123 name "New Name"')
        expected_output = "** class doesn't exist **\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
