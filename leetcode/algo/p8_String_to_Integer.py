# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 20:52:55 2017

@author: Mr.Wang
"""

"""
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, 
please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given 
input specs). You are responsible to gather all the input requirements up front.
"""

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        sign=1
        num=0
        if str=='':
            return num
        lists=list(str.strip())
        if lists[0]=='-':
            sign=-1
            lists=lists[1:]
        elif lists[0]=='+':
            lists=lists[1:]            
        i=0
        while i<len(lists) and lists[i].isdigit():
            num=num*10+ord(lists[i])-ord('0')
            i+=1
        return min(max(-2147483648,num*sign),2147483647)