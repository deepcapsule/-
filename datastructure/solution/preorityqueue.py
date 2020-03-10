import threading
class PreorityQueue():

    def __init__(self):
        self._items = Heap()
        self._index = 0
        self._cv  = threading.Condition()

    def push(self, preority, item):
        pre = - preority
        with self._cv:
            self._items.push((pre, self._index, item))
            self._index += 1
            self._cv.notify()

    def pop(self):
        with self._cv:
            while len(self) == 0:
                self._cv.wait()
        return self._items.pop()[-1]

    def __len__(self):
        return len(self._items)

class Heap():

    def __init__(self, source = None):
        self._items = list()
        self._size = 0
        if source:
            for item in source:
                self.push(item)

    def __len__(self):
         return self._size

    def push(self, item):
        if len(self) < len(self._items):
            self._items[len(self)] = item
        else:
            self._items.append(item)
        cur_pos = len(self)
        self._size += 1
        while cur_pos > 0:
            parent = (cur_pos-1) // 2
            if self._items[parent] <= item:
                break
            self._items[cur_pos] = self._items[parent]
            self._items[parent] = item
            cur_pos = parent

    def peek(self):
        if len(self) == 0:
            raise Exception("empty heap")
        return self._items[0]

    def pop(self):
        if len(self) == 0:
            raise Exception("empty heap")
        top_item = self._items[0]
        bottom_item = self._items[len(self) - 1]
        if len(self) == 1:
            self._size -= 1
            return bottom_item

        def heapify(heap, root, size):
            left = 2 * root + 1
            right = left + 1
            smaller = root
            if left < size and heap[smaller] > heap[left]:
                smaller = left
            if right < size and heap[smaller] > heap[right]:
                smaller = right
            if smaller != root:
                heap[smaller],heap[root] = heap[root],heap[smaller]
                heapify(heap, smaller, size)

        self._items[0] = bottom_item
        heapify(self._items, 0, len(self) - 1)
        self._size -= 1
        return top_item

    def __iter__(self):
        temp = type(self)()
        for i in range(len(self)):
            temp.push(self._items[i])
        while len(temp) != 0:
            yield temp.pop()

class heap():

    def __init__(self, source = None):
        self._items = list()
        if source:
            self._items = list()
            self.buildheap()

    def is_empty(self):
        return not self._items

    def peek(self):
        if self.is_empty():
            raise Exception("the stack is empty")
        return self._items[0]

    def shiftup(self, value, index):
        curpos = index
        parent = (curpos - 1) // 2
        while curpos > 0 and value < self._items[parent]:
            self._items[index] = self._items[parent]
            curpos = parent
            parent = (curpos - 1) // 2
        self._items[curpos] = value

    def push(self, value):
        self._elems.append(None)
        self.shiftup(value, len(self._items) - 1)

    def shiftdown(self, value, root, size):
        pos = root
        left = 2 * pos + 1
        right = left + 1
        while left < size:
            if right < size and self._items[right] < self._items[left]:
                left = right
            if value < self._items[left]:
                break
            self._items[pos] = self._items[left]
            pos = left
            left = 2 * pos + 1
            right = left + 1
        self._items[pos] = value

    def buildheap(self):
        size = len(self._items)
        for i in range(size // 2 - 1, -1, -1):
            self.shiftdown(self._items[i], i, size
                           )

if __name__ == "__main__":
    queue = PreorityQueue()
    queue.push(2,"wo")
    queue.push(3, "ni")
    queue.push(2, "ta")
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())