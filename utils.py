import os


def pause(automated: bool) -> None:
    if automated:
        return
    input("Press the Enter key to continue: ")