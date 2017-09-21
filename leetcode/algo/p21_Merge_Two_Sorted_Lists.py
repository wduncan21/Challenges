# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 21:20:54 2017

@author: Mr.Wang
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        holder = ListNode(0)
        temp=holder
        while l1!=None and l2!=None:
            if l1.val<l2.val:
                temp.next=l1
                l1=l1.next
            else:
                temp.next=l2
                l2=l2.next
            temp=temp.next
        if l1!=None:
            temp.next=l1
        else:
            temp.next=l2
        return holder.next