# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 13:24:23 2017

@author: lwang138
Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[[]]
        for i in nums:
            res+=[j+[i] for j in res]
        return res                
a=Solution()
nums=[1,2]
print(a.subsets(nums))
            