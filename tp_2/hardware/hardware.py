from hardware.memory import Memory
from hardware.cpu import Cpu
from hardware.clock import Clock

class Hardware():
    """
    Represents a full computer hardware, the "motherboard" along with the
    other components wired in, if you may.
    """

    def setup(self, memorySize = 20, clockSpeed = 1):
        self._memory = Memory(memorySize)
        self._cpu = Cpu(self._memory)
        self._clock = Clock(clockSpeed)
        self._clock.addSubscriber(self._cpu)

    @property
    def cpu(self):
        return self._cpu

    @property
    def memory(self):
        return self._memory

    @property
    def clock(self):
        return self._clock

    def turnOn(self):
        return self.clock.start()

    def turnOff(self):
        self.clock.stop()

    def __repr__(self):
        return "{cpu}\n{mem}".format(cpu=self._cpu, mem=self._memory)


"""An instance of the hardware that acts as a global variable
being accessible from anywhere"""
HARDWARE = Hardware()