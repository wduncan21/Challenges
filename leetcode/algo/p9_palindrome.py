# -*- coding: utf-8 -*-
"""
Created on Tue May 16 23:32:04 2017

@author: Mr.Wang
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if int(str(abs(x))[::-1])==x:
           return True
        else:
            return False