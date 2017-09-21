# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 12:23:58 2017

@author: lwang138
Given a m x n matrix, if an element is 0, set its entire row and column to 
0. Do it in place.
"""
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        loc=[]
        for row in range(len(matrix)):
            for column in range(len(matrix[row])):
                if matrix[row][column]==0:
                    loc.append([row,column])
        for i in loc:
            matrix[i[0]]=[0]*len(matrix[i[0]])
            for j in range(len(matrix)):
                matrix[j][i[1]]=0
        