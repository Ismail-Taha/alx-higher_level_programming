#!/usr/bin/python3

"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """Inverts the int operators == and !=."""

    def __eq__(self, other_value):
        """Override == operator with != behavior."""
        return super().__ne__(other_value)

    def __ne__(self, other_value):
        """Override != operator with == behavior."""
        return super().__eq__(other_value)
