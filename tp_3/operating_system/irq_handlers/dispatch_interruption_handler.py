from operating_system.irq_handlers.abstract_interruption_handler import AbstractInterruptionHandler

class DispatchInterruptionHandler(AbstractInterruptionHandler):

    def execute(self, irq):
        """
        Dispatch the next process to the running state.
        """
        preemptive = irq.arguments[0]
        pid = self.kernel.scheduler.currently_running_pid
        # TODO: (6)
        # As we have The next process in the ready state should be moved
        # to the running state.
        if preemptive or (not preemptive and pid in None):
            nextProcess = self.kernel.scheduler.next_process
            if nextProcess is not None:
                self.kernel.scheduler.move_to_running(nextProcess)