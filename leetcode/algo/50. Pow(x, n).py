# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 23:45:53 2017

@author: Mr.Wang

Implement pow(x, n).

"""
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        neg=1
        if n==0:
            return 1
        if n<0:
            neg=-1
            n=abs(n)
            x=1/x
        res=x
        while n>1:
            to_add=n-int(n/2)
            n=int(n/2)
            temp=x**to_add
            res=res*temp
        return res*neg
a=Solution()
print(a.myPow(2.000,-2147483648))