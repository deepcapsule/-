from abstractcollection import AbstractCollection

class LinkedDirectedGraph(AbstractCollection):

    def __init__(self, sourceCollection = None):
        """Adds a vertex with the given label to the graph."""
        self._edgeCount = 0
        self._vertices = dict()
        AbstractCollection.__init__(self, sourceCollection)

    def clear(self):
        self.__init__(self, None)

    def clearEdgeMarks(self):
        for edge in self.edges():
            edge.clearMark()

    def clearVerteMarks(self):
        for vertex in self.vertices():
            vertex.clearMark()

    def sizeEdges(self):
        return self._edgeCount

    def sizeVertices(self):
        return len(self)

    def __str__(self):
        return str(self.sizeVertices()) + " Vertices: " \
               + " ".join(map(str, self.vertices())) + "\n" \
                + str(self.sizeEdges()) + " Edges: " \
                + " ".join(map(str, self.edges()))

    def containsVertex(self, label):
        if label in self._vertices:
            return True
        else:
            return False

    def addVertex(self, label):
        if  not self.containsVertex(label):
            self._vertices[label] = LinkedVertex(label)
            self._size += 1

    def removeVertex(self, label):
        """Return True if the vertex was reomved, or False otherwise."""
        removedVertex = self._vertices.pop(label, None)
        if removedVertex is None:
            return False

        # Examine all other vertices to reomve edges
        # directed at the removed vertex
        for vertex in self.vertices():
            if vertex.removeEdgeTo(removedVertex):
                self._edgeCount -= 1
        # Examine all edges from the removed vertex to others
        for edge in removedVertex.incidentEdges():
            self._edgeCount -=1
        return True

    def containsEdge(self, fromLabel, toLabel):
        if self.getEdge(fromLabel, toLabel):
            return True
        else:
            return False

    def addEdge(self, fromLabel, toLabel, weight):
        """Connectes the vertices with an edge with the given weight."""
        if not self.containsEdge(fromLabel, toLabel):
            fromVertex = self.getVertex(fromLabel)
            toVertex = self.getVertex(toLabel)
            fromVertex.addEdgeTo(toVertex, weight)
            self._edgeCount += 1
            return True
        else:
            return False

    def getEdge(self, fromLabel, toLabel):
        """Returns the edge connecting the two vertices, or None if no edge exists."""
        fromVertex = self.getVertex(fromLabel)
        toVertex = self.getVertex(toLabel)
        return fromVertex.getEdgeTo(toVertex)

    def removeEdge(self, fromLabel, toLabel):
        """Returns True if the edge was removed, or False otherwise."""
        fromVertex = self.getVertex(fromLabel)
        toVertex = self.getVertex(toLabel)
        edgeRemovedFlg = fromVertex.removeEdgeTo(toVertex)
        if edgeRemovedFlg:
            self._edgeCount -= 1
        return edgeRemovedFlg

    def getVertex(self, label):
        return self._vertices.get(label)

    def edges(self):
        """Supports iteration over the edges in the graph."""
        result = set()
        for vertex in self.vertices():
            edges = vertex.incidentEdges()
            result = result.union(set(edges))
        return iter(result)

    def vertices(self):
        return iter(self._vertices.values())

    def __iter__(self):
        return iter(self._vertices.values())

    def incidentEdges(self, label):
        vertex = self.getVertex(label)
        if vertex:
            return vertex.incidentEdges()
        else:
            return None

    def neighboringVertices(self, label):
        vertex = self.getVertex(label)
        if vertex:
            return vertex.neighboringVertices()
        else:
            return None

class LinkedVertex(object):

    def __init__(self,label):
        self._label = label
        self._edgeList = list()
        self._mark = False

    def clearMark(self):
        self._mark = False

    def setMark(self):
        self._mark = True

    def isMarked(self):
        return self._mark

    def getLabel(self):
        return self._lable

    def setLabel(self, label, g):
        """Sets the vertex's label to label."""
        g._vertice.pop(self._label, None)
        g._vertice[label] = self
        self._label = label

    def addEdgeTo(self, toVertex, weight):
        edge = LinkedEdge(self, toVertex, weight)
        self._edgeList.append(edge)

    def getEdgeTo(self, toVertex):
        for edge in self._edgeList:
            if edge.getToVertex() == toVertex \
                and edge.getOtherVertex(toVertex) == self:
                return edge
        return False

    def removeEdgeTo(self, toVertex):
        """Returns True if the edge exists and is removed,
        or False otherwise."""
        for edge in self._edgeList:
            if edge.getToVertex() == toVertex \
                and edge.getOtherVertex(toVertex) == self:
                self._edgeList.remove(edge)
                return True
        return False

    def incidentEdges(self):
        for edge in self._edgeList:
            yield edge


    def neighboringVertices(self):
        """Returns the neighboring vertices of this vertex."""
        vertices = list()
        for edge in self._edgeList:
            vertices.append(edge.getOtherVertex(self))
        return iter(vertices)

    def __str__(self):
        return str(self._label)

    def __eq__(self, other):
        if self is other:
            return True
        if type(self) != type(other):
            return False
        return self._label  == other._label and \
            self._edgeList == other._edgeList


class LinkedEdge(object):

    def __init__(self, fromVertex, toVertex, weight = None):
        self._vertex1 = fromVertex
        self._vertex2 = toVertex
        self._weight = weight
        self._mark = False

    def __eq__(self, other):
        """Two edges are equal if they connect the same vertices."""
        if self is other:
            return True
        if type(self) != type(other):
            return False
        return self._vertex1  == other._vertex1 and \
            self._vertex2 == other._vertex2 and \
            self._weight == other._weight

    def clearMark(self):
        self._mark = False

    def setMark(self):
        self._mark = True

    def isMarked(self):
        return self._mark

    def getWeight(self):
        return self._weight

    def setWeight(self, weight):
        self._weight = weight

    def getOtherVertex(self, vertex):
        if self._vertex1 == vertex:
            return self._vertex2
        elif self._vertex2 == vertex:
            return self._vertex1
        else:
            return None

    def getToVertex(self):
        return self._vertex2

    def __str__(self):
        return str(self._vertex1) + ">" \
               + str(self._vertex2) + ":" + str(self._weight)
