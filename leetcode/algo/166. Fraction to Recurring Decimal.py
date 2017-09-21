# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 22:37:01 2017

@author: Mr.Wang

Given two integers representing the numerator and denominator of a fraction, 
return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".
"""
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        n,remainder=divmod(abs(numerator),abs(denominator))
        sign='-' if numerator*denominator<0 else ''
        res = [sign+str(n), '.']
        stack=[]
        while remainder not in stack:
            stack.append(remainder)
            n, remainder = divmod(remainder*10, abs(denominator))
            res.append(str(n))

        idx = stack.index(remainder)
        res.insert(idx+2, '(')
        res.append(')')
        return ''.join(res).replace('(0)', '').rstrip('.')
