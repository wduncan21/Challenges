# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 16:12:47 2017

@author: lwang138
Given a binary tree, return the zigzag level order traversal of its nodes' 
values. (ie, from left to right, then right to left for the next level and 
alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""
class Solution(object):
    def zigzagLevelOrder2(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res=[[root.val]]
        struc=[[root]]
        level=0
        pos=False
        while struc[level]:
            temp_res=[]
            temp_struc=[]
            if pos:
                pos=False
                for i in struc[level][::-1]:
                    if i:
                        temp_struc.extend([i.left,i.right])
                        if i.left:
                            temp_res.append(i.left.val)
                        if i.right:
                            temp_res.append(i.right.val)
            else:
                pos=True
                for i in struc[level][::-1]:
                    if i:
                        temp_struc.extend([i.right,i.left])
                        if i.right:
                            temp_res.append(i.right.val)     
                        if i.left:
                            temp_res.append(i.left.val)
           
            level+=1
            struc.append(temp_struc)
            res.append(temp_res)
        return res[:-2]
        
        
    def zigzagLevelOrder3(self, root):
        if not root:
            return []
        level=[root]
        res=[]
        pos=False
        while level:
            next_level=[]                          
            res.append([i.val for i in level])
            if pos:
                pos=False
                for i in level[::-1]:
                    if i.left:
                        next_level.append(i.left)
                    if i.right:
                        next_level.append(i.right)
            else:
                pos=True
                for i in level[::-1]:
                    if i.right:
                        next_level.append(i.right)                 
                    if i.left:
                        next_level.append(i.left)
            level=next_level
        return res
        
    def zigzagLevelOrder4(self, root):
        res, level, direction = [], [root], 1
        while root and level:
            next_level=[]
            res.append([i.val for i in level][::direction])
            direction*=-1
            for i in level:
                if i.left:
                    next_level.append(i.left)
                if i.right:
                    next_level.append(i.right)
            level=next_level
        return res
        
    def zigzagLevelOrder(self, root):
        res, level, direction = [], [root], 1
        while root and level:
            res.append([i.val for i in level][::direction])
            direction*=-1
            level=[new for i in level for new in [i.left,i.right] if new]
        return res