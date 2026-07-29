"""A small utility script demonstrating basic Python concepts."""

import datetime


def greet(name: str = "World") -> str:
    """Return a friendly greeting with the current timestamp."""
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"Hello, {name}! Today is {now}."


def main():
    print(greet("Starlight User"))


if __name__ == "__main__":
    main()
