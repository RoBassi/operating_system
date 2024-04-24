class Queue:
    """
    Models a queue data structure, using a list internally.
    This utility allows to simplify the use of lists in some scenarios,
    and to think about queues instead.
    """
    def __init__(self):
        self.__data = []

    @property
    def is_empty(self):
        """ Answers if the queue is empty. """
        return len(self.__data) == 0

    @property
    def front(self):
        """
        Answers the element in the front of the queue,
        or None if the queue is empty.
        """
        return None if self.is_empty else self.__data[0]

    def enqueue(self, datum):
        """ Add an element to the back of the queue. """
        self.__data.append(datum)

    def dequeue(self):
        """ Remove the front elemen from queue and return it. """
        return self.__data.pop(0)

    def __repr__(self):
        return " <- ".join([str(e) for e in self.__data])