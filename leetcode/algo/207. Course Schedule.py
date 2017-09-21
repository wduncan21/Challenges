# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 13:52:26 2017

@author: lwang138

There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to
 first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it
 possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have
 finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have 
finished course 0, and to take course 0 you should also have finished course
 1. So it is impossible.

Note:
The input prerequisites is a graph represented by a list of edges, not
 adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
"""
class Solution(object):
    def canFinish1(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        visit = [0 for _ in range(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)
        def dfs(i):
            if visit[i] == -1:
                return False
            if visit[i] == 1:
                return True
            visit[i] = -1
            for j in graph[i]:
                if not dfs(j):
                    return False
            visit[i] = 1
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
    def canFinish(self, numCourses, prerequisites):
                
        import collections
        dic={i:set() for i in range(numCourses)}
        neigh = collections.defaultdict(set)
        for i, j in prerequisites:
            dic[i].add(j)
            neigh[j].add(i)
        queue=collections.deque([i for i in dic if not dic[i]])
        res=[]
        while queue:
            current=queue.popleft()
            res.append(current)
            for i in neigh[current]:
                dic[i].remove(current)
                if not dic[i]:
                    queue.append(i)
        return True if len(res)==numCourses else False
        
numCourses, prerequisites=2, [[1,0],[0,1]]
a=Solution()
print(a.canFinish(numCourses, prerequisites))
                
        