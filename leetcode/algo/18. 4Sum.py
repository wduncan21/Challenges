# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 15:17:47 2017

@author: lwang138
Given an array S of n integers, are there elements a, b, c, and d in S such 
that a + b + c + d = target? Find all unique quadruplets in the array which 
gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res=[]
        for i in range(len(nums)):
            if nums[i] > target/4.0:
                break
            temp=nums[:i]+nums[i+1:]
            Sum=target-nums[i]
            for j in range(len(temp)):
                l,r=j+1,len(temp)-1
                while l<r:
                    temp_sum=sum([temp[j],temp[l],temp[r]])
                    if temp_sum==Sum:
                        temp_res=[nums[i],temp[j],temp[l],temp[r]]
                        temp_res.sort()
                        if temp_res not in res:
                            res.append(temp_res)
                        while l<r and temp[l]==temp[l+1]:
                            l+=1
                        l+=1
                        while l<r and temp[r]==temp[r-1]:
                            r-=1
                        r-=1
                    elif temp_sum<Sum:
                        l+=1
                    else:
                        r-=1
                    if sum([temp[j],temp[l],temp[l+1]])>Sum or\
                    sum([temp[j],temp[r-1],temp[r]])<Sum:
                        break                     
        return res
        
S =[-490,-481,-471,-467,-453,-450,-446,-440,-437,-424,-423,-391,-384,-373,-358,-332,-318,-314,-311,-309,-299,-279,-270,-257,-243,-208,-205,-171,-153,-147,-142,-138,-129,-99,-20,-19,17,30,44,82,86,93,122,125,138,139,158,169,175,181,199,200,203,203,205,225,248,272,277,306,334,335,337,338,342,344,359,396,403,405,412,434,437,439,440,441,443,446,446,457,465,468,473,496]
a=Solution()
a.fourSum(S,1896)