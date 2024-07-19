from threading import Thread
from time import sleep

class Clock():
    """
    Emulates a hardware clock.
    We use an observer pattern to implement it,
    so any object can subscribe an listen to the clock tick.
    """
    def __init__(self, speed = 1):
        """The speed of the code is expressed in ticks per second. Defaults to 1."""
        self._subscribers = []
        self._running = False
        self._speed = 1 / speed
        self._lastTick = 0

    def addSubscriber(self, subscriber):
        self._subscribers.append(subscriber)

    def stop(self):
        self._running = False

    def start(self):
        logger.info("---- :::: STARTING CLOCK  ::: -----")
        self._running = True
        # Run as a thread in the background
        t = Thread(target=self.__start)
        t.start()

    def __start(self):
        while (self._running):
            self.tick()

    def tick(self):
        self._lastTick += 1
        ## notify all subscriber that a new clock cycle has started
        for subscriber in self._subscribers:
            subscriber.tick(self._lastTick)
        ## wait for a while and keep looping
        sleep(self._speed)