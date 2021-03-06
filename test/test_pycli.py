import unittest
from sys import argv

from decocli.api import cli_class
from decocli.cli import CLI
from decocli.mbr.subcli import SubCLI


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
            print(kwargs)
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

    def test_no_arg_command(self):
        a = argv
        a.append('one')

        @CLI.set_cmd
        def one():
            return 1

        result = CLI.exec()

        self.assertEqual(1, result, 'No name command Test')

    def test_list_namespace_command1(self):
        a = argv
        a.append('get')
        a.append('one')
        get = SubCLI('get')

        @get.set_cmd('one')
        def one():
            return 1

        @get.set_cmd('two')
        def two():
            return 2

        CLI.add_sub_cli(get)
        result = CLI.exec()

        self.assertEqual(1, result, 'List Namespace command Test1')

    def test_list_namespace_command2(self):
        a = argv
        a.append('get')
        a.append('two')
        get = SubCLI('get')

        @get.set_cmd('one')
        def one():
            return 1

        @get.set_cmd('two')
        def two():
            return 2

        CLI.add_sub_cli(get)
        result = CLI.exec()

        self.assertEqual(2, result, 'List Namespace command Test2')

    def test_class_cli_api1(self):
        a = argv
        a.append('one')
        CLI.clear()

        @cli_class
        class A:
            def one(self):
                return 1

            def two(self):
                return 2

        result = CLI.exec()
        self.assertEqual(1, result, 'Class CLI TEST')

    def test_class_cli_api2(self):
        a = argv
        a.append('two')
        CLI.clear()

        @cli_class
        class A:
            def one(self):
                return 1

            def two(self):
                return 2

        result = CLI.exec()
        self.assertEqual(2, result, 'Class CLI TEST')

    def test_class_cli_api3(self):
        a = argv
        a.append('num')
        CLI.clear()

        @cli_class
        class A:
            def __init__(self):
                self.num = 3

            def num(self):
                return self.num

        result = CLI.exec()
        self.assertEqual(3, result, 'Class CLI TEST')

    def test_class_cli_api4(self):
        a = argv
        a.append('add')
        a.append('num')
        CLI.clear()

        @cli_class
        class A:
            def __init__(self):
                self.num = 3

            def add(self):
                self.num += 1

            def num(self):
                return self.num

        result = CLI.exec_seq()
        self.assertEqual(4, result, 'Class CLI TEST')

    def test_class_cli_api5(self):
        a = argv
        CLI.clear()

        a.append('get')
        a.append('--n')
        a.append('2')
        a.append('num')

        @cli_class
        class A:
            def __init__(self):
                self.num = 3

            def get(self, n):
                self.num = int(n)

            def num(self):
                return self.num

        result = CLI.exec_seq()
        self.assertEqual(2, result, 'Class CLI params TEST')


if __name__ == '__main__':
    unittest.main()
