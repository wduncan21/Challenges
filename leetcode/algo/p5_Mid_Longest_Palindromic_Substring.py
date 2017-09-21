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
        Longest=''
        for i in range(len(s)):
            temp_window1=temp_window2=0
            while i-temp_window1>=0 and i+temp_window1<=len(s) and IsPalindrome(s[i-temp_window1:i+temp_window1+1]):
                temp_window1+=1
            temp_window1-=1    
            while i-temp_window2>=0 and i+temp_window2-1<=len(s) and IsPalindrome(s[i-temp_window2:i+temp_window2]):
                temp_window2+=1
            temp_window2-=1
            if len(Longest)<2*temp_window1+1:
                Longest=s[i-temp_window1:i+temp_window1+1]
            if len(Longest)<2*temp_window2:
                Longest=s[i-temp_window2:i+temp_window2]
        return Longest
