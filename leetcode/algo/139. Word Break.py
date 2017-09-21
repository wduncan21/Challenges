# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 20:41:07 2017

@author: Mr.Wang
Given a non-empty string s and a dictionary wordDict containing a list of 
non-empty words, determine if s can be segmented into a space-separated 
sequence of one or more dictionary words. You may assume the dictionary does 
not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

UPDATE (2017/1/4):
The wordDict parameter had been changed to a list of strings (instead of a 
set of strings). Please reload the code definition to get the latest changes.

"""

class Solution(object):
    def wordBreak2(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        res=[True]+[False]*len(s)
        for i in range(1,len(s)+1):
            for word in wordDict:
                length=len(word)
                if res[i-length]==True and word==s[i-length:i]:
                    res[i]=True
        return res[-1]

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        ok=[True]
        for i in range(1,len(s)+1):
            test=[ok[j] and s[j:i] in wordDict for j in range(i)]
            ok+=any(test),
        return ok[-1]

a=Solution()
s = "leetcode"
wordDict = ["leet", "code"]
print(a.wordBreak(s,wordDict))