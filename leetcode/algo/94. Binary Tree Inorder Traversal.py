# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 15:47:19 2017

@author: lwang138

Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res=[root.val]
        if root.left:
            res=self.inorderTraversal(root.left)+res
        if root.right:
            res.extend(self.inorderTraversal(root.right))
        return res
                