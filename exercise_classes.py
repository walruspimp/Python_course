from test_runner import test_runner


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


if __name__ == 'main':
    test_runner()
