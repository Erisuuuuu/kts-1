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

    if day > 0:
        return f'{day:02d}d{hours:02d}h{minu:02d}m{sec:02d}s'
    elif hours > 0:
        return f'{hours:02d}h{minu:02d}m{sec:02d}s'
    elif minu > 0:
        return f'{minu:02d}m{sec:02d}s'
    else:
        return f'{sec:02d}s'
