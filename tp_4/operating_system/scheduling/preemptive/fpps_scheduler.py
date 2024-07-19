from utilities.priority_queue import PriorityQueue

from operating_system.scheduling.preemptive.preemptive_scheduler import PreemptiveSchedulerAlgorithm

class FPPSSchedulingAlgorithm(PreemptiveSchedulerAlgorithm):
    """ Implementation of Fixed Priority Preemtive Scheduling Algorithm. """

    # TODO (4) Complete the class
    def __init__(self, kernel, quantum):
        super().__init__(kernel, quantum)
        self._ready_priority_queue = PriorityQueue()
        
    @property
    def next_process_id(self):
        if not self._ready_priority_queue.is_empty:
            return self._ready_priority_queue.front
        return None
    
    def move_to_ready(self, pid, pcb):
        self._ready_priority_queue.enqueue(pid, pcb.priority)
        
    
    def move_to_running(self, pid, pcb):
        if not self._ready_priority_queue.is_empty:
            return self._ready_priority_queue.dequeue()
        return None    
    
    def move_to_waiting(self, pid, pcb):
      pass

    def __repr__(self):
        return str(self.__ready_priority_queue)