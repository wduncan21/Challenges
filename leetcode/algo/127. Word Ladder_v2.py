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
        query={beginWord:beginWord}
        i=2
        n=len(wordList)
        dic={}
        explored={}
        for j in wordList:
            dic[j]=j
        while i<=n:
            next_query={}
            next_wordList=dic.copy()
            for word in query.keys():
                for candy in dic.keys():
                    if candy not in explored:
                        if sum(word[i]!=candy[i] for i in range(len(word)))==1:
                            explored[candy]=1
                            if candy==endWord:
                                return i
                            if candy not in next_query:
                                next_query[candy]=candy
                            if candy in next_wordList:
                                next_wordList.pop(candy)
            i+=1
            query=next_query
            dic=next_wordList
        return 0
        
a=Solution()
beginWord="hit"
endWord="cog"
wordList=["hot","dot","dog","lot","log","cog"]
print(a.ladderLength(beginWord, endWord, wordList))