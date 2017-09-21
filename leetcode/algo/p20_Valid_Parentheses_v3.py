# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 20:11:37 2017

@author: Mr.Wang
"""



class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ## if length is odd, return False, cause has to be equal
        if len(s)%2==1:
            return False
        valid={'(': ')', '{':'}', '[' : ']'}
        holder=[]
        ## check and hold s[0]
        if s[0] in valid.keys():
            holder.append(s[0])
        else:
            return False
        
        ## for each element in s, if is in key, add to holder, else, check if the same with the last holder item,
        ## if true, delete the last holder item, which equals to deleting the whole '{}'
        for i in range(1,len(s)):
                if s[i] in valid.keys():
                    holder.append(s[i])
                elif valid[holder[-1]]==s[i]:
                    holder.pop()
                else: 
                    ## if not a key and not equal to last holder item, then not valid
                    return False
                    
        ## after go through the whole list, if any keys left in holder ,return false
        if len(holder)>0:
            return False
        return True