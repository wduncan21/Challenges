# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 22:54:12 2017

@author: Mr.Wang

Given a string, your task is to count how many palindromic substrings in this
 string.

The substrings with different start indexes or end indexes are counted as 
different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
Note:
The input string length won't exceed 1000.
"""
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        result=0
        for length in range(1,len(s)+1):
            for start in range(len(s)+1-length):
                sub_s=s[start:start+length]
                #if sub_s not in result:
                if sub_s==sub_s[::-1]:
                    result+=1

        return result