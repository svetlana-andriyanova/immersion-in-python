# Напишите функцию принимающую на вход только ключевые параметры и
# возвращающую словарь, где ключ — значение переданного аргумента, а
# значение — имя аргумента. Если ключ не хешируем, используйте его строковое
# представление. reverse_kwargs(rev=True, acc="YES", stroka=4) ->
# {True: "rev", "YES": 'acc', 4: "stroka"}

import typing


def reverse_kwargs(**kwargs):
    res_dict = {}
    for key, value in kwargs.items():
        if isinstance(value, typing.Hashable):
            res_dict[value] = key
        else:
            res_dict[str(value)] = key
    return res_dict


rev_dict = reverse_kwargs(rev=True, acc="YES", stroka=4)
print(rev_dict)
