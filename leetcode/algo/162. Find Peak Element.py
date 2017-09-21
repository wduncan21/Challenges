# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 22:50:01 2017

@author: Mr.Wang

A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return 
its index.

The array may contain multiple peaks, in that case return the index to any one 
of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function 
should return the index number 2.
"""
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=[float('-inf')]+nums+[float('-inf')]
        for i in range(1,len(nums)):
            if nums[i+1]<nums[i]>nums[i-1]:
                return int(i-1)
    def findPeakElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return 0
        if len(nums)==2:
            return int(nums[0]<nums[1])
        mid=int(len(nums)/2)
        if nums[mid-1]>nums[mid]:
            return self.findPeakElement2(nums[:mid+1])
        else:
            return mid+self.findPeakElement2(nums[mid:])


a=Solution()
print(a.findPeakElement2([1, 2, 3, 5]))
print(a.findPeakElement2([1]))