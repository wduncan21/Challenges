# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 15:15:24 2017

@author: lwang138

Given two words (beginWord and endWord), and a dictionary's word list, find 
the length of shortest transformation sequence from beginWord to endWord, such
 that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not 
a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
UPDATE (2017/1/20):
The wordList parameter had been changed to a list of strings (instead of a 
set of strings). Please reload the code definition to get the latest changes.
"""
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        dic={}
        for i in wordList:
            for j in wordList:
                if self.helper(i,j):
                    if i not in dic:
                        dic[i]=[j]
                    else:
                        dic[i].append(j)
        for j in wordList:
            if self.helper(beginWord,j):
                if i not in dic:
                    dic[beginWord]=[j]
                else:
                    dic[beginWord].append(j)
                    
        length=2
        match=True
        words=[beginWord]
        while wordList and match:
            match=False
            temp_a=words[:]
            temp_b=wordList[:]
            for word in temp_a:
                for i in temp_b:
                    if self.helper(word,i):
                        match=True
                        if i not in words:
                            words.append(i)
                        if i in wordList:
                            wordList.remove(i)
                words.remove(word)            
            if endWord in words:
                return length
            length+=1
        return 0
    def helper(self,a,b):
        diff=0
        for i in range(len(a)):
            if a[i]!=b[i]:
                diff+=1
                if diff>1 or diff==0:
                    return False
        return True
        
a=Solution()
beginWord="hit"
endWord="cog"
wordList=["hot","dot","dog","lot","log","cog"]
print(a.ladderLength(beginWord, endWord, wordList))