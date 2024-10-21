from typing import TypeVar

__all__ = ("corresponding_pairs",)


T1 = TypeVar("T1")
T2 = TypeVar("T2")


def corresponding_pairs(list1: list, list2: list) -> list:
    """Возвращает список кортежей, содержащих соответствующие элементы двух списков.

    Args:
        list1 (list): Первый список.
        list2 (list): Второй список.

    Returns:
        list: Список кортежей, содержащих соответствующие элементы.
    """
    min_length = min(len(list1), len(list2))
    return [(list1[i], list2[i]) for i in range(min_length)]
