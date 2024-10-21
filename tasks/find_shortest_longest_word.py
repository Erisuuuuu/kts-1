import re
__all__ = ("find_shortest_longest_word",)



def find_shortest_longest_word(text: str) -> tuple:
    """Находит самое короткое и самое длинное слово в тексте.

    Args:
        text (str): Входной текст.

    Returns:
        tuple: Кортеж из самого короткого и самого длинного слова.
    """
    # Используем регулярное выражение для поиска всех слов
    words = re.findall(r'\b\w+\b', text)

    if not words:
        return (None, None)

    shortest_word = min(words, key=len)
    longest_word = max(words, key=len)

    return (shortest_word, longest_word)
