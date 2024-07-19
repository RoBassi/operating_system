from utilities.printer import Printer

from hardware.asm import ASM

NEW = "NEW"
READY = "READY"
WAITING = "WAITING"
RUNNING = "RUNNING"
TERMINATED = "TERMINATED"

class PCB:
    """Models a PCB"""

    def __init__(self, pid, memory_start, memory_end):
        self.__pid = pid
        self.__state = NEW
        self.__memory_start = memory_start
        self.__memory_end = memory_end
        self.__pc = memory_start

    @property
    def pid(self):
        """ Returns the PCB's PID. """
        return self.__pid

    @property
    def state(self):
        """ Returns the PCB's state. """
        return self.__state

    @state.setter
    def state(self, value):
        """ Returns the PCB's state. """
        self.__state = value

    @property
    def memory_start(self):
        """
        Returns the initial memory position the
        associated program for this PCB is store at.
        """
        return self.__memory_start

    @property
    def memory_end(self):
        """
        Returns the last memory position the
        associated program for this PCB is store at.
        """
        return self.__memory_end

    @property
    def pc(self):
        """ Returns the status of the PC registry for this PCB. """
        return self.__pc

    @pc.setter
    def pc(self, value):
        """ Assign the status of the PC registry for this PCB. """
        self.__pc = value

    def __repr__(self):
        return Printer.tabulated([
            ["PID", self.__pid],
            ["State", self.__state],
            ["M.Start", self.__memory_start],
            ["M.End", self.__memory_end],
            ["PC", self.__pc]
        ])