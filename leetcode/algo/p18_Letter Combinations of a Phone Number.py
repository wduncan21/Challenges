# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 23:39:33 2017

@author: Mr.Wang
"""
"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
"""
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        if not digits:
            return []
        solutions=[]
        for i in str(digits):
            letters=dic[i]
            temp_solutions=[]
            for j in letters:
                if solutions:
                    temp_solutions.extend([x+j for x in solutions])
                else:
                    temp_solutions.extend([j])
            solutions=temp_solutions
        return solutions