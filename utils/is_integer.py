def is_integer(value: str) -> bool:
    try:
        int(value)
        return True
    except ValueError:
        return False
