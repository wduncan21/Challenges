# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 14:45:35 2017

@author: lwang138
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
"""
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res=''
        M=['','M','MM','MMM']
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        res+=M[int(num/1000)]
        res+=C[int((num%1000)/100)]
        res+=X[int((num%100)/10)]
        res+=I[num%10]
        return res
        