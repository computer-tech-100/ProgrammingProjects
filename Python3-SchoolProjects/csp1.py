#!/usr/bin/env python
#coding: utf-8
#In[3]:

#question1
import random

class my_dictionary(dict):

    #init function
    def init(self):
        self = dict()

    #Function to add key:value
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
                graph[firstMember].append(secondMember)
                graph[secondMember].append(firstMember)

    return graph

numberOfNodes = 7
probability = 0.20
print(rand_graph(numberOfNodes, probability))  #call the function
