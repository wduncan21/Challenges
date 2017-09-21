# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 11:33:22 2017

@author: lwang138
Given an array of non-negative integers, you are initially positioned at the 
first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if 0 not in nums:
            return True
        zeros=[i for i,x in enumerate(nums) if x == 0]
        if len(nums)-1 in zeros:
            zeros.pop()
        res=[0]*len(zeros)
        for i in range(len(zeros)):
            for loc in range(zeros[i]):
                if zeros[i]-loc<nums[loc]:
                    res[i]=1
        if len(res)==sum(res):
            return True
        return False