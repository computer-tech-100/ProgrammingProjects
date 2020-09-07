#!/usr/bin/env python
#coding: utf-8
#In[2]:

#question 4
#here in order to approximate solution we need to use min conflict csp 
from csp import *
import random
import time
import sys
#from  matplotlib import pyplot as plt

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

def find_number_of_teams(assignment):
    teams = my_dictionary()
    for member in assignment:
        team_index = assignment[member]
        if team_index not in teams:
            teams.add(team_index, [])
        teams[team_index].append(member)
        
    unassigned=[]
    assigned=assignment
    print("number of times CSP variables were assigned:",len(assigned))
    for i in assignment:
        if i not in assigned:
            unassigned.append(i)
    print("number of times CSP variables were unassigned:",len(unassigned))
    
    return len(teams)

def prepare_domains(number_of_nodes):
    domains = my_dictionary()
    for i in range(0, number_of_nodes):
        domains.add(i, [])
        for j in range(0, number_of_nodes):
            domains[i].append(j)
    return domains


arr=[] #in this array we keep minimum number of teams for all 5 graphs

def run_q4():
    
    n = 100
    graphs = [rand_graph(n, 0.1), rand_graph(n, 0.2), rand_graph(n, 0.3), rand_graph(n, 0.4), rand_graph(n, 0.5)]
    
    domains = prepare_domains(n)
    constraints = lambda X, x, Y, y: x != y

    for graph in graphs:

        csp = CSP(variables=None, domains=domains, neighbors=graph, constraints=constraints)
        startTime=time.time()
        
        result = min_conflicts(csp) #use min conflict to approximate
        
        numberOfTeams = find_number_of_teams(result)
        print("approximate solution for minimum number of the teams is:",numberOfTeams )#approximate
        print("solver running time in seconds:", time.time()-startTime )#time complexity
        print("memory usage of solver in bytes:",sys.getsizeof(result))#space complexity
        print("\n")
      
        arr.append(numberOfTeams)
    
#this function draws a graph for minimum number of the teams    
#def draw_teams():
    #t=[i for i in arr]
    #g=[j for j in range(5)]
    #plt.title("approximate solution for minimum number of teams (for 5 graphs)")
    #plt.xlabel("minimum number of teams")
    #plt.ylabel("random graph")
    #plt.plot(t,g)
    #plt.show()
        
run_q4() #call the function

#draw_teams()
