# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 23:21:47 2017

@author: Mr.Wang
"""
"""

Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
"""
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        """
        dividend=a0*2*b0*divisor+a1*b1*divisor+...+ak*bk*divisor
        where bk=2**k,then result=a0*2*b0+a1*b1+...+ak*bk
        for each round, calculate largest b then calculate the corresponding a,
        subtract bk*divisor from dividend add to result, until dividend<divisor
        """
        positive=(dividend>0) == (divisor>0)
        dividend=abs(dividend)
        divisor=abs(divisor)
        b=1
        res=0
        while dividend>=divisor:
            temp=divisor
            b=1
            while dividend>=temp:
                old_temp=temp
                temp+=temp
                old_b=b
                b+=b
            a=0
            while dividend>=old_temp:
                dividend-=old_temp
                a+=old_b
            res+=a
        if not positive:
            res=-res
        return min(max(-2147483648, res), 2147483647)