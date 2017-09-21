# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 22:13:57 2017

@author: Mr.Wang

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another 
expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        res=0
        symbol=["+",  "*","/","-"]
        loc=0
        while len(tokens)>1:
            if tokens[loc] not in symbol:
                loc+=1
            else:
                ope=tokens[loc]
                temp=int(eval(tokens.pop(loc-2)+tokens.pop(loc-1)+tokens.pop(loc-2)))
                res=temp+1 if temp<0 and ope=='/'  else temp
                loc-=2
                tokens=tokens[:loc]+[str(res)]+tokens[loc:]
        return int(tokens[0])
        
        
a=Solution()
tokens=["4","-2","/","2","-3","-","-"]#["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(a.evalRPN(tokens))