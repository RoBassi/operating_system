from threading import Thread
from time import sleep

class Clock():
    """
    Emulates a hardware clock.
    We use an observer pattern to implement it,
    so any object can subscribe an listen to the clock tick.
    """
    def __init__(self, speed = 1):
        """ The speed of the code is expressed in ticks per second. Defaults to 1. """
        self.__subscribers = []
        self.__running = False
        self.__delay = 1 / speed
        self.__last_tick = 0
        self.__is_overclocked = False

    def add_subscriber(self, subscriber, priority=None):
        """
        Add a subscriber to this clock. The subscriber will get
        notified each time the clock ticks.
        """
        # This allows to register an element with higher priority than others
        # If no priority i given, just add at the end
        if (priority == None):
            self.__subscribers.append(subscriber)
        else:
            # If priority is given, lower priority means receiving the
            # notification first. So 0 is the lowest. The priority is
            # actually the index in which to insert the subscriber.
            # This useful as sometimes we want to be sure that the
            # subscriber gets notified before something happens, such as
            # the history, which requires to register data before the
            # actual tick's execution.
            self.__subscribers.insert(priority, subscriber)

    def stop(self):
        """ Stop the clock. """
        self.__running = False

    def start(self):
        """ Start the clock. """
        self.__running = True
        # Run as a thread in the background
        t = Thread(target=self.__start)
        t.start()

    def __start(self):
        """ The function that executes when the clock starts, in a new thread. """
        while (self.__running):
            self.tick()

    def tick(self):
        """ The tick function is executed with each tick of the clock. """
        self.__last_tick += 1
        ## notify all subscriber that a new clock cycle has started
        for subscriber in self.__subscribers:
            subscriber.tick(self.__last_tick)
        ## wait for a while and keep looping
        if (not self.__is_overclocked):
            sleep(self.__delay)

    def overclock(self):
        """
        Overclock the clock. That is, ignore the delay between ticks.
        Not really needed, but useful for debugging.
        """
        self.__is_overclocked = True

    def reset(self):
        """
        Reset the clock to it's regular speed.
        Not really needed, but useful for debugging.
        """
        self.__is_overclocked = False