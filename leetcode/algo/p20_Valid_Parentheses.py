# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 23:47:14 2017

@author: Mr.Wang
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s)%2==1:
            return False
        valid={'(': ')', '{':'}', '[' : ']'}
        for i in range(int(len(s)/2)):
            try:
                if valid[s[2*i]]!=s[2*i+1] and valid[s[i]]!=s[-(i+1)]:
                    return False
            except KeyError: 
                return False
        return True