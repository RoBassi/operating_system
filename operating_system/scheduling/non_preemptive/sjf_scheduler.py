from utilities.priority_queue import PriorityQueue

from operating_system.scheduling.non_preemptive.non_preemptive_scheduler import NonPreemptiveSchedulerAlgorithm

class SJFSchedulingAlgorithm(NonPreemptiveSchedulerAlgorithm):
    """ Implementation of Shortest Job First Scheduling Algorithm. """

    # TODO (2) Complete the class
    def init(self, kernel, quantum):
        super().init(kernel, quantum)
        self.ready_queue = PriorityQueue()

    @property
    def next_process_id(self):
        return self.ready_queue.front

    def move_to_ready(self, pid, pcb):
        self.ready_queue.enqueue(pid, -pcb.burst_time)

    def move_to_running(self, pid, pcb):
        return self.ready_queue.dequeue()

    def move_to_waiting(self, pid, pcb):
        pass

    def repr(self):
        return str(self.__ready_queue)