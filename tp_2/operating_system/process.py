from utilities.printer import Printer
from hardware.asm import ASM

CREATED = "CREATED"
READY = "READY"
BLOCKED = "BLOCKED"
EXECUTING = "EXECUTING"
FINISHED = "FINISHED"

class Process:
    def __init__(self, pid, memory_start, memory_end):
        self._pid = pid
        self._state = CREATED
        self._memory_start = memory_start
        self._memory_end = memory_end
        self._pc = memory_start

    @property
    def pid(self):
        return self._pid
    
    @property
    def state(self):
        return self._state
    
    @property
    def memory_start(self):
        return self._memory_start
    
    @property
    def memory_end(self):
        return self._memory_end
    
    @property
    def pc(self):
        return self.pc
    
    def ready(self):
        self._state = READY

    def blocked(self):
        self._state = BLOCKED

    def executing(self):
        self._state = EXECUTING

    def finished(self):
        self._state = FINISHED
    
    def __repr__(self):
        return