from utilities.priority_queue import PriorityQueue

from operating_system.scheduling.non_preemptive.non_preemptive_scheduler import NonPreemptiveSchedulerAlgorithm

class SJFSchedulingAlgorithm(NonPreemptiveSchedulerAlgorithm):
    """ Implementation of Shortest Job First Scheduling Algorithm. """

    # TODO (2) Complete the class
    def __init__(self,kernel,quantum):
            super().__init__(kernel,quantum)
            self.__ready_priority_queue = PriorityQueue()

    @property
    def next_process_id(self):
        if not self.__ready_priority_queue.is_empty:
            return self.__ready_priority_queue.front
        return None

    def move_to_ready(self, pid, pcb):
        self.__ready_priority_queue.enqueue(pid, -pcb.burst_time)
        
        
    def move_to_running(self, pid, pcb):
        if not self.__ready_priority_queue.is_empty:
            self.__ready_priority_queue.dequeue()
        else:
            print("La cola de listos esta vacia.")

    def move_to_waiting(self, pid, pcb):
        pass

    def __repr__(self):
        return str(self.__ready_priority_queue)