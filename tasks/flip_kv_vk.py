from typing import TypeVar

__all__ = (
    "flip_kv_vk",
    "flip_kv_vk_safe",
)


KT = TypeVar("KT")
KV = TypeVar("KV")


def flip_kv_vk(original_dict: dict) -> dict:
    """Переворачивает словарь, меняя местами ключи и значения.

    Args:
        original_dict (dict): Исходный словарь.

    Returns:
        dict: Новый словарь с перевернутыми ключами и значениями.
    """
    return {value: key for key, value in original_dict.items()}


def flip_kv_vk_safe(original_dict: dict) -> dict:
    """Безопасно переворачивает словарь, собирая ключи с одинаковыми значениями в списки.

    Args:
        original_dict (dict): Исходный словарь.

    Returns:
        dict: Новый словарь с перевернутыми ключами и значениями.
    """
    flipped_dict = {}

    for key, value in original_dict.items():
        if value not in flipped_dict:
            flipped_dict[value] = []
        flipped_dict[value].append(key)

    return flipped_dict
