# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 22:09:55 2017

@author: Mr.Wang
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length=temp_length=0
        temp_max=''
        if len(s)==1:
            return 1
        for i in s:
            if i not in temp_max:
                temp_max+=i
            else:
                temp_length=len(temp_max)
                max_length= max(max_length,temp_length)
                temp_max=temp_max[temp_max.index(i)+1:]+i
        temp_length=len(temp_max)
        max_length= max(max_length,temp_length)
        return max_length