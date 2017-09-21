# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 20:29:27 2017

@author: Mr.Wang

Given a string s, partition s such that every substring of the partition 
is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["aa","b"],
  ["a","a","b"]
]
"""

class Solution(object):
    def partition(self, s):
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s)+1):
            if self.isPal(s[:i]):
                self.dfs(s[i:], path+[s[:i]], res)
    
    def isPal(self, s):
        return s == s[::-1]

    def partition2(self, s):
        return [[s[:i]] + rest for i in range(1, len(s)+1) if s[:i] == s[i-1::-1] \
                for rest in self.partition2(s[i:])] or [[]]    




            
a=Solution()
s = "ccdc"
print(a.partition2(s))
print(a.partition(s))
