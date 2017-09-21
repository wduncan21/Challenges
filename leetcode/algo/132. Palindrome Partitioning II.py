# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 22:46:16 2017

@author: Mr.Wang
Given a string s, partition s such that every substring of the partition is a 
palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using
 1 cut.
"""
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=self.partition(s)
        return min([len(i) for i in res])
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

a=Solution()
s = "ccdc"
print(a.minCut(s))