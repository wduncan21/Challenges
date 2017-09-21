# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 14:39:55 2017

@author: lwang138
A gene string can be represented by an 8-character long string, with choices 
from "A", "C", "G", "T".

Suppose we need to investigate about a mutation (mutation from "start" to 
"end"), where ONE mutation is defined as ONE single character changed in the
 gene string.

For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.

Also, there is a given gene "bank", which records all the valid gene mutations.
 A gene must be in the bank to make it a valid gene string.

Now, given 3 things - start, end, bank, your task is to determine what is the 
minimum number of mutations needed to mutate from "start" to "end". If there is
 no such a mutation, return -1.

Note:

Starting point is assumed to be valid, so it might not be included in the bank.
If multiple mutations are needed, all mutations during in the sequence must be
 valid.
You may assume start and end string is not the same.
Example 1:

start: "AACCGGTT"
end:   "AACCGGTA"
bank: ["AACCGGTA"]

return: 1
Example 2:

start: "AACCGGTT"
end:   "AAACGGTA"
bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

return: 2
Example 3:

start: "AAAAACCC"
end:   "AACCCCCC"
bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]

return: 3
"""

class Solution(object):
    def minMutation(self, start, end, bank):
        if end not in bank:
            return -1
        query=[start]
        i=1
        n=len(bank)
        explored={end:1}
        while i<=n:
            next_query=[]
            while query:
                query_seq=query.pop()
                for bank_seq in bank:
                    if bank_seq not in query:
                        if sum(query_seq[i] != bank_seq[i] for i in range(8)) == 1:
                            if bank_seq==end:
                                return i
                            if bank_seq not in explored:
                                explored[bank_seq]=1
                                next_query.append(bank_seq)
            i+=1
            query=next_query[:]
        return -1
        
