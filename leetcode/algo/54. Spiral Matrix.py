# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 23:40:15 2017

@author: Mr.Wang
Given a matrix of m x n elements (m rows, n columns), return all elements of 
the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
"""
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res=[]

        while len(matrix)>0:            
            res.extend(matrix[0])
            matrix.pop(0)
            temp=matrix[:]
            temp[::]=zip(*matrix[::])
            temp[::-1]=zip(*matrix[::])
            matrix=temp

        return res
a=Solution()
print(a.spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]))
            