from hardware.hardware import HARDWARE
from hardware.irq import IRQ

from operating_system.irq_handlers.abstract_interruption_handler import AbstractInterruptionHandler

class IoInInterruptionHandler(AbstractInterruptionHandler):

    def execute(self, irq):
        """
        The current process has requested the use of IO.
        We need to put it in WAITING state and set next process to RUNNING.
        """
        # The device that was requested for use can be retrieved from the arguments.
        device = irq.arguments[0]
        # TODO: (4)
        # The current process needs to be changed to waiting state,
        # and the request be dispatched.
        # First we need to get the currently running process id
        pidToMove = self.kernel.scheduler.currently_running_pid
        
        # Next, we have to move the process to waiting state
        self.kernel.scheduler.move_to_waiting(pidToMove)
        
        # After the process is in waiting state, we need to send the
        # request to the corresponding IO controller.
        ioController = self.kernel.io_controllers_vector.get_by_id(device)
        ioController.request(pidToMove)

        # As the currently running process is now in waiting state,
        # the last step is to tell the scheduler to run the next process
        # in the ready queue, if any.
        runningProcess = self.kernel.scheduler.currently_running_pid
        next_process = self.kernel.scheduler.next_process
        if next_process is not None and runningProcess is None:
                self.kernel.scheduler.move_to_running(next_process)