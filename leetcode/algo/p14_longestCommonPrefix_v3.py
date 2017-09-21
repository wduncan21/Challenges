# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 23:13:44 2017

@author: Mr.Wang
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ""
        ## for every character in the first string, check if it is the same in all other strings
        for i in range(len(strs[0])):
            for string in strs[1:]:
                ## for every string, if max length reached or unequal, return the current string[0][:i]
                if i >= len(string) or string[i] != strs[0][i]:
                    return strs[0][:i]
        ## if everything matches, return the complete string[0]        
        return strs[0]



print(str1)        
print(longestCommonPrefix(0, str1))
print(str2)        
print(longestCommonPrefix(0, str2))
print(str3)        
print(longestCommonPrefix(0, str3))