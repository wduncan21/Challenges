# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 14:13:40 2017

@author: lwang138

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(i,j,board,word):
                    return True
        return False
    
    def dfs(self,i,j,board,word):
        if len(word)==0:
            return True
        if i<0 or i>len(board)-1 or j<0 or j>len(board[0])-1 or word[0]!=board[i][j]:
            return False
        temp,board[i][j]=board[i][j],''
        res= self.dfs(i+1,j,board,word[1:]) or self.dfs(i,j+1,board,word[1:]) or\
        self.dfs(i-1,j,board,word[1:]) or self.dfs(i,j-1,board,word[1:])
        board[i][j]=temp
        return res
        
a=Solution()
board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
a.exist(board,"ABCCED")
a.exist(board,"SEE")
a.exist(board,"ABCB")
