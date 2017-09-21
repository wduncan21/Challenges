# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 23:40:07 2017

@author: Mr.Wang

Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note: All inputs will be in lower-case.
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res={}
        for i in strs:
            temp=[]
            for j in i:
                temp.append(j)
                temp.sort()
            key=str(temp)
            if key in res:
                res[key].append(i)
            else:
                res[key]=[i]
        return list(res.values())
        
a=Solution()
a.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])