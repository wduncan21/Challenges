# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 14:59:23 2017

@author: lwang138

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = sum(nums[:3])
        if res==target:
            return target
        for i in range(len(nums)):
            l,r=i+1,len(nums)-1
            while l<r:
                temp=sum([nums[i],nums[l],nums[r]])
                if temp==target:
                    return target
                if abs(temp-target)<abs(res-target):
                    res=temp
                if temp<target:
                    l+=1
                else:
                    r-=1
        return res