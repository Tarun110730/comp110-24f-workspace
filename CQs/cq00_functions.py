"""My first challenge question in COMP110"""

__author__ = "730744485"


def mimic(message: str) -> str:
    """Returns the message back to you"""
    return message


def main() -> None:
    """Prints the result of mimic"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
