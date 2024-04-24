from hardware.hardware import HARDWARE

from operating_system.pcb import RUNNING, READY, WAITING

class Dispatcher:
    """
    The dispatcher is in charge of loading and saving the state
    of the CPU into a particular PCB.
    """
    """El despachador se encarga de cargar y guardar el estado de la CPU en una PCB particular."""

    def __init__(self, kernel):
        self.__kernel = kernel

    def load(self, pcb):
        """
        Load the state of a PCB into the CPU.
        Next tick will tart executing the program of the loaded process.
        """
        # TODO: (2)
        # We need to load the state of the given PCB to the CPU.
        # This implies copying the information stored in the PCB
        # to the corresponding registries in the CPU, so next tick will
        # run the process the PCB represents.

        """Cargue el estado de una PCB en la CPU. El siguiente tick comenzará a ejecutar el programa del proceso cargado."""
        # TODO: (2)
        # Necesitamos cargar el estado de la PCB dada en la CPU.
        # Esto implica copiar la información almacenada en la PCB
        # a los registros correspondientes en la CPU, por lo que el siguiente tick será
        # ejecuta el proceso que representa la PCB.
        # ---------------------------------------------------------------------------------
        # Access relevant information from the PCB
        HARDWARE.cpu.pc = pcb.pc

    def save(self, pcb):
        """
        Save the current state of the CPU to the given PCB.
        The CPU remains IDLE into the next load.
        """
        # TODO: (2)
        # We need to save the current state of the CPU to the given PCB.
        pcb.pc = HARDWARE.cpu.pc
        # This occurrs on a context switch, so after this step, the CPU
        # should be put as IDLE, not running anything.
        HARDWARE.cpu.pc = -1