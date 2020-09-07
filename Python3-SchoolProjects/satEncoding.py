#!/usr/bin/env python
#coding: utf-8
#In[1]:

#question 1
import sys
import random
import os
import time
from random import choice

def make_queen_sat(N):
    
    #N=2
    #A=1,B=2,C=3,D=4
    if N==2:
        arr=[1,2,3,4]
        A=arr[0]
        B=arr[1]
        C=arr[2]
        D=arr[3]
        my_arr=[(A,B,0),(-A,-B,0),(C,D,0),(-C,-D,0),(A,C,0),(-A,-C,0),(B,D,0),(-B,-D,0),(A,D,0),(-A,-D,0),(B,C,0),(-B,-C,0)]
        for k in my_arr:
            organize1=str(k).replace(',','')
            print(str(organize1).strip('()'))
     
    #N=3
    #A=1, B=2, C=3, D=4, E=5, F=6 , G=7 , H=8, I=9
    elif N==3:
        a=[]
        b=[]
        c=[]
        arr=[1,2,3,0]
        x=arr[0]
        y=arr[1]
        z=arr[2]
        a.append([-x,-y,0])
        b.append([-x,-z,0])
        c.append([-y,-z,0])
    
        arr_1=str(arr).replace(',','')
        a_1=str(a).replace(',','') # remove camma
        b_1=str(b).replace(',','')
        c_1=str(c).replace(',','')
    
        for j in a:
            for k in j:
                organize1=str(k).replace(',','')
                organize2=str(organize1).strip('()') 
    
        print(str(arr_1).strip('[]'),"\n",str(a_1).strip('[]'),"\n",str(b_1).strip('[]'),"\n",str(c_1).strip('[]'))
     
        a=[]
        b=[]
        c=[]
  
        arr=[4,5,6,0]
    
        x=arr[0]
        y=arr[1]
        z=arr[2]
        a.append([-x,-y,0])
        b.append([-x,-z,0])
        c.append([-y,-z,0])
    
        arr_1=str(arr).replace(',','')
        a_1=str(a).replace(',','')
        b_1=str(b).replace(',','')
        c_1=str(c).replace(',','')
    
        for j in a:
            for k in j:
                organize1=str(k).replace(',','')
                organize2=str(organize1).strip('()')
   
        print(str(arr_1).strip('[]'),"\n",str(a_1).strip('[]'),"\n",str(b_1).strip('[]'),"\n",str(c_1).strip('[]'))
      
        a=[]
        b=[]
        c=[]

        arr=[7,8,9,0]

        x=arr[0]
        y=arr[1]
        z=arr[2]
        a.append([-x,-y,0])
        b.append([-x,-z,0])
        c.append([-y,-z,0])
    
        arr_1=str(arr).replace(',','')
        a_1=str(a).replace(',','')
        b_1=str(b).replace(',','')
        c_1=str(c).replace(',','')
    
        for j in a:
            for k in j:
                organize1=str(k).replace(',','')
                organize2=str(organize1).strip('()')

        print(str(arr_1).strip('[]'),"\n",str(a_1).strip('[]'),"\n",str(b_1).strip('[]'),"\n",str(c_1).strip('[]'))
    
        my_arr=[]
        my_arr2=[]
        my_arr3=[]
        my_arr4=[]
        my_arr5=[]
        
        for i in range(1,4):
            # we use sample in order to have unique elements that are random
            my_arr=random.sample(range(1,10),3)
            my_arr1=random.sample(range(1,10),3)
            my_arr2=random.sample(range(1,10),3)
            my_arr3=random.sample(range(1,10),3)
            my_arr4=random.sample(range(1,10),3)
            my_arr5=random.sample(range(1,10),3)
        
    #we should have 0 at the end of each clause (i.e at the end of each line)
        my_arr.append(0)
        my_arr2.append(0)
        my_arr3.append(0)
        my_arr4.append(0)
    
        a=[]
        b=[]
        c=[]
        x=my_arr[0]
        y=my_arr[1]
        z=my_arr[2]
        a.append([-x,-y,0])
        b.append([-x,-z,0])
        c.append([-y,-z,0])
        e=[]
        f=[]
        g=[]
        x=my_arr2[0]
        y=my_arr2[1]
        z=my_arr2[2]
        e.append([-x,-y,0])
        f.append([-x,-z,0])
        g.append([-y,-z,0])
        h=[]
        I=[]
        j=[]
        x=my_arr3[0]
        y=my_arr3[1]
        z=my_arr3[2]
        h.append([-x,-y,0])
        I.append([-x,-z,0])
        j.append([-y,-z,0])
    
        m=[]
        n=[]
        l=[]
        w=[]
        v=[]
        x=my_arr4[0]
        y=my_arr4[1]
        z=my_arr4[2]
        m.append([-x,-z,0])
        n.append([-y,-z,0])
        l.append([-y,-x,0])
        w.append([-z,-y,0])
        v.append([-x,-z,0])
    
        p=[]
        k=[]
        q=[]
        f=[]
        d=[]
        x=my_arr5[0]
        y=my_arr5[1]
        z=my_arr5[2]
        p.append([-x,-z,0])
        k.append([-y,-z,0])
        q.append([-y,-x,0])
        f.append([-z,-y,0])
        d.append([-x,-z,0])
    
        arr_1=str(my_arr).replace(',','')
        a_1=str(a).replace(',','')
        b_1=str(b).replace(',','')
        c_1=str(c).replace(',','')
        
        arr_2=str(my_arr2).replace(',','')
        e_1=str(e).replace(',','')
        f_1=str(f).replace(',','')
        g_1=str(g).replace(',','')
        
        arr_3=str(my_arr3).replace(',','')
        h_1=str(h).replace(',','')
        I_1=str(I).replace(',','')
        j_1=str(j).replace(',','')
    
        arr_4=str(my_arr4).replace(',','')
        m_1=str(m).replace(',','')
        n_1=str(n).replace(',','')
        l_1=str(l).replace(',','')
        w_1=str(w).replace(',','')
        v_1=str(v).replace(',','')
    
        arr_5=str(my_arr5).replace(',','')
        p_1=str(p).replace(',','')
        k_1=str(k).replace(',','')
        q_1=str(q).replace(',','')
        f_1=str(f).replace(',','')
        d_1=str(d).replace(',','')
    
        #by strip function we remove the brackets
        print(str(arr_1).strip('[]'),"\n",str(a_1).strip('[]'),"\n",str(b_1).strip('[]'),"\n",str(c_1).strip('[]'))
        print(str(arr_2).strip('[]'),"\n",str(e_1).strip('[]'),"\n",str(f_1).strip('[]'),"\n",str(g_1).strip('[]'))
        print(str(arr_3).strip('[]'),"\n",str(h_1).strip('[]'),"\n",str(I_1).strip('[]'),"\n",str(j_1).strip('[]'))
        print('',str(m_1).strip('[]'),"\n",str(n_1).strip('[]'),"\n",str(l_1).strip('[]'),"\n",str(w_1).strip('[]'),"\n",str(v_1).strip('[]'))
        print('',str(p_1).strip('[]'),"\n",str(k_1).strip('[]'),"\n",str(q_1).strip('[]'),"\n",str(f_1).strip('[]'),"\n",str(d_1).strip('[]'),"\n")
     
    # N > 3
    else:   
        my_arr = [] 
        def my_generator(place_holder,N):
            # we use choice function to get random numbers except zero 
            my_choice=choice([i for i in range(-N,N) if i!=0]) 
            for my_choice in place_holder:
                my_choice = choice([i for i in range(-N,N) if i!=0])
            return my_choice
        
        array_1=[N]
        A=my_generator(array_1,N)
        array_2=[A]
        B= my_generator(array_2,N)
        array_3=[A,B]
        C= my_generator(array_3,N)
        array_4=[A,B,C]
        D=my_generator(array_4,N)
        array_5=[A,B,C,D]
        E=my_generator(array_5,N)
        array_6=[A,B,C,D,E]
        F=my_generator(array_6,N)
        array_7=[A,B,C,D,E,F]
        G=my_generator(array_7,N)
        array_8=[A,B,C,D,E,F,G]
        H=my_generator(array_8,N)
        array_9=[A,B,C,D,E,F,G,H]
        I=my_generator(array_9,N)
        
        # 0 should be at the end of each line
        my_sat1=(A,B,C,0)
        my_sat2=(D,E,F,G,0)
        my_sat3=(H,I,A,0)
        my_sat4=(B,C,0)
        my_sat5=(D,E,D,0)
        my_sat6=(F,G,0)
        my_sat7=(H,I,A,0)
        my_sat8=(B,C,0)
        my_sat9=(D,E,0) 
        my_sat=[my_sat1,my_sat2,my_sat3,my_sat4,my_sat5,my_sat6,my_sat7,my_sat8,my_sat9]
        N=N*N
        for i in range(N):
            my_arr.append(my_sat)
            
        for j in my_arr:
            for k in j:
                organize1=str(k).replace(',','')
                organize2=str(organize1).strip('()')
                print(organize2)
            
# shows the results of make_queen_sat(N) function
def showResults(N):
    if N==2:
        print('c 2-queens problem',"\n","p cnf",N*N,12)
        make_queen_sat(N)
        
    elif N==3:
        print('c 3-queens problem',"\n","p cnf",N*N,34)
        make_queen_sat(N)
        
    elif N==4:
        print('c 4-queens problem',"\n","p cnf",N*N,84)
        make_queen_sat(N)
    else:
        print('c',N,'-queens problem',"\n","p cnf",N*N,N*(N+1)*N)
        make_queen_sat(N)
        
# N can be any number... here for example it is 3        
N=3      
showResults(N)        

def draw_queen_sat_sol(sol):
    
    sol=outPut_content.read()
    print(sol) # print output of minisat to screen
    
    if sol=="UNSATISFIABLE"or sol=="UNSAT":
        print("No solution")
        
     
    if len(sol)>40:
        print("too big: N must be less than 40")
    
print("These are outputs of minisat:\n")
outPut_content = open("output.txt", "r")
draw_queen_sat_sol(outPut_content)

print("\n")
outPut_content = open("out_sample1.txt", "r")
draw_queen_sat_sol(outPut_content)

print("\n")
outPut_content = open("out_sample2.txt", "r")
draw_queen_sat_sol(outPut_content)
