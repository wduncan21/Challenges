# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 20:11:37 2017

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
        while len(s)>0:
            try:
                if valid[s[0]]==s[1]:
                    s=s[2:]
                elif valid[s[0]]==s[-1]:
                    s=s[1:-1]
                elif 
                else:
                    return False
            except:
                return False
        return True