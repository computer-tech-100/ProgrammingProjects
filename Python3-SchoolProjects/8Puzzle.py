#!/usr/bin/env python
#coding: utf-8
#In[1]:
#a1.py
from search import *
from collections import defaultdict, deque
import math
import random
import sys
import bisect
from operator import itemgetter
from numpy import array
import time
import numpy as np
import copy

class Problem():
    
    def __init__(self,myPhase,actions,node,lenghtValue,heuristics,path_cost,maxTreeDepthValue):
       
        self.myPhase = myPhase
        self.actions = actions 
        self.node = node 
        self.lenghtValue = lenghtValue
        self.heuristics = heuristics
        self.path_cost = path_cost 
        self.maxTreeDepthValue = maxTreeDepthValue
        
    #we can use state instance along our program by calling this function
    def state_instance(self):
        myState=[self.myPhase]
        return myState
    
    #specify the positions of numbers in goal state in the 3*3 matrix
    def myGoalPhase(self):
        goal={
              1:(0,0),
              2:(0,1),
              3:(0,2),
              4:(1,0),
              5:(1,1),
              6:(1,2),
              7:(2,0),
              8:(2,1),
              0:(2,2)
             }
        return goal
    
    #this function shows created states which are result of doing actions
    def created_states(self):
        
        myState= self.state_instance()
        while self.node:
            self=self.node
            the_state=self.myPhase
            myState.append(the_state)

        while myState:
            print( '\n')
            moving = myState.pop()
            print (moving)

    #define each action which can be going to up,down,left,right
    def action(self,actions):
        mostRecent_state=copy.copy(self.myPhase)
        zeroState=self.myPhase
        zeroState2=np.where(zeroState==0)# we get index of each element when condition is satisfied
        first_index=[
            g[0] for g in zeroState2
                    ]
        zero_index=first_index   

        if  actions=='UP':
            cellOne=zero_index[0]
            cellTwo=cellOne+1
            cellThree=cellOne-1
            cellFour=zero_index[1]
            cellFive=cellOne+1
            cellSix=cellOne-1
            zero_index=first_index
               
            if cellOne != 2:
               
                mostRecent_state[cellOne,cellFour]=self.myPhase[cellTwo,cellFour]
                mostRecent_state[cellTwo,cellFour] = 0
                return mostRecent_state,self.myPhase[cellTwo,cellFour]  
            else:
                return None

        if  actions=='DOWN':
            aboveCell_1=zero_index[0]-1
            aboveCell_2=aboveCell_1+1
            aboveCell_3=zero_index[1]   
        
            if aboveCell_2 != 0:
              
                mostRecent_state[aboveCell_2,aboveCell_3]= self.myPhase[aboveCell_1,aboveCell_3]
                mostRecent_state[aboveCell_1,aboveCell_3] = 0
                return mostRecent_state,self.myPhase[aboveCell_1,aboveCell_3]
            else:
                return None

        if  actions=='LEFT':
            cellOne=zero_index[0]
            cellTwo=cellOne+1
            cellThree=cellOne-1
            cellFour=zero_index[1]
            cellFive=cellOne+1
            cellSix=cellOne-1
            cellSeven=cellFour+1
            
            if cellFour != 2:
               
                mostRecent_state[cellOne,cellFour] =self.myPhase[cellOne,cellSeven] 
                mostRecent_state[cellOne,cellSeven] = 0
                return mostRecent_state,self.myPhase[cellOne,cellSeven]
            
            else:
                return None

        if  actions=='RIGHT':
            cell_1=zero_index[0]
            cell_2=cell_1+1
            cell_3=zero_index[1]
            cell_4=cell_3-1
            cell_5=cell_3+1
            
            if cell_3 != 0:
              
                mostRecent_state[cell_1,cell_3] =  self.myPhase[cell_1,cell_4] 
                mostRecent_state[cell_1,cell_4] = 0
                return mostRecent_state,self.myPhase[cell_1,cell_4]
               
            else:
                return None
            
        val1=self.myPhase[cellTwo,cellFour]#UP
        val2= self.myPhase[aboveCell_1,aboveCell_3]#DOwn
        val3 = self.myPhase[cellOne,cellSeven]#LEFT
        val4= self.myPhase[cell_1,cell_4]#RIGHT  
                     
class EightPuzzle(Problem):
    
    def __init__(self,myPhase,actions,node,lenghtValue,heuristics,path_cost,maxTreeDepthValue):
       
        Problem.__init__(self,myPhase,actions,node,lenghtValue,heuristics,path_cost,maxTreeDepthValue)      
        
    def find_blank_square(self, state):
        """Return the index of the blank square in a given state"""
     
        return state.index(0)

    def possible_actions(self,last_state,heuristic_function):
        
        possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT'] 
        start_time = time.time()
        frontier= [(self,None)]
        distance= [(1,1)] #from root
        extension=[(1,1)] # from root
        exploredNodes = [] #make set
        lenghtOfFrontier=len(frontier) 
        maxLenOfFrontier=2
        numberOfRemovedNodes=1 # number of nodes removed from frontier ( suppose root node was removed)
       
        while True:
            
            def firstIndex(a):
                return a[1]
              
            firstNodeRemoved= frontier.pop(0)[0] # pop off first node
            reshape=firstNodeRemoved.myPhase.reshape(1,9)[0]
            reshape=tuple(reshape)
     
            exploredNodes.append(reshape)
            frontier= sorted(frontier,key=firstIndex)
          
            numberOfRemovedNodes=numberOfRemovedNodes + 1
 
            my_time= time.time()-start_time
            
            def pathFromRoot():
                x=firstNodeRemoved.created_states()
                return x         
                
            if (firstNodeRemoved.myPhase==last_state).all():
                pathFromRoot()
           
                print('total running time is: %0.2fs' % my_time)
                print(int(str(len(frontier))[:1]),'is length of  the solution')
                print(int(str(numberOfRemovedNodes)[:1]),'is total number of nodes that were removed from the frontier.\n')
                return True

            else: 

                if  firstNodeRemoved.action(actions='UP'):
                    mostRecent_state, val1 = firstNodeRemoved.action(actions='UP')
                    myReshape=mostRecent_state.reshape(1,9)[0]
                    NotChecked=tuple(myReshape)
  
                    if  not NotChecked in exploredNodes :
                        edgeValue= distance.pop(0)[0]
                        edgeValue+=val1
                        d_Val= sorted(extension, key=firstIndex).pop(0)[0] 
                        d_Val+=1
                        def functionV():
                            functionVal = self.my_heuristics(mostRecent_state,last_state,heuristic_function)
                            return functionVal
                        funcV=functionV()
                        sumOfValues = edgeValue
                        sumOfValues +=funcV
                        sorted(extension, key=firstIndex).append((d_Val, sumOfValues))
                        distance.append((edgeValue,sumOfValues ))
                        def goingUp():
                            firstNodeRemoved.goingUp = Problem(myPhase=mostRecent_state,
                                                               node=firstNodeRemoved,actions='up',
                                                               maxTreeDepthValue=d_Val,
                                                               lenghtValue=val1,
                                                               path_cost=edgeValue,heuristics=funcV)
                            go_up=firstNodeRemoved.goingUp
                            return go_up
                        u=goingUp()
                        frontier.append((u, sumOfValues))       

                if firstNodeRemoved.action(actions='DOWN'):
                    mostRecent_state,val2 = firstNodeRemoved.action(actions='DOWN')
                
                    myReshape=mostRecent_state.reshape(1,9)[0]
                    NotChecked=tuple(myReshape)
                    if not NotChecked in exploredNodes :
                        edgeValue= distance.pop(0)[0]
                        edgeValue+=val2
                        d_Val= sorted(extension, key=firstIndex).pop(0)[0] 
                        d_Val+=1
                        def functionV():
                            functionVal = self.my_heuristics(mostRecent_state,last_state,heuristic_function)
                            return functionVal
                        funcV=functionV()
                        sumOfValues= edgeValue
                        sumOfValues+=funcV
                        sorted(extension, key=firstIndex).append((d_Val, sumOfValues))
                        distance.append((edgeValue, sumOfValues))
                        def goingDown():
                            firstNodeRemoved.going_down = Problem(myPhase=mostRecent_state,
                                                                  node=firstNodeRemoved,actions='down',
                                                                  maxTreeDepthValue=d_Val,lenghtValue=val2,
                                                                  path_cost=edgeValue,heuristics=funcV)
                            go_down=firstNodeRemoved.going_down
                            return go_down
                        d=goingDown()
                        frontier.append((d, sumOfValues))   
                        
                if firstNodeRemoved.action(actions='LEFT'):
                    mostRecent_state,val3 = firstNodeRemoved.action(actions='LEFT')
                    myReshape=mostRecent_state.reshape(1,9)[0]
                    NotChecked=tuple(myReshape)

                    if not NotChecked in exploredNodes :
                        edgeValue= distance.pop(0)[0]
                        edgeValue+=val3
                        d_Val = sorted(extension, key=firstIndex).pop(0)[0] 
                        d_Val+=1
                        def functionV():
                            functionVal = self.my_heuristics(mostRecent_state,last_state,heuristic_function)
                            return functionVal
                        funcV=functionV()
                        sumOfValues = edgeValue
                        sumOfValues+=funcV
                        sorted(extension, key=firstIndex).append((d_Val, sumOfValues))
                        distance.append((edgeValue,sumOfValues))
                        def goingLeft():
                            firstNodeRemoved.going_left = Problem(myPhase=mostRecent_state,
                                                                  node=firstNodeRemoved,actions='left',
                                                                  maxTreeDepthValue=d_Val,lenghtValue=val3,
                                                                  path_cost=edgeValue,heuristics=funcV)
                            go_left=firstNodeRemoved.going_left
                            return go_left
                        l=goingLeft()
                        frontier.append((l, sumOfValues))
       
                if firstNodeRemoved.action(actions='RIGHT'):
                    mostRecent_state,val4 = firstNodeRemoved.action(actions='RIGHT')
                    myReshape=mostRecent_state.reshape(1,9)[0]
                    NotChecked=tuple(myReshape)
                  
                    if not NotChecked in exploredNodes :
                        edgeValue= distance.pop(0)[0]
                        edgeValue+=val4
                        d_Val = sorted(extension, key=firstIndex).pop(0)[0] 
                        d_Val+=1
                        def functionV():
                            functionVal = self.my_heuristics(mostRecent_state,last_state,heuristic_function)
                            return functionVal
                        funcV=functionV()
                        sumOfValues= edgeValue
                        sumOfValues+=funcV
                        sorted(extension, key=firstIndex).append((d_Val,sumOfValues))
                        distance.append((edgeValue,sumOfValues ))
                        def goingRight():
                            firstNodeRemoved.going_right =Problem(myPhase=mostRecent_state,
                                                                  node=firstNodeRemoved,actions='right',
                                                                  maxTreeDepthValue=d_Val,lenghtValue=val4,
                                                                  path_cost=edgeValue,heuristics=funcV)
                            go_right=firstNodeRemoved.going_right
                            return go_right
                        r=goingRight()
                        frontier.append((r, sumOfValues))

        return possible_actions

    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """

        # blank is the index of the blank square
        blank = self.find_blank_square(state)
        new_state = list(state)

        delta = {'UP':-3, 'DOWN':3, 'LEFT':-1, 'RIGHT':1}
        neighbor = blank + delta[action]
     
        new_state[blank], new_state[neighbor] = new_state[neighbor], new_state[blank]

        return tuple(new_state)
        
    def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """
     
        return state == self.goal

    def check_solvability(self, state):
        """ Checks if the given state is solvable """
        self.state=state
        state=[]
    
        inversion = 0
        for i in range(len(state)):
            for j in range(i+1, len(state)):
                if (state[i] > state[j]) and state[i] != 0 and state[j]!= 0:
                    inversion += 1
                    
        solvable = inversion % 2 == 0
        
        if solvable:
            print("puzzle is solvable\n")
        else:
            print("puzzle is not solvable")
            
        return solvable
  
    def display(self,state):
        
        self.state=state
        myMatrix = state
        
        my_array = enumerate(myMatrix) 
        for m,n in my_array:
    
            if n==0:
                myMatrix[m]="*"
    
        my_range=range(0,len(myMatrix),3)
        matrix = [
           myMatrix[i:i+3]  for i in my_range
                 ]
                 
        for j in matrix:
            print(j)
    
    def make_rand_8puzzle(self):
        my_list = [1,2,3,4,8,0,7,6,5]
        random.shuffle(my_list) #make random list
        print("question 1 :\n")
        print('This is my random initial state:',my_list)
        print('\n')
        print('This is my state showing as 3*3 matrix and 0 is replaced by *:')
        self.display(my_list)
        state=self.check_solvability(my_list) # check if the generated random puzzle is solvable
      
    #this function specifies kind of heuristic function
    def my_heuristics(self,myState,lastState,my_HeuristicAlgorithm):
        
        myRange=range(3)
        lastPhase=self.myGoalPhase()
 
        if my_HeuristicAlgorithm == 'Misplaced_Tile_Heuristic':
            if sum(myState != lastState).all()-1 < 0:
                return 0
            else:
                return sum(myState != lastState).all()-1

        if my_HeuristicAlgorithm == 'Manhattan_Distance_Heuristic':

            for y in myRange:
                for z in myRange:
                    if myState[y,z] == 0:
                        return False
                    else: 
                        my_lastPhase=lastPhase[myState[y,z]]
                        compression=zip((y,z), my_lastPhase)
                        my_manhattan=0
                        my_sum=sum(abs(m-n) for m,n in compression)
                        my_manhattan =my_manhattan + my_sum
                        return my_manhattan

        if my_HeuristicAlgorithm == 'Max_of_Manhattan_and_Misplaced':
            if sum(myState != lastState).all()-1 < 0:
                return 0
            else:
                return sum(myState != lastState).all()-1

            for y in myRange:
                for z in myRange:
                    if myState[y,z]==0:
                        return False
                    else: 
                        my_lastPhase=lastPhase[myState[y,z]]
                        compression=zip((y,z), my_lastPhase)
                        my_manhattan=0
                        my_sum=sum(abs(m-n) for m,n in compression)
                        my_manhattan =my_manhattan + my_sum
  
            valueMisplaced=value2
            manhattan=my_manhattan
            maximumVal=max(valueMisplaced,manhattan)
            return maximumVal            

    def display2(self,myPhase=[]):
        
        myFirstArray=self.myPhase
        print("Question2:\n")
        print('The beginning state is:')
        myMatrix= [myFirstArray[i:i+3] for i in range (0,len(myFirstArray),3)]
        for j in myMatrix:
            print(j)
        print('\n')
        print('Then the goal state should be:')
        last = [1,2,3,4,5,6,7,8,0] # our goal state
        mmatrix=[last[i:i+3]for i in range(0,len(last),3)]         
        for l in mmatrix:
            print(l,)
        print('\n')
        
        #replacing 0 with star
        #my_array = enumerate(myFirstArray) 
        #for m,n in my_array:
    
            #if n==0:
                #myFirstArray[m]="*"

        state=self.check_solvability(myFirstArray)
        first_state = array(myFirstArray)
        first_state=first_state.reshape(3,3) 
        last_state=array(last)
        last_state=last_state.reshape(3,3)

        puzzle=EightPuzzle(first_state,0,0,0,0,0,0)

        print('solve the puzzle:\n')
   
        print('This is misplaced tile heuristic:')
        puzzle.possible_actions(last_state,'Misplaced_Tile_Heuristic')

        print('This is Manhattan distance heuristic:')
        puzzle.possible_actions(last_state,'Manhattan_Distance_Heuristic')

        print('This is max of the misplaced tile heuristic and the Manhattan distance heuristic:')
        puzzle.possible_actions(last_state,'Max_of_Manhattan_and_Misplaced')
  
#Question1        
my_random_puzzle=EightPuzzle(0,0,0,0,0,0,0) # create object
my_random_puzzle.make_rand_8puzzle()

#Question2
myFirstArray=[3,4,5,1,2,6,0,7,8] 
myResults=EightPuzzle(myFirstArray,0,0,0,0,0,0) #create object of class
myResults.display2(myFirstArray)
