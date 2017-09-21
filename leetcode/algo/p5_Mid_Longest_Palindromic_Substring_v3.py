# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 22:44:45 2017

@author: Mr.Wang
"""

"""
Given a string s, find the longest palindromic substring in s. You may assume 
that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
"""

"""
Key logic: only need to check for string ending in s[i] IsPalindrome, only need 
to add 1 or 2 from previous max length. Won't need to check for adding 3
"""

class Solution(object):
    def longestPalindrome(self,s):
        """
        :type s: str
        :rtype: str
        """

        def IsPalindrome(input):
            if input[::-1]==input:
                return True
            else:
                return False
        Longest=s[0]
        max_len=1
        for i in range(1,len(s)):
            if i-max_len>=0 and IsPalindrome(s[i-max_len:i+1]):
                Longest=s[i-max_len:i+1]
            if i-max_len-1>=0 and IsPalindrome(s[i-max_len-1:i+1]):
                Longest=s[i-max_len-1:i+1]                
            max_len=len(Longest)
        return Longest
