# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 16:05:33 2017

@author: Mr.Wang
"""
"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        a=len(nums)
        mid=int(a/2)
        if nums[mid]>nums[0]:
            pivot='right'
        else:
            pivot='left'
        if pivot=='right' and target<nums[0]:
            return self.search(nums[mid:],target)+mid
        elif pivot=='right' and target>nums[0]:
            if target<nums[mid]:    
                return self.binary(nums[:mid],target)+0
            else:
                return self.search(nums[mid:],target)+mid
        elif pivot=='left' and target>nums[0]:
            return self.search(nums[:mid],target)+0
        else:
            if target<nums[mid]:
                return self.search(nums[:mid],target)+0
            else:
                return self.binary(nums[mid:],target)+mid
    def binary(self,list,target):
        l=0
        r=len(list)-1
        mid=int((l+r)/2)
        while r-l>1:
            if list[l]==target:
                return l
            if list[r]==target:
                return r
            if list[mid]<target:
                l=mid
            else:
                r=mid
        mid=int((l+r)/2)
        if list[mid]==target:
            return mid
        return -1