from test_runner import run_tests


class Animal:
    pass


class Dog(Animal):
    pass


def test_isinstance():
    donald = Animal()
    fido = Dog()

    assert isinstance(fido, Animal)
    assert isinstance(donald, Animal)
    assert not isinstance(donald, Dog)


def test_that_fails():
    assert False


if __name__ == '__main__':
    run_tests()
