# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 22:35:24 2017

@author: Mr.Wang

Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
"""
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        res={}
        for i in range(len(board)):
            for j in range(len(board[i])):
                dic1='h'+str(i)
                dic2='v'+str(j)
                dic3=str(int(i/3))+str(int(j/3))
                if board[i][j]=='.':
                    continue
                for dic in [dic1,dic2,dic3]:
                    if dic in res:
                        if board[i][j] in res[dic]:
                            return False
                        else:
                            res[dic].append(board[i][j])
                    else: 
                        res[dic]=[board[i][j]]
        return True