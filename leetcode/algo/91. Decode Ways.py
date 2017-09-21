# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 14:52:39 2017

@author: lwang138

A message containing letters from A-Z is being encoded to numbers using the 
following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways
 to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
"""
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0]=='0':
            return 0
        res=[0 for x in range(len(s)+1)]
        res[0]=1
        for i in range(len(s)):
            if s[i]!='0':
                res[i+1]+=res[i]
            if i!=0 and int(s[i-1:i+1])<27 and int(s[i-1:i+1])>9:
                res[i+1]+=res[i-1]

        return res[-1]
        
a=Solution()
print(a.numDecodings('01'))

print(a.numDecodings('27'))


print(a.numDecodings('101'))

print(a.numDecodings('110'))

print(a.numDecodings('100'))