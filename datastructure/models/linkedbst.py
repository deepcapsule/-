# -*- coding: utf-8 -*-
"""
File: linkedbst.py
Created on Tue Mar 19 14:38:23 2019

@author: wangchx
"""

from abstractcollection import AbstractCollection
from bstnode import BSTNode


class LinkedBST(AbstractCollection):
    """A  linked-based binary search tree implementation."""
    
    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._root = None
        AbstractCollection.__init__(self, sourceCollection)
    
    # 由于递归搜索算法需要一个树节点作为参数，所以不能将其定义为一个顶级方法。
    # 相反，将该算法定义为一个嵌套的辅助方法，在顶级的find方法中调用它。
    def find(self, item):
        """Returns data if item is found or None otherwise."""
        
        # Helper function to search the binary tree
        def recurse(node):
            if node is None:
                return None
            elif item == node.data:
                return node.data
            elif item < node.data:
                return recurse(node.left)
            else:
                return recurse(node.right)
            
        # Top-level call on the root node
        return recurse(self._root)
    
    def findMin(self):
        """Find the Min value in the tree"""
        
        def recurse(node):
            if node.left:
                return recurse(node.left)
            else:
                return node.data
        
        if self._root:
            return recurse(self._root)
        else:
            return None
        
    def findMax(self):
        """Find the Max value in the tree"""
        
        def recurse(node):
            if node.right:
                return recurse(node.right)
            else:
                return node.data
        
        if self._root:
            return recurse(self._root)
        else:
            return None
            
    
    def replace(self, item, newItem):
        """Replace data  with new  data if item is found 
        or return None otherwise."""
        
        # Helper function to search the binary tree
        def recurse(node):
            if node is None:
                return None
            elif item == node.data:
                node.data = newItem
            elif item < node.data:
                return recurse(node.left)
            else:
                return recurse(node.right)
            
        # Top-level call on the root node
        recurse(self._root)

    
    def inorder(self):
        """Supports an inorder traversal on a view of self."""
        lyst = list()
        def recurse(node):
            if node != None:
                recurse(node.left)
                lyst.append(node.data)
                recurse(node.right)
        recurse(self._root)
        return iter(lyst)
    
    def postorder(self):
        """Supports an postorder traversal on a view of self."""
        lyst = list()
        def recurse(node):
            if node != None:
                recurse(node.left)
                recurse(node.right)
                lyst.append(node.data)
        recurse(self._root)
        return iter(lyst)
    
    def levelorder(self):
        """Supports an leverorder traversal on a view of self."""
        lyst = list()
        queue = list()
        
        def recurse():
            if queue:
                node = queue.pop(0)
                lyst.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if queue:
                recurse()
            
        if self._root != None:
            queue.append(self._root)
            recurse()
        return iter(lyst)
    
    def __iter__(self):
        """Supports an preorder traversal on a view of self."""
        lyst = list()
        if self._root != None:
            lyst.append(self._root)
        while lyst:
            node = lyst.pop()
            yield node.data
            if node.right:
                lyst.append(node.right)
            if node.left:
                lyst.append(node.left)

    def __str__(self):
        """Returns a string representation with the tree rotated
        90 degrees counterclockwise."""
        
        def recurse(node, level):
            s = ""
            if node is not None:
                s += recurse(node.right, level + 1)
                s += "| " * level
                s += str(node.data) + '\n'
                s += recurse(node.left, level + 1)
            return s
        return recurse(self._root, 0)
    
    def add(self, item):
        """Adds item to the tree."""
        
        # Helper function to search for item's position
        def recurse(node):
            # New item is less; go left until spot is found
            if item < node.data:
                if node.left is None:
                    node.left = BSTNode(item)
                else:
                    recurse(node.left)
            # New item is greater or equal;
            # go right until spot is found
            elif node.right is None:
                node.right = BSTNode(item)
            else:
                recurse(node.right)
                
        # Tree is empty, so new item goes at the root
        if self.isEmpty():
           self._root = BSTNode(item)
        # Otherwise, search for the item's spot
        else:
            recurse(self._root)
        self._size += 1
        
    def remove(self, item):
        """Remove the item and adjust it's children if necessary."""
        exist = 1
        def findMin(node):
                if node.left:
                    return findMin(node.left)
                else:
                    return node.data
        def recurse(node, val):
            if node is None:
                exist = 0 
                return
            if val < node.data:
                node.left = recurse(node.left, val)
            elif val > node.data:
                node.right = recurse(node.right, val)
            else:
                if node.left and node.right:
                    rightMin = findMin(node.right)
                    node.data = rightMin
                    node.right = recurse(node.right, rightMin)
                elif node.left is None and node.right is None:
                    node = None
                elif node.right is None:
                    node = node.left
                elif Node.left is None:
                    node = node.right
            return node
        self._root = recurse(self._root, item)
        if exist:
            self._size -= 1
            
    def clear(self):
        self._root = None
        self._size = 0
                    
        