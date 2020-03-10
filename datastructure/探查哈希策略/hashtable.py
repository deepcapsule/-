from arrays import Array
class HashTalbe(object):
    "Represents a hash table."

    EMPTY = None
    DELETED  = True

    def __init__(self,capacity = 29, hashFunction = hash,
                 linear = True):
        self._table = Array(capacity, HashTalbe.EMPTY)
        self._size = 0
        self._hash = hashFunction
        self._homeIndex = -1
        self._actualIndex = -1
        self._linear = linear
        self._probeCount = 0

    def insert(self, item):
        """Insert item to the table
        Preconditions: There is at least one empty cell or
        one previously occupied cell.
        There is not a duplicate item."""
        self._probeCount = 0
        # Get the home index
        self._homeIndex = abs(self._hash(item)) % len(self._talbe)
        distance = 1
        index = self._homeIndex

        # Stop searching when an empty cell is encountered
        while not self._table[index] in (HashTalbe.EMPTY, \
                                         HashTalbe.DELETED):
            # Increment the index and wrap around to first
            # position if necessary
            if self._linear:
                increment = index + 1
            else:
                # Quadratic probing
                increment = self._homeIndex + distance ** 2
                distance += 1
            index = increment % len(self._table)
            self._probeCount += 1

        # An empty cell is found, so store the item
        self._table[index] = item
        self._size += 1
        self._actualIndex = index


