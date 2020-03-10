"""
视图类包含的用于显示菜单和获取命令的方法 。
"""

from model import GraphDemoModel
from algorithms import shortestPaths, spanTree, topoSort

class GraphDemoView(object):

    def __init__(self):
        self._model = GraphDemoModel()
