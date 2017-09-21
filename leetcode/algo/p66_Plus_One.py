# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 23:23:14 2017

@author: Mr.Wang
"""

"""
Given a non-negative integer represented as a non-empty array of digits, plus 
one to the integer.

You may assume the integer do not contain any leading zero, except the number 
0 itself.

The digits are stored such that the most significant digit is at the head of 
the list.

"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i=len(digits)-1
        while digits[i]==9:
            digits[i]=0
            i-=1
        if i<0:
            digits=[1]+digits
        else:
            digits[i]+=1
        return digits