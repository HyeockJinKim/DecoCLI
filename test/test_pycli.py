import unittest

from pycli.cli import PyCLI


class TestPyCLI(unittest.TestCase):

    def setUp(self):
        self.py_cli = PyCLI()
        self.py_cli.set_param('--name', 'name', 1)

        @self.py_cli.set_cmd('version')
        def version(**kwargs):
            return 'Version 0.01'

    def test_command(self):
        self.assertEqual(self.py_cli.parser.commands['version'].exec(), 'Version 0.01')

    def test_params(self):
        self.assertEqual(self.py_cli.parser.params['--name'].len, 1)


if __name__ == '__main__':
    unittest.main()