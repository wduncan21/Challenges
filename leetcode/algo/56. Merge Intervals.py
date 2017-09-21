# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 11:54:09 2017

@author: lwang138
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        sorted_int=sorted(intervals,key=lambda i:i.start)
        res=[]
        for i in sorted_int:
            if res and res[-1].end>=i.start:
                res[-1].end=max(i.end,res[-1].end)
            else:
                res.append(i)
        return res