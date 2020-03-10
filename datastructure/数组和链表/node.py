from collections import Iterable
class Node(object):
    """Represents a singly linked node."""
    
    def __init__(self, data, next = None):
        """Instantiates a Node with a default next of None."""
        self.data = data
        self.next = next
        
    def getData(self):
        return self.data
    
    def setData(self,newData):
        self.data = newData
        
    def getNext(self):
        return self.next
    
    def setNext(self,newNext):
        self.next = newNext
        

class LinkedList(object):
    #初始化，头结点为空
#    def __init__(self):
#        self.head = None
    
    def __init__(self, listData=None):
        self.head = None
        if isinstance(listData,Iterable):
            for data in reversed(listData):
                self.add(data)
        elif listData is None:
            pass
        else:
            self.add(listData)
        
    def add(self, data):
        '首部添加节点'
        newNode = Node(data)
        newNode.setNext(self.head)
        self.head = newNode     
        
    def insert(self,i,data):
        probe = self.head
        if i <=0 or probe is None:
            #可以简写为(self.head = Node(data,self.head))
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode
        else:
            while i > 1 and probe.next != None:
                i -= 1
                probe = probe.next
            #可以简写为probe.next = Node(data,probe.next)
            newNode = Node(data)
            newNode.next = probe.next
            probe.next = newNode
        
    def search(self, data):
        probe = self.head
        while probe != None and data != probe.getData():
            probe = probe.getNext()
        if probe != None:
            return True
        else:
            return False
        
    def remove(self, data):
        if self.isEmpty():
            return
        probe = self.head
        if probe.getData() == data:
            self.head = probe.getNext()
        else:
            while probe.getNext() != None and probe.next.data != data:
                probe = probe.getNext()
            if probe.next != None:
                probe.next =probe.next.next
                
    def isEmpty(self):
        return self.head == None
    
    def size(self):
        count = 0
        probe = self.head
        while probe != None:
            count += 1
            probe = probe.getNext()
        return count
                
    def __str__(self):
        probe = self.head
        s = 'Link head'
        while probe != None:
            s += '->' + str(probe.data)
            probe = probe.next
        s += '->None'
        return s
    

class OrderedLinkedList(object):
    
    def __init__(self, listData=None):
        self.head = None
        if listData is None:
            return
        elif isinstance(listData,Iterable):
            for data in listData:
                self.add(data)
        else:
            self.add(listData)
        
    def add(self, data):
        '添加在适当位置使其成为有序链表'
        probe = self.head
        previous = None   # 记录前一个节点
        while probe != None:
            if probe.getData() > data:
                break
            previous = probe
            probe = probe.getNext()
        
        newNode = Node(data)
        if previous == None:
            newNode.setNext(self.head)
            self.head = newNode
        else:
            previous.setNext(newNode)
            newNode.setNext(probe)
            
    def remove(self, data):
        if self.isEmpty():
            return
        probe = self.head
        if probe.getData() == data:
            self.head = probe.getNext()
        else:
            while probe.getNext() != None and probe.next.data != data:
                probe = probe.getNext()
            if probe.next != None:
                probe.next =probe.next.next
                
    def isEmpty(self):
        return self.head == None
    
    def size(self):
        count = 0
        probe = self.head
        while probe != None:
            count += 1
            probe = probe.getNext()
        return count
        
            
    def __str__(self):
        probe = self.head
        s = 'Link head'
        while probe != None:
            s += '->' + str(probe.data)
            probe = probe.next
        s += '->None'
        return s
    
#带有哑头节点的循环链表，哑头可以存放链表长度
class CircleLinkedList():
    
    def __init__(self):
        self.head = Node(None, None)
        self.head.next = self.head
    
    #在表头插入
    def add(self, data):
        newNode = Node(data)
        newNode.next = self.head.next
        self.head.next = newNode
        
    def insert(self, i, data):
        probe = self.head
        if i <=0 or probe is None:
            self.head = Node(data,self.head)
        else:
            while i > 1 and probe.next != None:
                i -= 1
                probe = probe.next
            probe.next = Node(data,probe.next)
        
    def __str__(self):
        probe = self.head.next
        s = 'Link head'
        while probe != self.head:
            s += '->' + str(probe.data)
            probe = probe.next
        s += '->Link head again'
        return s
    
class TwoWayNode(Node):
    
    def __init__(self, data, previous = None, next = None):
        Node.__init__(self, data, next)
        self.previous = previous
        
        
class DoubleLinkedList(object):
    
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add(self, data):
        '末端添加节点'
        if self.head is None:
            self.head = TwoWayNode(data)
            self.tail = self.head
        else:
            self.tail.next = TwoWayNode(data, self.tail)
            self.tail = self.tail.next
            
        
            
            