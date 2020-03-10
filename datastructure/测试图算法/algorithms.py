"""
algorithms模块中定义的函数必须接受两个参数：一个图和一个开始的标签。
当没有使用开始标签的时候，它可以被定义为一个可选的参数。
"""

from linkedstack import LinkedStack
from minarrayheap import MinArrayHeap

def topoSort(g, startLabel = None):
    stack = LinkedStack()
    g.clearVertexMarks()
    for v in g.vertices():
        if not v.isMarked():
            dfs(g, v, stack)
    return stack

def dfs(g, v, stack):
    v.setMark()
    for w in g.neighboringVertices(v.getLabel()):
        if not w.isMarked():
            dfs(g, w, stack)
    stack.push(v)

def spanTree(g, startLabel):
    """
    :param g: 图g
    :param startLabel: 开始标签。
    :return: 返回一个列表，包含了图的最小生成树包含的边。
    """
    g.clearVertexMarks()
    g.clearEdgeMarks()
    if not g.containsVertex(startLabel):
        return None
    heap = MinArrayHeap()
    for edge in g.getVertex(startLabel).incidentEdges():
        heap.add(edge)
    k = 1
    while k < len(g.vertices()):


def shortestPaths(g, startLabel):

