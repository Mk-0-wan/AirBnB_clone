import unittest

from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.cmd = HBNBCommand()

    def test_default(self):
        self.cmd.default('create BaseModel')
        self.assertEqual(self.cmd.prompt, '(hbnb) ')

    def test_do_EOF(self):
        self.assertTrue(self.cmd.do_EOF(''))

    def test_do_quit(self):
        self.assertTrue(self.cmd.do_quit(''))

    def test_do_create(self):
        self.cmd.do_create('BaseModel')
        self.assertEqual(self.cmd.prompt, '(hbnb) ')

    def test_do_show(self):
        self.cmd.do_create('BaseModel')
        self.cmd.do_show('BaseModel 1234-1234-1234')
        self.assertEqual(self.cmd.prompt, '(hbnb) ')

    def test_do_destroy(self):
        self.cmd.do_create('BaseModel')
        self.cmd.do_destroy('BaseModel 1234-1234-1234')
        self.assertEqual(self.cmd.prompt, '(hbnb) ')

    def test_do_all(self):
        self.cmd.do_create('BaseModel')
        self.cmd.do_all('BaseModel')
        self.assertEqual(self.cmd.prompt, '(hbnb) ')

    def test_do_update(self):
        self.cmd.do_create('BaseModel')
        self.cmd.do_update('BaseModel 1234-1234-1234 email "aibnb@mail.com"')
        self.assertEqual(self.cmd.prompt, '(hbnb) ')


if __name__ == '__main__':
    unittest.main()
