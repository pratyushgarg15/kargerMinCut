# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 19:16:31 2019

@author: HP
"""

import random

def contract(edge):
    global graph
    
    #merging the edges of v2 into v1 and deleting v2
    l = graph[edge[0]]
    l.extend(graph[edge[1]])
    del graph[edge[1]]
    
    
    #Replace occurences of v2 with v1
    for vertex, edges in graph.items():
        for i in range(0,len(edges)):
            if(edges[i] == edge[1]):
                edges[i] = edge[0]
    
    #Removing occurences of self loops within v1
    graph[edge[0]] = [x for x in graph[edge[0]] if x != edge[0]]
    
    #print(edge[0],':',graph[edge[0]])
    

def random_edge():
    l = list(graph.keys())
    v1 = random.choice(l)
    v2 = random.choice(graph[v1])
    #print(v1,v2)
    
    '''print(v1,':',graph[v1])
    print(v2,':',graph[v2])'''
    return (v1,v2)

    
if __name__ == '__main__':
    
    mincut = []
    for i in range(0,20):
        n = 200 #number of vertices
        graph = {}

        with open("kargerMinCut.txt") as f:
            for i in range(0,n):
                l = [int(val) for val in f.readline().split('\t') if (val != '\n' and val != '')]
                graph[l[0]] = l[1:]
        
        while(len(graph)>2):
            contract(random_edge())
        
        '''Finding the len of list of edges from the remaining nodes 
           that indicate the mincut for a given iteration'''
        mincut.append(len(graph[list(graph.keys())[0]]))    
        
    print(min(mincut))        