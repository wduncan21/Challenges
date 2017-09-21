# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 22:57:28 2017

@author: Mr.Wang

Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        if len(nums)>1:
            for i in range(len(nums)):
                temp=nums.copy()
                num=temp.pop(i)
                post=self.permute(temp)
                #pre=post.copy()
                [i.append(num) for i in post]
                #[i.insert(0,num) for i in pre]
                #res.append(pre)
                res.extend(post)
        else:
            res=[nums]
        return res
            
        
a=Solution()
a.permute([1,2])