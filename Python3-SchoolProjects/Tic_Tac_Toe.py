#!/usr/bin/env python
#coding: utf-8
#In[ ]:
#a4.py
from random import randint
import random
import sys

total_cells = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_arr1=[]
no_element=" "

for i in total_cells:
    my_arr1.append(str(i))

print('This is Tic Tac Toe game!!!')
print("Consider the following schema for choosing your desired cell ")
first_Row = ("1", "2", "3")
print("|".join(first_Row))

print('_____')

second_Row = ("4", "5", "6")
print("|".join(second_Row))
print('_____')

third_Row = ("7", "8", "9")
print("|".join(third_Row))

print("\n")

def set_conditions():
    
    a=total_cells[0]
    b=total_cells[1]
    c=total_cells[2]
    d=total_cells[3]
    e=total_cells[4]
    f=total_cells[5]
    g=total_cells[6]
    h=total_cells[7]
    i=total_cells[8]

    placeholder1=list([a,b,c,d,e])
    placeholder2=list([f,g,h,i])
    x=any(placeholder1)
    o=any(placeholder2)
    return x,o


def Monte_Carlo_Tree_Search(table):

    my_list=[]

    for element in total_cells:

        def a_player(arr, cell):
            if cell == no_element:
                arr[element] = 'o'

        a = list(cell for cell in table)

        each_element = a[int(element)]

        a_player(a,each_element)

        winners=[]
        winner=element
        thirdRow = all([a[7] == 'o', a[8] == 'o', a[9] == 'o'])
        secondRow = all([a[4] == 'o', a[5] == 'o', a[6] == 'o'])
        firstRow = all([a[1] == 'o', a[2] == 'o', a[3] == 'o'])
        firstCol = all([a[7] == 'o', a[4] == 'o', a[1] == 'o'])
        secondCol = all([a[8] == 'o', a[5] == 'o', a[2] == 'o'])
        thirdCol = all([a[9] == 'o', a[6] == 'o', a[3] == 'o'])
        dia1 = all([a[7] == 'o', a[5] == 'o', a[3] == 'o'])
        dia2 = all([a[9] == 'o', a[5] == 'o', a[1] == 'o'])

        winners.append([thirdRow, secondRow, firstRow, firstCol, secondCol, thirdCol, dia1, dia2])

        for i in winners:
            if any(i):
                return winner

    direction=no_element
    for el in total_cells:

        def next_player(arr, cell):

            if cell == no_element:
                arr[el] = 'x'

        a2 = list(cell for cell in table)
        each_el=a2[int(el)]

        next_player(a2, each_el)

        winners = []
        winner=el
        thirdRow = all([a2[7] == 'x' , a2[8] == 'x' , a2[9] == 'x'])
        secondRow = all([a2[4] == 'x' , a2[5] == 'x' ,a2[6] == 'x'])
        firstRow = all([a2[1] == 'x' , a2[2] == 'x' ,a2[3] == 'x'])
        firstCol = all([a2[7] == 'x' , a2[4] == 'x' , a2[1] == 'x'])
        secondCol = all([a2[8] == 'x' , a2[5] == 'x' , a2[2] == 'x'])
        thirdCol = all([a2[9] == 'x' , a2[6] == 'x' , a2[3] == 'x'])
        dia1 =all([ a2[7] == 'x' , a2[5] == 'x' , a2[3] == 'x'])
        dia2 = all([a2[9] == 'x' , a2[5] == 'x' , a2[1] == 'x'])
        winners.append([thirdRow, secondRow, firstRow, firstCol, secondCol, thirdCol, dia1, dia2])

        def random_playOut():

            direction = randint(1, 9)# random playout
            return direction

        for i in winners:
            if any(i):
                return winner

        direction=random_playOut()

    return direction # program is base on random playouts

x=set_conditions()
o=set_conditions()

def human_and_computer(human):
    if human=='x':
        return not x > o
    else:
        return x > o

while human_and_computer('x'):

    def computer_and_human(computer):
        if computer == 'o':
            return not x > o
        else:
            return x > o

    def define_myElements():

        x = ''
        human = 'x'
        computer = 'o'
        return x, human, computer

    #empty table can be larger than actual table for playouts
    my_table = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def filling_the_cells(direction,arr):

        my_array = list(k for k in arr)
        one_element_in_cell= direction in my_array
        d = not one_element_in_cell
        return d

    def fill_each_cell(direction):

        con = filling_the_cells(direction,my_arr1)
        return con

    def two_rivals(firstPlayer, secondPlayer):

        f=firstPlayer
        s=secondPlayer
        total=(f,s)
        myRivals = list(rival for rival in total)
        return myRivals

    def cellElements():

        x, human, computer = define_myElements()

        competition=two_rivals(human,computer) # human is playing with computer
        while (x!='x'):
            x='x'
            return competition

    user = input("Do want to start playing?(yes/no):").lower()

    if user=='no':
        print('ok.have a nice day!')

    while computer_and_human('o'):

        my_condition1 = x > o
        my_condition2 = not my_condition1

        if user== 'yes':

            direction = no_element
            print("Base on above schema you need to enter a number(from 1 to 9) to choose your desired cell!!")

            def showResults():
                firstRow = (my_table[1], my_table[2], my_table[3])
                print("|".join(firstRow))
                print('_____')

                secondRow = (my_table[4], my_table[5], my_table[6])
                print("|".join(secondRow))
                print('_____')

                thirdRow = (my_table[7], my_table[8], my_table[9])
                print("|".join(thirdRow))

            def show_on_screen():

                showResults()

            show_on_screen()

            while fill_each_cell(direction):

                direction = input('Enter a number from 1 to 9 to choose your desired cell: ')

            humanTurn, computerTurn = cellElements()

            def MCTS(computer_win):
                computer_win = Monte_Carlo_Tree_Search(my_table)
                return computer_win

            winners=[]
            my_table[int(direction)] = humanTurn
            thirdRow = all([my_table[7] == my_table[int(direction)], my_table[8] == my_table[int(direction)],my_table[9] == my_table[int(direction)]])
            secondRow = all([my_table[4] == my_table[int(direction)], my_table[5] == my_table[int(direction)], my_table[6] == my_table[int(direction)]])
            firstRow = all([my_table[1] == my_table[int(direction)], my_table[2] == my_table[int(direction)],my_table[3] == my_table[int(direction)]])
            firstCol = all([my_table[7] == my_table[int(direction)], my_table[4] == my_table[int(direction)], my_table[1] == my_table[int(direction)]])
            secondCol = all([my_table[8] == my_table[int(direction)], my_table[5] == my_table[int(direction)], my_table[2] == my_table[int(direction)]])
            thirdCol = all([my_table[9] == my_table[int(direction)], my_table[6] == my_table[int(direction)],my_table[3] == my_table[int(direction)]])
            dia1 = all([my_table[7] == my_table[int(direction)], my_table[5] == my_table[int(direction)],my_table[3] == my_table[int(direction)]])
            dia2 = all([my_table[9] == my_table[int(direction)], my_table[5] == my_table[int(direction)],my_table[1] == my_table[int(direction)]])

            winners.append([thirdRow, secondRow, firstRow, firstCol, secondCol, thirdCol, dia1, dia2])

            def winTheGame():
                for i in winners:
                    return i

            def draw_is_reached():

                firstRow = (my_table[1], my_table[2], my_table[3])
                print("|".join(firstRow))
                print('_____')

                secondRow = (my_table[4], my_table[5], my_table[6])
                print("|".join(secondRow))
                print('_____')

                thirdRow = (my_table[7], my_table[8], my_table[9])
                print("|".join(thirdRow))
                print('A draw is reached!')

            def computerW():

                firstRow = (my_table[1], my_table[2], my_table[3])
                print("|".join(firstRow))
                print('_____')

                secondRow = (my_table[4], my_table[5], my_table[6])
                print("|".join(secondRow))
                print('_____')

                thirdRow = (my_table[7], my_table[8], my_table[9])
                print("|".join(thirdRow))
                print('The computer won...you lost!')

            def humanW():

                firstRow = (my_table[1], my_table[2], my_table[3])
                print("|".join(firstRow))
                print('_____')

                secondRow = (my_table[4], my_table[5], my_table[6])
                print("|".join(secondRow))
                print('_____')

                thirdRow = (my_table[7], my_table[8], my_table[9])
                print("|".join(thirdRow))
                print('You won! the computer lost')

            def empt():

                def notEmpty(table):

                    for cell in total_cells:
                        each_cell = table[int(cell)]
                        if each_cell==no_element:
                            return my_condition1

                    return my_condition2

                return not notEmpty(my_table)

            w=winTheGame()

            if not any(w):

                if empt():

                    direction=MCTS(direction)
                    winners=[]
                    my_table[int(direction)] = computerTurn
                    thirdRow = all([my_table[7] == my_table[int(direction)] , my_table[8] == my_table[int(direction)] , my_table[9] == my_table[int(direction)]])
                    secondRow =all([ my_table[4] == my_table[int(direction)] ,my_table[5] == my_table[int(direction)] , my_table[6] == my_table[int(direction)]])
                    firstRow = all([my_table[1] == my_table[int(direction)] , my_table[2] == my_table[int(direction)] , my_table[3] == my_table[int(direction)]])
                    firstCol = all([my_table[7] == my_table[int(direction)] , my_table[4] == my_table[int(direction)] , my_table[1] == my_table[int(direction)]])
                    secondCol = all([my_table[8] == my_table[int(direction)] , my_table[5] == my_table[int(direction)] , my_table[2] == my_table[int(direction)]])
                    thirdCol =all([ my_table[9] == my_table[int(direction)] , my_table[6] == my_table[int(direction)] , my_table[3] == my_table[int(direction)]])
                    dia1 = all([my_table[7] == my_table[int(direction)] , my_table[5] == my_table[int(direction)] , my_table[3] == my_table[int(direction)]])
                    dia2 = all([my_table[9] == my_table[int(direction)] , my_table[5] == my_table[int(direction)] , my_table[1] == my_table[int(direction)]])
                    winners.append([thirdRow, secondRow, firstRow, firstCol, secondCol, thirdCol, dia1, dia2])

                    def win_the_game():
                        for i in winners:
                            return i

                    i=win_the_game()

                    if any(i):
                        computerW()
                        break

                    else:
                        #when all the cells are empty we ask the human to see if he likes to play again
                        if empt():
                            user = 'yes'
                        else:
                            draw_is_reached()
                            break

                else:
                    draw_is_reached()
                    break

            else:
                humanW()
                break
