# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 23:16:36 2017

@author: Mr.Wang

iven a 2d grid map of '1's (land) and '0's (water), count the number of
 islands. An island is surrounded by water and is formed by connecting 
 adjacent lands horizontally or vertically. You may assume all four edges of
 the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
"""
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        explored=[[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        island=0
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                if explored[j][i]==0:
                    if grid[j][i]=='1':
                        island+=1
                        self.helper(grid,explored,i,j)
        return island

    def helper(self,grid,explored,i,j):
        if 0<=i<len(explored[0]) and 0<=j<len(explored) and explored[j][i]==0:
            explored[j][i]=1
            if grid[j][i]=='1':
                self.helper(grid,explored,i+1,j)
                self.helper(grid,explored,i,j+1)
                self.helper(grid,explored,i-1,j)
                self.helper(grid,explored,i,j-1)
            else:
                explored[j][i]=1

grid=['11110',
'11010',
'11000',
'00000']
grid2=['11000',
'11000',
'00100',
'00011'
]
grid3=[]
a=Solution()
print(a.numIslands(grid))
print(a.numIslands(grid2))

print(a.numIslands(grid3))
