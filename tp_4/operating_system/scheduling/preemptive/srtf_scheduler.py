from utilities.priority_queue import PriorityQueue

from operating_system.scheduling.preemptive.preemptive_scheduler import PreemptiveSchedulerAlgorithm

class SRTFSchedulingAlgorithm(PreemptiveSchedulerAlgorithm):
    """ Implementation of Shortest Running Time First Scheduling Algorithm. """

    # TODO (3) Complete the class
    def __init__(self, kernel, quantum):
        super().__init__(kernel, quantum)
        self._ready_priority_queue = PriorityQueue()
    
    @property
    def next_process_id(self):
        if not self._ready_priority_queue.is_empty:
            return self._ready_priority_queue.front
        return None
    
    def move_to_ready(self, pid, pcb):
        priority = - pcb.remaining_time
        self._ready_priority_queue.enqueue(pid, priority)
    
    def move_to_running(self, pid, pcb):
        if not self._ready_priority_queue.is_empty:
            self._ready_priority_queue.dequeue()
        else:
            print("La cola de listos esta vacia.")
    
    def move_to_waiting(self, pid, pcb):
        pass

    def __repr__(self):
        return str(self.__ready_priority_queue)