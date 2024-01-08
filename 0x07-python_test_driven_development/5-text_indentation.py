#!/usr/bin/python3
"""
    My Code FUNC
"""


def text_indentation(text):
    """
    Indent text based on punctuation.

    Args:
    - text: str, the input text

    Raises:
    - TypeError: if text is not a string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    punctuation = ".?:"
    for char in punctuation:
        text = text.replace(char, f"{char}\n\n")

    lines = [line.strip() for line in text.split('\n')]
    revised = "\n".join(lines)
    print(revised, end="")
