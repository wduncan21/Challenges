# -*- coding: utf-8 -*-
"""
Created on Sun May 14 22:59:32 2017

@author: Mr.Wang
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d={}
        for rank_id,num in enumerate(nums):
            if target-num in d:
                return d[target-num],rank_id
            d[num]=rank_id