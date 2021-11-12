"""Basic die representation"""
import random


class Die:
    """Basic die"""

    def __init__(self, color, number=None):
        # TODO validate color
        self.color = color
        self.number = random.randint(1, 7) if number is None else number

    def get_number(self):
        """Return number stored on die"""
        return self.number

    def get_color(self):
        """Return color of die"""
        return self.color

    def __repr__(self):
        return f"{self.color}: {self.number}"

    def __str__(self):
        return f"{self.color}: {self.number}"
