# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 14:32:32 2017

@author: lwang138

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number 
of rows like this: (you may want to display this pattern in a fixed font for
 better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number
 of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows<=1:
            return s
        res=['' for i in range(numRows)]
        row=0
        direction=1
        for i in s:
            res[row]+=i
            row+=direction
            if row<0:
                row=1
                direction=1
            if row>=numRows:
                row=numRows-2
                direction=-1
        out=''
        for i in res:
            out+=i
        return out
        
s, numRows= "PAYPALISHIRING",3
a=Solution()
print(a.convert(s, numRows))
                