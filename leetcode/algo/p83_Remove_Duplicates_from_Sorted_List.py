# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 22:40:01 2017

@author: Mr.Wang
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return []
        no_dup=ListNode(head.val)
        temp=no_dup
        while head.next is not None:
            if temp.val!=head.next.val:
                temp.next=head.next
                temp=temp.next
            head=head.next
        if temp.val==head.val:
            temp.next=None
        return no_dup