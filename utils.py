import os


def pause(automated: bool) -> None:
    if not automated:
        input("Press the Enter key to continue: ")
    return