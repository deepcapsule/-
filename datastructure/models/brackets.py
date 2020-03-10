# -*- coding: utf-8 -*-
"""
File: brackets.py
Created on Mon Mar 11 13:54:39 2019

@author: wangchx
"""

from linkedstack import LinkedStack

def bracketsBalance(exp):
    """exp is s string that represents the expression"""
    stk = LinkedStack()
    for ch in exp:
        if ch in ["[", "("]:
            stk.push(ch)
        elif ch in [']', ')']:
            if stk.isEmpty():
                return False
            chFromStck = stk.pop()
            if ch == ']' and chFromStck != '[' or \
            ch == ')' and chFromStck != '(' :
                return False
    return stk.isEmpty()

def main():
    exp = input("Enter a bracketed expression: ")
    if bracketsBlance(exp):
        print('OK')
    else:
        print('Not Ok')
        
if __name__ == "__main__":
    main()