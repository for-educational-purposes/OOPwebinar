from dis import dis


class A:
    public = 'I\'m public'
    _protected = 'I\'m protected'
    __private = 'I\'m private'

    def public_method(self):
        print(self.public, 'method')

    def _protected_method(self):
        print(self._protected, 'method')

    def __private_method(self):
        print(self.__private, 'method')


if __name__ == '__main__':
    a = A()

    print(a.public)
    print(a._protected)  # noqa
    print(a._A__private)  # noqa

    a.public_method()
    a._protected_method()  # noqa
    a._A__private_method()  # noqa
