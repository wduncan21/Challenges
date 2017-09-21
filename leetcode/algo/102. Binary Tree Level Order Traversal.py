# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 15:35:40 2017

@author: lwang138
Given a binary tree, return the level order traversal of its nodes' values. 
(ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res=[[root.val]]
        struc=[[root]]
        level=0
        while struc[level]:
            temp_res=[]
            temp_struc=[]
            for i in struc[level]:
                if i:
                    temp_struc.extend([i.left,i.right])
                    if i.left:
                        temp_res.append(i.left.val)
                    if i.right:
                        temp_res.append(i.right.val)

            level+=1
            struc.append(temp_struc)
            res.append(temp_res)
        return res[:-2]
        
    def levelOrder2(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res=[]
        level=[root]
        while level:
            temp_res=[]
            temp_level=[]
            for i in level:
                temp_res.append(i.val)
                if i.left:
                    temp_level.append(i.left)
                if i.right:
                    temp_level.append(i.right)

            level=temp_level
            res.append(temp_res)
        return res