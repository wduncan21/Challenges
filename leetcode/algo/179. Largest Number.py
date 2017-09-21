# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 23:00:16 2017

@author: Mr.Wang
Given a list of non negative integers, arrange them such that they form the 
largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of 
an integer.
"""
from functools import cmp_to_key


class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        def mycmp(x, y):
            if x + y > y + x:
                return 1
            elif x == y:
                return 0
            else:
                return -1

        nums = list(map(str, nums))
        nums.sort(key=cmp_to_key(mycmp), reverse=True)
        return "".join(nums).lstrip("0") or "0"