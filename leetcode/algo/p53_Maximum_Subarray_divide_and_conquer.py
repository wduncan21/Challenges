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
        cutoff=int(len(nums)/2)
        if len(nums)=1:
            current_max=nums
            pos=3
        elif:
            left=nums[:cutoff]
            right=nums[cutoff:]
            max_left,left_pos=maxSubArray(left)
            max_right,right_pos=maxSubArray(right)
            current_max=max(max_left,max_right,max_left+max_right)
            pos=[max_left,max_right,max_left+max_right].index(current_max)
            if 