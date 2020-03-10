# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 10:57:19 2019

@author: wangchx
"""

from treeparser import TreeParser

class ParserView(object):
    
    def __init__(self):
        pass
        
    def inputs(self):
        result = input("Enter an infix expression: ")
        return result
    
    def run(self):
        while True:
            expr = self.inputs()
            if expr == "exit":
                break
            parser = TreeParser(expr)
            tree = parser.parser()
            if tree:
                print("Prefix: " + tree.prefix())
                print("Infix: " + tree.infix())
                print("Postfix: " + tree.postfix())
                print("Value: " + str(tree.value()))
            
def main():
    parserView = ParserView()
    parserView.run()
    
if __name__ == '__main__':
    main()
        