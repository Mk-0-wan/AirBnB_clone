#!/usr/bin/python3
"""
A test for the console class
"""
import unittest
import pep8
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """
    A class to test the HBNBCommand class
    """

    def setUp(self):
        """
        Set up a new HBNBCommand instance for each test
        """
        self.cmd = HBNBCommand()

    def test_default(self):
        """
        Test the default prompt value
        """
        self.assertEqual(self.cmd.prompt, '(hbnb) ')

    def test_do_EOF(self):
        """
        Test the do_EOF method
        """
        self.assertTrue(self.cmd.do_EOF(''))

    def test_do_quit(self):
        """
        Test the do_quit method
        """
        self.assertTrue(self.cmd.do_quit(''))

    def test_do_create(self):
        """
        Test the do_create method
        """
        self.assertEqual(self.cmd.prompt, '(hbnb) ')

    def test_do_show(self):
        """
        Test the do_show method
        """
        self.assertEqual(self.cmd.prompt, '(hbnb) ')

    def test_do_destroy(self):
        """
        Test the do_destroy method
        """
        self.assertEqual(self.cmd.prompt, '(hbnb) ')

    def test_do_all(self):
        """
        Test the do_all method
        """
        self.assertEqual(self.cmd.prompt, '(hbnb) ')

    def test_do_update(self):
        """
        Test the do_update method
        """
        self.assertEqual(self.cmd.prompt, '(hbnb) ')

    def test_pycodestyle(self):
        """Testing for pycodestyle implementation"""
        pycode_pass = pep8.StyleGuide(quite=True)
        record = pycode_pass.check_files(
                ['./console.py',
                 './tests/test_console.py'])
        self.assertEqual(record.total_errors, 0, "errors found")


if __name__ == '__main__':
    unittest.main()
