import unittest
from sys import argv

from pycli.cli import PyCLI


class TestPyCLI(unittest.TestCase):

    def setUp(self):
        self.py_cli = PyCLI()
        self.py_cli.set_param('--name', 'name', 1)
        a = argv
        a.clear()
        a.append('pyCLI.py')

        @self.py_cli.set_cmd('version')
        def version(**kwargs):
            return 'Version 0.01'

        @self.py_cli.set_cmd('printing')
        def print_name(**kwargs):
            return kwargs['name']

    def test_parser_command(self):
        self.assertEqual(self.py_cli.parser.commands['version'].exec(), 'Version 0.01', 'Parser Command Version Test')

    def test_parser_params(self):
        self.assertEqual(1, self.py_cli.parser.params['--name'].len, 'Parser Param Length Test')

    def test_exec(self):
        a = argv
        a.append('version')
        result = self.py_cli.exec()
        
        self.assertEqual(['Version 0.01'], result, 'Exec Test')

    def test_params(self):
        a = argv
        a.append('printing')
        a.append('--name')
        a.append('pyCLI')
        result = self.py_cli.exec()

        self.assertEqual(['pyCLI'], result, 'Command with Param Test')


if __name__ == '__main__':
    unittest.main()