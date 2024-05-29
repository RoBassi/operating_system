from utilities.priority_queue import PriorityQueue

from operating_system.scheduling.preemptive.preemptive_scheduler import PreemptiveSchedulerAlgorithm

class FPPSSchedulingAlgorithm(PreemptiveSchedulerAlgorithm):
    """ Implementation of Fixed Priority Preemtive Scheduling Algorithm. """

    # TODO (4) Complete the class
    def __init__(self, kernel, quantum):
        super().init(kernel, quantum)
        self.ready_queue = PriorityQueue()

    @property
    def next_process_id(self):
        return self.ready_queue.front

    #def move_to_ready(self, pid, pcb):
        

    #def move_to_running(self, pid, pcb):
        

    def move_to_waiting(self, pid, pcb):
        pass

    def repr(self):
        return str(self.__ready_queue)