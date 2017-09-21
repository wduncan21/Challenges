# -*- coding: utf-8 -*-
"""
Created on Tue May 16 23:13:25 2017

@author: Mr.Wang
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>=0:
            rev=int(str(x)[::-1])
        else:
            rev=0-int(str(x)[::-1][:-1])
        if abs(rev)<2147483647:
            return rev
        else:
            return 0