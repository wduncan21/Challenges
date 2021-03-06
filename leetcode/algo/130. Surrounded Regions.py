# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 19:22:47 2017

@author: Mr.Wang

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions
 surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
"""
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m,n=len(board),len(board[0])
        save = list(set([ij for k in range(max(m,n)) for ij in ((0, k), (m-1, k), (k, 0), (k, n-1))]))
        while save:
            i,j=save.pop()
            if 0<=i<m and 0<=j<n and board[i][j]=='O':
                board[i][j]='S'
                save.extend([(i-1,j),(i+1,j),(i,j-1),(i,j+1)])
        for row in board:
            for i in range(len(row)):
                row[i]='XO'[row[i]=='S']
        