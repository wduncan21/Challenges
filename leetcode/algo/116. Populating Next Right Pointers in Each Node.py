# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 20:19:05 2017

@author: Mr.

ven a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next 
right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same
 level, and every parent has two children).
For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
"""
# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect2(self, root):
        level=[root]
        while level[0]:           
            next_level=[]
            for i in range(len(level[:-1])):
                level[i].next=level[i+1]
                next_level.extend([level[i].left,level[i].right])
            level[-1].next=None
            next_level.extend([level[-1].left,level[-1].right])
            level=next_level
            
    def connect(self,root):
        while root and root.left:
            next_level=root.left
            while root:
                root.left.next=root.right
                root.right.next=root.next and root.next.left
                root=root.next
            root=next_level