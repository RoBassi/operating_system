from hardware.hardware import HARDWARE
from operating_system.scheduler.long.long_term_scheduler import LongTermScheduler

class Kernel():

    def __init__(self):
        self._process_table = {}
        self._long_term_scheduler = LongTermScheduler(self, self._process_table)
        self._last_allocated_position = 0

    def create_process(self, program):
        self._long_term_scheduler.create_process(program)
        
    def kill_process(self, pid):
        self._long_term_scheduler.kill_process(pid)

    def has_free_memory(self, size):
        return HARDWARE.memory.size - self._last_allocated_position >= size

    def allocate (self, data):
        memory_location = self._last_allocated_position
        for i in range(len(data)): 
            HARDWARE.memory.write(memory_location + i, data[i])
        self._last_allocated_position += len(data)
        return memory_location
    
    def free(self, posicion):
        HARDWARE.memory.write(posicion, '')

    def __repr__(self):
        return "Kernel "