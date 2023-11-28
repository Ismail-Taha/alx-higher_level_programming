#!/usr/bin/python3

"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.
    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    L = 0
    while L < len(text) and text[L] == ' ':
        L += 1

    while L < len(text):
        print(text[L], end="")
        if text[L] == "\n" or text[L] in ".?:":
            if text[L] in ".?:":
                print("\n")
            L += 1
            while L < len(text) and text[L] == ' ':
                L += 1
            continue
        L += 1
