"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=100):
        self.start = start

    def generate(self):
        """Increments serial by one when called"""
        self.start += 1
        return self.start - 1

    def reset(self):
        """Resets serial back to initial value"""
        self.start = 100



