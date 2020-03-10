# -*- coding: utf-8 -*-
"""
File: pfevaluatorview.py
Created on Tue Mar 12 10:49:14 2019

@author: wangchx
"""

from  model import PFEvaluatorModel

class PFEvaluatorView():
    
    def __init__(self):
        self._model = PFEvaluatorModel()
        
    def run(self):
        while True:
            inputStr = input("Enter a postfix expression: ")
            if not inputStr:
                print("input nothing,please input again.")
                continue
            elif inputStr == 'exit':
                print('bye')
                break
            else:
                print(self._model.format(inputStr))
                try:
                    print(self._model.evaluate(inputStr))
                except AttributeError as e:
                    print(e)
                    print(self._model.evaluationStatus())


def main():
    view = PFEvaluatorView()
    view.run()
                    
if __name__ == '__main__':
    main()