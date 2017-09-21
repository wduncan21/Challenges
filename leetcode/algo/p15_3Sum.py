# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 22:21:15 2017

@author: Mr.Wang
"""

"""
Given an array S of n integers, are there elements a, b, c in S such that 
a + b + c = 0? Find all unique triplets in the array which gives the sum of 
zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        solutions=[]
        nums.sort()
        length=len(nums)
        list1=[-x for x in nums]
        for sum_id in range(length):
            dict={}
            temp_num=nums[:]
            temp_num.pop(-(length-sum_id))
            for i in temp_num:
                if list1[sum_id]-i not in dict:
                    dict[i]=i
                else:
                    temp_sol=sorted([nums[sum_id],i,dict[list1[sum_id]-i]])
                    if temp_sol not in solutions:
                        solutions.append(temp_sol)
        return solutions
                
    def threeSum2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        solutions=[]
        nums.sort()
        for i in range(0,len(nums)-2):
            if i and nums[i]==nums[i-1]:
                continue
            target=0-nums[i]
            l,r=i+1,len(nums)-1
            while l<r:
                if nums[l]+nums[r]<target:
                    l+=1
                elif nums[l]+nums[r]>target:
                    r-=1
                else:
                    result=[nums[i],nums[l],nums[r]]
                    solutions.append(result)
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
        return solutions
        