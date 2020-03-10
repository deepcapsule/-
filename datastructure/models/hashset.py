from node import Node

from arrays import Array
from abstractset import AbstractSet
from abstractcollection import AbstractCollection

class HashSet(AbstractCollection, AbstractSet):
    """A hashing implementation of a set."""
    DEFAULT_CAPACITY = 3
    def __init__(self, sourceCollection = None, capacity = None):
        if capacity is None:
            self._capacity = HashSet.DEFAULT_CAPACITY
        else:
            self._capacity = capacity
        self._items = Array(self._capacity)
        self._foundNode = self._priorNode = None
        self._index = -1
        AbstractCollection.__init__(self, sourceCollection)

    # Accessor methods
    def __contains__(self, item):
        """Return True if item is in the set or False otherwise."""
        self._index = abs(hash(item)) % len(self._items)
        self._priorNode = None
        self._foundNode = self._items[self._index]
        while self._foundNode != None:
            if self._foundNode.data == item:
                return True
            else:
                self._priorNode = self._foundNode
                self._foundNode = self._foundNode.next
        return False

    def __iter__(self):
        """Supports iteration voer view of self."""

    def __str__(self):
        """Returns the string representation of self."""
        return "{" + ", ".join(map(str, self)) + "}"

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._array = Array(HashSet.DEFAULT_CAPACITY)

    def add(self, item):
        """Adds item to the set if it si not in the set."""
        if not item in self:
            newNode = Node(item, self._items[self._index])
            self._items[self._index] = newNode
            self._size += 1

    def remove(self, item):
        """Precondition:item is in self.
        Raise: KeyError if item is not in self.
        Postcondition: item is removed from self."""
        if not item in self:
           raise KeyError(str(item) + "not in the set.")
        else:
            self._priorNode.next = self._foundNode.next
            self._size -= 1