# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 23:17:17 2017

@author: Mr.Wang

Find the contiguous subarray within an array (containing at least one number) 
which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp_max=temp_min=current_max=nums[0]
        for i in nums[1:]:
            temp_max,temp_min=max(i,temp_max*i,temp_min*i),min(i,temp_max*i,temp_min*i)
            current_max=max(current_max,temp_max)
        return current_max