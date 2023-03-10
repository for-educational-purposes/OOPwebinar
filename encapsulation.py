"""
Инкапсуляция - принцип ООП, согласно которому сложность реализации
программного компонента должна быть спрятана за его интерфейсом.
* Отсутствует доступ к внутреннему устройству программного компонента.
* Взаимодействие компонента с внешним миром осуществляется
  посредством интерфейса, который включает публичные методы и поля (атрибуты).

Для чего нужна инкапсуляция?
* Инкапсуляция упрощает процесс разработки,
  т.к. позволяет нам не вникать в тонкости реализации того или иного объекта.
* Повышается надежность программ за счет того,
  что при внесении изменений в один из компонентов,
  остальные части программы остаются неизменными.
* Обмен компонентами между программами становится легче.
"""


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
