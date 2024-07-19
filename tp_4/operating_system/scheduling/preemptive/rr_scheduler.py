from utilities.queue import Queue

from hardware.irq import IRQ

from operating_system.pcb import *
from operating_system.scheduling.preemptive.preemptive_scheduler import PreemptiveSchedulerAlgorithm

class RRSchedulingAlgorithm(PreemptiveSchedulerAlgorithm):
    """ Implementation of Round Robin Scheduling Algorithm. """

    # TODO (5) Complete the class
    def __init__(self, kernel, quantum):
        super().__init__(kernel, quantum)
        self.__quantum = quantum
        self.__ready_queue = Queue()
        HARDWARE.clock.add_subscriber(self)
        self.__current_quantum = 0

    @property
    def next_process_id(self):
        if not self.__ready_queue.is_empty:
            return self.__ready_queue.front.pid
        return None
    
    def tick(self, last_tick):
        self.__current_quantum += 1
        if self.__current_quantum >= self.__quantum:
            self.__current_quantum = 0
        HARDWARE.interrupt_vector.handle(IRQ.DISPATCH(True))
    
    def move_to_ready(self, pid, pcb):
        self.__ready_queue.enqueue(pcb)
    
    def move_to_running(self, pid, pcb):
        if(not self.__ready_queue.is_empty):
            self.__ready_queue.dequeue()
    
    def move_to_waiting(self, pid, pcb):
        pass

    def __repr__(self):
        return str(self.__ready_queue)
    
    