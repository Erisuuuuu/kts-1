from typing import TypeVar

__all__ = ("cartesian_product",)


T1 = TypeVar("T1")
T2 = TypeVar("T2")


def cartesian_product(list1: list, list2: list) -> list:
    """Возвращает декартово произведение двух списков с использованием базовых конструкций.

    Args:
        list1 (list): Первый список.
        list2 (list): Второй список.

    Returns:
        list: Список кортежей, представляющих все пары.
    """
    result = []
    for item1 in list1:
        for item2 in list2:
            result.append((item1, item2))
    return result
