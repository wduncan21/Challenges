# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 22:56:48 2017

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
        ##loop through to get the length of all strings, use the shortest one as search start
        current_long=strs[0]
        current_length=len(current_long)
        for i in range(1,len(strs)):
            if len(strs[i])<current_length:
                current_long=strs[i]
                current_length=len(current_long)    
            elif strs[i][0:current_length]!=current_long:
                last_length=current_length
                current_length=int(current_length/2)
                step=int(current_length/2)+1
                while step>1:
                    if strs[i][0:current_length]==current_long[:current_length]:
                        last_length=current_length
                        current_length=last_length+step
                    else:
                        current_length=last_length-step
                    step=int(step/2)
                
                shorter=min(current_length,last_length)+1
                if strs[i][0:shorter]==current_long[:shorter]:
                    current_long=current_long[:shorter]
                else:
                    current_long=current_long[:(shorter-1)]
                            
        return current_long

print(str1)        
print(longestCommonPrefix(0, str1))
print(str2)        
print(longestCommonPrefix(0, str2))
print(str3)        
print(longestCommonPrefix(0, str3))