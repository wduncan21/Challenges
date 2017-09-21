# -*- coding: utf-8 -*-
"""
Created on Wed May 17 23:08:43 2017

@author: Mr.Wang
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        length=[]
        if len(strs)==0:
            return ""
        ##loop through to get the length of all strings, use the shortest one as search start
        for i in strs:
            temp_len=len(i)
            length.append(temp_len)
        search_id=length.index(min(length))
        ##do a binary search
        current_length=last_length=int((length[search_id]+1)/2)
        current_long_pre=last_long_pre=strs[search_id][0:current_length]
        match_all=True
        mismatch_id=0
            ##loop to test if the current prefix is common in all peps
        for i in range(len(strs)):
            if strs[i][0:current_length]!=current_long_pre:
                match_all=False
                mismatch_id=i
                break
        while True:

            last_length=current_length
            last_long_pre=current_long_pre
            step=int((last_length+1)/2)
            ## if not matching all, need to reduce the length, else extend it
            if match_all==False:
                current_length=step
            else:
                current_length=last_length+step                    
            current_long_pre=strs[search_id][0:current_length]
            for i in range(mismatch_id,len(strs)):
                if strs[i][0:current_length]!=current_long_pre:
                    match_all=False
                    mismatch_id=i
                    break
            if step==1:
                if match_all==False:
                    return last_long_pre
                else:
                    return current_long_pre
            match_all=True