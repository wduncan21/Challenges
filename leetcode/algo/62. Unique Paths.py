# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 21:10:42 2017

@author: Mr.Wang

A robot is located at the top-left corner of a m x n grid (marked 'Start' in 
the diagram below).

The robot can only move either down or right at any point in time. The robot 
is trying to reach the bottom-right corner of the grid (marked 'Finish' in 
the diagram below).

How many possible unique paths are there?


Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

"""
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if not m or not n:
            return 0
        result=[[1 for i in range(n)] for i in range(m)]
        for a in range(1,m):
            for b in range(1,n):
                result[a][b]=result[a-1][b]+result[a][b-1]
        return result[m-1][n-1]