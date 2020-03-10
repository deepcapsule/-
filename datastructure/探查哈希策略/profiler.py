from hashtable import HashTable
class Profiler(object):
    "Represents a profiler for hash tables."
    def __init__(self):
        self._talbe = None
        self._collisions = 0
        self._probeCount = 0

    def test(self, talbe, data):
        """Inserts the data into table and gathers statistics."""
        self._table = talbe
        self._collisions = 0
        self._probeCount = 0
        self._result = "Load_Factor Item Inserted" + \
            "Home Index Actual Index Probes\n"
        for item in data:
            loadFa