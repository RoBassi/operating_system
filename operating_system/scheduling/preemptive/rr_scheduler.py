from utilities.queue import Queue

from hardware.irq import IRQ

from operating_system.pcb import *
from operating_system.scheduling.preemptive.preemptive_scheduler import PreemptiveSchedulerAlgorithm

class RRSchedulingAlgorithm(PreemptiveSchedulerAlgorithm):
    """ Implementation of Round Robin Scheduling Algorithm. """

    # TODO (5) Complete the class
    