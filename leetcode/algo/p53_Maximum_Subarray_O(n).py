# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 22:35:59 2017

@author: Mr.Wang
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_max=max_i=nums[0]
        for i in nums[1:]:
            ## max_i checks if i itself is larger or adding i to previous max_i is larger, so i is always included
            max_i=max(i,i+max_i)
            ## current_max keeps the current max subarray, and compare it with the new max_i to see which one is larger
            current_max=max(current_max,max_i)
        return current_max