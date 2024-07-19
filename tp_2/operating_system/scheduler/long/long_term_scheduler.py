from hardware.hardware import HARDWARE
from operating_system.process import Process

class LongTermScheduler:
    def __init__(self, kernel, process_table):
        self._kernel = kernel
        self._process_table = process_table
        self._next_pid = 1

    def create_process(self, program):
        memory_location = self._allocate_program_in_memory(program)
        self._create_pcb(program, memory_location)
        self._increase_next_pid(self)
        
    def kill_process(self, pid):
        pcb = self._process_table[pid]
        self._dellocate_program_from_memory(pcb)
        self._remove_pcb(pcb)

    def _allocate_program_in_memory(self, program):
        if self._kernel.has_free_memory(len(program.instructions)):
            return self._kernel.allocate(program.instructions)
        else: 
            raise Exception("No hay suficiente memoria")
    
    def _dellocate_program_from_memory(self, pcb):
        for position in range(pcb.memory_start, pcb.memory_end):
            return self._kernel.free(position)
    
    def _create_pcb(self, program, memory_location):
        self._process_table[self._next_pid] = Process(self._next_pid, memory_location, memory_location + len(program.instructions))

    def _remove_pcb(self, pcb):
        del self._process_table[pcb.pid]

    def _increase_next_pid(self):
        self._next_pid += 1