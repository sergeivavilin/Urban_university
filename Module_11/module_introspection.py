import inspect


class IntrospectionClass:
    """
    Класс для тестирования работы функции introspection_info()

    """
    def __init__(self):
        self.string = "String"
        self.integer = 50

    def __str__(self):
        return f"{self.__class__.__name__}"

    def __repr__(self):
        return "Integer"

    def return_dir_list(self):
        return self.__dir__()


def introspection_info(obj):
    """
    Выводит строки с данными об объекте, включающий следующую информацию:
    - Тип объекта.
    - Атрибуты объекта.
    - Методы объекта.
    - Модуль, к которому объект принадлежит.
    :param obj:
    :return:
    """

    # Получаем все атрибуты и методы объекта
    all_attributes_methods = dir(obj)

    # Собираем атрибуты и методы
    attributes = obj.__dict__
    # Получаем все методы объекта, включая методы класса
    methods = [method for method in all_attributes_methods if callable(getattr(obj, method))]

    # Получаем модуль объекта
    module =  inspect.getmodule(obj)

    # Получаем тип объекта
    type_obj = type(obj)

    # Выводим информацию
    print(f"Тип объекта: {type_obj}")
    print(f"Атрибуты объекта: {attributes}")
    print(f"Методы объекта: {methods}")
    print(f"Модуль, к которому объект принадлежит: {module}")
    print(f"DocString объекта: '{inspect.getdoc(obj)}'")


if __name__ == '__main__':
    test_obj = IntrospectionClass()
    introspection_info(test_obj)
