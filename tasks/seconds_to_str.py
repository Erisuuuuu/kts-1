__all__ = ("seconds_to_str",)


def seconds_to_str(seconds: int) -> str:
    """Реализует текстовое представление времени.

    Example:
        >> seconds_to_str(20)
        20s
        >> seconds_to_str(60)
        01m00s
        >> seconds_to_str(65)
        01m05s
        >> seconds_to_str(3700)
        01h01m40s
        >> seconds_to_str(93600)
        01d02h00m00s
    """
    day = seconds // (24 * 60 * 60)
    seconds -= (day * 24 * 60 * 60)
    hours = seconds // (60 * 60)
    seconds -= (hours * 60 * 60)
    minu = seconds // 60
    seconds -= (minu * 60)
    sec = seconds
    if day == 0:
        if hours == 0:
            if minu == 0:
                return f'{sec}s'
            return f'{minu}m{sec}s'
        return f'{hours}h{minu}m{sec}s'
    return f'{day}d{minu}m{sec}s'
