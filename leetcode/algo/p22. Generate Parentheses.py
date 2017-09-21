# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 22:10:59 2017

@author: Mr.Wang
"""

"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
class Solution(object):
    def generateParenthesis_slow(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=['()']
        i=1
        while i<n:            
            temp_res=[]
            for j in res:
                for start in range(len(j)):
                    for end in range(start,len(j)):
                        temp=j[:start]+'('+j[start:end]+')'+j[end:]
                        if temp not in temp_res:
                            temp_res.append(temp) 
            res=temp_res
            i+=1
        return res
        

    def generateParenthesis(self, n):
        def generate(p, left, right, parens=[]):
            if left:         generate(p + '(', left-1, right)
            if right > left: generate(p + ')', left, right-1)
            if not right:    parens += p,
            return parens
        return generate('', n, n)