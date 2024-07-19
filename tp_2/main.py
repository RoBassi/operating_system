#!/usr/bin/env python3
import cmd
from time import sleep

from utilities.printer import Printer
from utilities.compiler import Compiler

from hardware.hardware import HARDWARE
from hardware.asm import ASM
from operating_system.kernel import Kernel
""""
#  1) a- Por medio del reloj: 
#           tanto usando de la clase Clock el metodo tick() que le avisa al CPU cada vez que se realiza un tick, 
#           como tambien pidiendole al reloj que arranque.
#      b- Se usa el patron Facade: Sirve para abstraer la complejidad de una interfaz subyacente y proveer una mas 
#       amigable y simple, muchas veces orquestando procesos complejos.
#      c- Se usa el patron Observer. Conviene el uso de este patron por si se quiere tener mas de un subscriptor. Por el momento,
#       tanto Cpu como main son subscriptores de Clock.

"""
# This class uses some python reflection in order to load the programs.
# Aside from the available_programs and get_program, any other method
# that does not start with __ is considered a program, and attempted
# to be compiled once the instance is created. Add as many programs
# as you want.
class SoftwarePrograms:
    """
    A simple holder class for all your program. This is ued by the CLI
    when searching for a program by name.
    """
    def __init__(self):
        self._programs = dict()
        # Python magic (Gets all the defined method of this class to iterate)
        for prog in [p for p in self.__class__.__dict__.keys() if not self.__is_ignored_pattern__(p)]:
            self._programs[prog] = Compiler.compile(prog, getattr(self, prog)())

    def __is_ignored_pattern__(self, name):
        return (
            name[0:2] == "__" or
            name == "available_programs" or
            name == "get_program"
        )

    def available_programs(self):
        """Return all the available program names"""
        return self._programs.keys()

    def get_program(self, program_name):
        """Return a program based on the name"""
        return self._programs[program_name]

    def program1(self):
        return [
            ASM.CPU(1),
            ASM.IO(1),
            ASM.CPU(3)
        ]

    def program2(self):
        return [
            ASM.CPU(3),
            ASM.IO(2),
            ASM.CPU(1)
        ]


# Now this main file has been converted to a CLI application.
# You can run commands that will allow you to manage the
# application, as well as having a constant monitoring on your
# hardware state (CPU and memory).
# Each method tarting with do_ is a valid command and the preloop works
# as an initialization. You may change the default initialization values
# in preloop if you might.
# You should not feel the need to modify this, but this class works in tandem
# with the programs class, so you may modify that one to change the programs
# you want to have at hand.
class HardwareManagementCLIApp(cmd.Cmd):

    ############### HARDWARE CONFIGURATION AND BEHAVIOR ########################

    _memory_size=20
    _clock_speed=0.5
    _showing_ticks = False
    _start_in_turbo_mode=True

    ############### END HARDWARE CONFIGURATION AND BEHAVIOR ########################


    ############### CLI APP CONFIGURATION ########################

    prompt = "Hardware >> "
    intro = "Welcome to the hardware manager. Type 'help' for available commands."
    _programs = SoftwarePrograms()
    _os = None

    def preloop(self):
        """
        This method is executed before starting the application,
        so it"s used to initialize all elements.
        """
        Printer.initialize()
        HARDWARE.setup(memorySize=self._memory_size, clockSpeed=self._clock_speed)
        self._os = Kernel()
        # We subscribe, in order to print after every tick the
        # hardware status.
        HARDWARE.clock.addSubscriber(self)
        # Adjust speed if starting in turbo mode
        if (self._start_in_turbo_mode):
            HARDWARE.clock._speed = 0
        # Show available programs.
        Printer.show("Available programs are:")
        for prog in self._programs.available_programs():
            Printer.show(self._programs.get_program(prog))

    def do_quit(self, line):
        """Exit the application."""
        return True

    ############### END CLI APP CONFIGURATION ########################

    ############### MANIPULATE HARDWARE ########################

    def do_on(self, line):
        """Turn ON the computer."""
        Printer.show(" ---- TURNING COMPUTER ON ---- ")
        HARDWARE.turnOn()

    def do_off(self, line):
        """Turn OFF the computer."""
        HARDWARE.turnOff()
        Printer.show(" ---- TURNING COMPUTER OFF ---- ")

    def do_turbo_on(self, line):
        """Turn ON turbo mode."""
        # Turbo sets the speed of the clock to immediate mode,
        # this is usefull when running ticks manually for debugging
        HARDWARE.clock._speed = 0
        Printer.show(" ---- STARTING TURBO MODE ---- ")

    def do_turbo_off(self, line):
        """Turn OFF turbo mode."""
        # Set the speed back to original value
        HARDWARE.clock._speed = 1 / self._clock_speed
        Printer.show(" ---- ENDING TURBO MODE ---- ")

    def do_status(self, line):
        """Show the hardware status"""
        os_config = Printer.tabulated([["No configuration yet"]],
                                    headers=["Configuration"])
        os_proctable = Printer.tabulated([["No process table yet"]],
                                    headers=["Process Table"])
        os_data = os_config + "\n\n" + os_proctable
        data = Printer.tabulated([[HARDWARE.cpu, HARDWARE.memory, os_data]],
            headers=["CPU", "Memory", "Operating System"],
            numalign="center", stralign="left"
        )
        Printer.show(data)

    ############### END MANIPULATE HARDWARE ########################


    ############### SIMULATE TICKING ########################

    def do_tick(self, line):
        """Run a clock"s tick, even if computer is off."""
        ticks = 1
        # If the user passes as integer, perform that many ticks
        if (line != "" and line.isdigit()):
            ticks = int(line)
        for _ in range(ticks):
            HARDWARE.clock.tick()

    def do_show_ticks(self, line):
        """Show the hardware status"""
        self._showing_ticks = True

    def do_hide_ticks(self, line):
        """Show the hardware status"""
        self._showing_ticks = False

    def tick(self, tickNbr):
        if (self._showing_ticks):
            Printer.show("        --------------- tick: {tickNbr} ---------------".format(tickNbr = tickNbr))
            self.do_status("")

    ############### END SIMULATE TICKING ########################


    ############### LOAD PROGRAMS ########################

    def do_load(self, line):
        """Load a program from the ones in SoftwarePrograms"""
        try:
            prog = self._programs.get_program(line)
            # Here we should tell the OS to load our program
            # For now, and for testing purposes, just
            # load the instructions in memory (But here is
            # where the OS should kick in)
            self._os.create_process(prog)
        except:
            Printer.error("No program with the name: " + line)

    ############### END LOAD PROGRAMS ########################

    def do_kill(self, line):
        try:
            pid = int(line.string())
            self._os.kill_process(pid)
        except TypeError:
            Printer.error("No hay proceso con id: " + line)
        except Exception as e:
            Printer.error("ERROR " + str(e))

if __name__ == "__main__":
    HardwareManagementCLIApp().cmdloop()