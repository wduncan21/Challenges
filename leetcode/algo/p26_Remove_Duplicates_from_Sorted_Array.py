# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 22:36:58 2017

@author: Mr.Wang
"""

"""
Given a sorted array, remove the duplicates in place such that each element 
appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with 
constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums 
being 1 and 2 respectively. It doesn't matter what you leave beyond the new 
length.
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length=temp=len(nums)
        if length==0:
            return 0
        
        for i in range(length-1,0,-1):
            if nums[i] ==nums[i-1]:
                nums.pop(-(temp-i))                
                temp-=1
        return len(nums)