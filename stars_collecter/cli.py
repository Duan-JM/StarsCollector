"""Command line interface for the package

    Author: Duan-JM
    Email: vincent.duan95@outlook.com
    ChangeLog:
        2020-09-27: init cli

    Typical usage examples:
    >>> sc -u Duan-JM
"""

from .core import printResults


def main():
    printResults()


if __name__ == "__main__":
    main()
