# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 20:46:36 2017

@author: Mr.Wang
"""

"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity 
should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        lower1=0
        upper1=len(nums1)
        lower2=0
        upper2=len(nums2)
        med1=int((lower1+upper1)/2)
        med2=int((lower2+upper2)/2)
        med=med1+med2
        if nums1[med1]==nums2[med2]:
            return nums1[med1]
        elif nums1[med1]>nums2[med2]:
            upper1=med1
            med1=int((lower1+upper1)/2)
            lower2=med2
            med2=int((lower2+upper2)/2)
        else:
            lower1=med1
            med1=int((lower1+upper1)/2)
            upper2=med2
            med2=int((lower2+upper2)/2)