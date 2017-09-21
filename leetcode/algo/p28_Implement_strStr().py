# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 22:23:35 2017

@author: Mr.Wang
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        window=len(needle)
        for i in range(len(haystack)+1-window):
            if haystack[i:i+window]==needle:
                return i
        return -1