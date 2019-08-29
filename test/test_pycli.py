import unittest
from sys import argv

from decocli.cli import CLI


class TestPyCLI(unittest.TestCase):

    def setUp(self):
        a = argv
        a.clear()
        a.append('decoCLI.py')
        CLI.clear()
        CLI.set_param('--name', 'name', 1)

        @CLI.set_cmd('version')
        def version(**kwargs):
            return 'Version 0.01'

        @CLI.set_cmd('printing')
        def print_name(**kwargs):
            return kwargs['name']

    def test_parser_command(self):
        self.assertEqual('Version 0.01', CLI.parser.commands['version'].exec(), 'Parser Command Version Test')

    def test_parser_params(self):
        self.assertEqual(1, CLI.parser.params['--name'].len, 'Parser Param Length Test')

    def test_exec(self):
        a = argv
        a.append('version')
        result = CLI.exec()

        self.assertEqual('Version 0.01', result, 'Exec Test')

    def test_params(self):
        a = argv
        a.append('printing')
        a.append('--name')
        a.append('decoCLI')
        result = CLI.exec()

        self.assertEqual('decoCLI', result, 'Command with Param Test')

    def test_class_cli(self):
        a = argv
        a.append('setup')
        a.append('--name')
        a.append('decoCLI')

        class API:
            def __init__(self, name):
                self._name = name

            @CLI.set_cmd('name')
            def name(self):
                return self._name

        @CLI.set_cmd('setup')
        def setup(**kwargs):
            api = API(kwargs['name'])
            return api.name()

        result = CLI.exec()

        self.assertEqual('decoCLI', result, 'Class CLI Test')

    def test_no_name_command(self):
        a = argv
        a.append('one')

        @CLI.set_cmd()
        def one():
            return 1

        result = CLI.exec()

        self.assertEqual(1, result, 'No name command Test')


if __name__ == '__main__':
    unittest.main()
