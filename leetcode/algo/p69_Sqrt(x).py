# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 23:38:59 2017

@author: Mr.Wang
"""

"""
Implement int sqrt(int x).

Compute and return the square root of x.
"""
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<2:
            return x        
        lower=0
        upper=x
        dist=upper-lower
        while dist>1:
            temp_mid=int((upper+lower)/2)
            if temp_mid**2==x:
                return temp_mid
            elif temp_mid**2>x:
                upper=temp_mid
            else:
                lower=temp_mid                
            dist=upper-lower
        if upper**2>x:
            return lower
        else:
            return upper
