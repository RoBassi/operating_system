from utilities.priority_queue import PriorityQueue

from operating_system.scheduling.preemptive.preemptive_scheduler import PreemptiveSchedulerAlgorithm

class LRTFSchedulingAlgorithm(PreemptiveSchedulerAlgorithm):
    """ Implementation of Longest Running Time First Scheduling Algorithm. """

    # TODO (3) Complete the class
    def __init__(self, kernel, quantum):
        super().init(kernel, quantum)
        self.ready_queue = PriorityQueue()

    @property
    def next_process_id(self):
        return self.ready_queue.front

    def move_to_ready(self, pid, pcb):
        self.ready_queue.enqueue(pid, pcb.burst_time)

    def move_to_running(self, pid, pcb):
        return self.ready_queue.dequeue()

    def move_to_waiting(self, pid, pcb):
        return self.ready_queue.enqueue(pid, pcb.recalculate_remaining_time())

    def repr(self):
        return str(self.__ready_queue)