#!/usr/bin/env python
#coding: utf-8
#In[3]:

#question 2
import random

class my_dictionary(dict):

    # init function
    def init(self):
        self = dict()

        # Function to add key:value
    def add(self, key, value):
        self[key] = value

def rand_graph(n, p):
    
    # n is number of the nodes
    # p is probability of an edge
    
    graph = my_dictionary()
    for firstMember in range(0, n):
        for secondMember in range(firstMember + 1, n):
            if firstMember not in graph:
                graph.add(firstMember,[])
            if secondMember not in graph:
                graph.add(secondMember,[])
            if random.random() < p:
                graph[firstMember].append(secondMember);
                graph[secondMember].append(firstMember);

    return graph

def check_teams(graph, csp_sol):

    if len(csp_sol) != len(graph):
        return False

    teams= my_dictionary()

    for i in csp_sol:
        if csp_sol[i] not in teams:
            teams.add(csp_sol[i], [])
        teams[csp_sol[i]].append(i)

    for i in teams:
        members = teams[i]
        for firstMember in range(0,len(members)):
            for secondMember in range(1,len(members)):
                if members[secondMember] in graph[members[firstMember]]:
                    return False

    return True;

numberOfNodes = 4
probability = 0.20
g= rand_graph(numberOfNodes, probability)  # call the function
#print(g)
x = {0:0, 1:1, 2:1, 3:0}
print(check_teams(g, x))
