# -*- coding: utf-8 -*-
"""
Created on Wed May 17 22:48:01 2017

@author: Mr.Wang
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_pool={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        reverse_num=s[::-1]
        result=0
        result_temp=0
        for i in reverse_num:
            if dict_pool[i]>=result_temp:
                result+=dict_pool[i]
            else:
                result-=dict_pool[i]
            result_temp=dict_pool[i]
        return result
            
            
