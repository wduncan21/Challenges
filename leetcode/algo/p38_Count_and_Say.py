# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 22:37:24 2017

@author: Mr.Wang
"""

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1:
            return "1"
        if n==2:
            return "11"
        str="11"
        for i in range(2,n):
            temp=str[0]
            count=1
            temp_str=""
            for j in str[1:]:
                if j==temp:
                    count+=1
                else:
                    temp_str+=count.__str__()
                    temp_str+=temp
                    temp=j
                    count=1
            temp_str+=count.__str__()
            temp_str+=temp
            str=temp_str
        return str