# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 19:53:04 2017

@author: Mr.Wang

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            mid=inorder.index(preorder.pop(0))
            root=TreeNode(inorder[mid])
            root.left=self.buildTree(preorder,inorder[:mid])
            root.right=self.buildTree(preorder,inorder[mid+1:])
            return root