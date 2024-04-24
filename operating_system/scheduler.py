from utilities.printer import Printer
from utilities.queue import Queue

from operating_system.pcb import *

""" It's useful to remember the following chart of states of a process
according to the different interruptions that may occur.

    NEW --                       --->TERMINATED
          |                      |
          |                      |
     #NEW |   ----------------   | #KILL
          |  |    #SWAP      |   |
          V  v               |   |
        READY -------------> RUNNING
          ^     #DISPATCH      |
  #IO_OUT |                    | #IO_IN
          |                    |
          ------  WAITING <-----
"""
class Scheduler():
    """
    Models the short-term scheduler in charge of performing the
    context switching and determine the next process to assign the CPU.
    For now we are going to follow a really simple strategy, based on
    a minimal queue.
    The Scheduler is the one in charge of maintaining which process is doing
    what, and changing them around in a coherent state at different times. It
    does this with support of the Dispatcher.
    """
    def __init__(self, kernel):
        self.__kernel = kernel
        # We are going to keep track of the current process being running
        # by the CPU. Of course, we start with no process running.
        self.__currently_running_pid = None
        # We are going to keep track of which processes are ready to be
        # executed, and which are waiting for an IO request. When a process
        # is in the ready queue, it should have the READY state in it's PCB
        # and when it's in the IO queue, it should be in the WAITING state.
        # In the queue we only save the PID of the process, and not the PCB.
        self.__ready_queue = Queue()

    @property
    def currently_running_pid(self):
        """ Returns the process table of the OS. """
        return self.__currently_running_pid

    @property
    def next_process(self):
        """
        Return the next process in the ready queue,
        if any, or None if there's no next process.
        Note that this does not remove the process
        from the queue.
        """
        return self.__ready_queue.front

    ############### BASIC PROCESS STATE CHANGE ########################

    def move_to_ready(self, pid):
        """ Move a process with the given pid to the ready state. """
        pcb = self.__kernel.process_table.get_pcb_by_pid(pid)
        # To become ready, the process may be in any state other than
        # terminated
        if pcb.state == TERMINATED:
            raise RuntimeError("IllegalState: A TERMINATED process cannot be moved to READY")
        # If it is on the running state, we need to unload it from the CPU
        if pcb.state == RUNNING:
            self.__kernel.dispatcher.save(pcb)
            self.__currently_running_pid = None
        # If it's already ready, there is nothing to do
        if pcb.state == READY:
            return
        # If it was on waiting state, nothing is to be done
        if pcb.state == WAITING:
            pass
        # Add it to the ready queue
        self.__ready_queue.enqueue(pid)
        # And update the PCB to the ready state
        pcb.state = READY

    def move_to_running(self, pid):
        """ Move a process with the given pid to the running state. """
        pcb = self.__kernel.process_table.get_pcb_by_pid(pid)
        # To become running, the process must be in the ready state
        if not pcb.state == READY:
            raise RuntimeError("IllegalState: A non READY process cannot be moved to RUNNING")
        # Remove from the ready queue, as a precondition,
        # it should be at the front, although other strategies may exist
        self.__ready_queue.dequeue()
        # Set the process as the currently running one
        self.__currently_running_pid = pid
        # Change the PCB state to running
        pcb.state = RUNNING
        # And load the PCB to the CPU
        self.__kernel.dispatcher.load(pcb)

    def move_to_waiting(self, pid):
        """ Move a process with the given pid to the waiting state. """
        pcb = self.__kernel.process_table.get_pcb_by_pid(pid)
        # To become waiting, the process must be in the running state
        if not pcb.state == RUNNING:
            raise RuntimeError("IllegalState: A non RUNNING process cannot be moved to WAITING")
        # Save the CPU to the PCB
        self.__kernel.dispatcher.save(pcb)
        # Now, there is no running process (Another process should be moved
        # to running)
        self.__currently_running_pid = None
        # And of course, update the PCB state
        pcb.state = WAITING

    def move_to_terminated(self, pid):
        """ Move a process with the given pid to the terminated state. """
        pcb = self.__kernel.process_table.get_pcb_by_pid(pid)
        # To become terminated, the process must be in the running state
        if not pcb.state == RUNNING:
            raise RuntimeError("IllegalState: A non RUNNING process cannot be moved to TERMINATED")
        # Save the CPU to the PCB
        self.__kernel.dispatcher.save(pcb)
        # Now, there is no running process (Another process should be moved
        # to running)
        self.__currently_running_pid = None
        # And of course, update the PCB state
        pcb.state = TERMINATED

    ############### END BASIC PROCESS STATE CHANGE ########################

    def __repr__(self):
        return Printer.tabulated([[
            Printer.tabulated([
                ["Currently running", self.__currently_running_pid],
                ["Ready queue", str(self.__ready_queue)]
            ])]], headers=["Scheduler"]
        )