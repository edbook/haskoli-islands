from subprocess import call
from enum import Enum
from pathlib import Path
import typer


def get_value(item):
    if isinstance(item, bytes):
        return item.decode()
    return item
