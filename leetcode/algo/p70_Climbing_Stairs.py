# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 19:34:17 2017

@author: Mr.Wang
"""

"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can 
you climb to the top?

Note: Given n will be a positive integer.
"""
## Top down with dictionary to memoriz already solved n
class Solution(object):
    def __init__(self):
        self.solved={1:1,2:2}
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n not in self.solved:
            self.solved[n]=self.climbStairs(n-1)+self.climbStairs(n-2)
        return self.solved[n]

## Bottom up approach 
class Solution2(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        larger=2
        smaller=1
        for i in range(n-1):
            larger,smaller=larger+smaller,larger
        return smaller

