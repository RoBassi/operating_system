from utilities.printer import Printer

class Memory():
    """Models the Hardware memory"""

    def __init__(self, size):
        self._size = size
        self._cells = [""] * size

    def write(self, addr, value):
        """Write a given value to a given memory address"""
        self._cells[addr] = value

    def read(self, addr):
        """Write the value stored from a given memory address"""
        return self._cells[addr]

    @property
    def size(self):
        """Answer the memory size"""
        return self._size

    def __repr__(self):
        return Printer.tabulated(enumerate(self._cells))