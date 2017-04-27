import inspect
import importlib


def run_tests():
    module_name = inspect.stack()[1].filename.split('.')[0]
    mod = importlib.import_module(module_name)
    test_functions = (f for f in dir(mod) if f.startswith('test_'))

    print('Testing module {}'.format(module_name))

    for test_function in test_functions:
        print('Testing function {}... '.format(test_function), end='')
        try:
            exec('mod.{}()'.format(test_function))
            print('SUCCESS')
        except AssertionError:
            print('FAIL')
