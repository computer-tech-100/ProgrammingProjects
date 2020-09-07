//assignment 5
//connect 4
//pure Monte Carlo Tree Search algorithm
#include <iostream>
using namespace std;
#include <string.h>
#include<vector>
#include <time.h>
#include <cctype>

clock_t start_point= clock();

// declare functions
int my_func();
int my_possible_choices(int);

int my_func(){
    int a=6;
    int b=7;
    int e=1;
    int Arr[2]={a,b};
    for (int i=0;i<2;i++){
        e=e*Arr[i];
    }
    return e;
}

typedef int myConnect4;
typedef char tableInput;

myConnect4 my_possible_choices(int num){
    
    int arr[9]={-1,0,1,2,3,4,5,6,7};
    if (num==1){
        return arr[0]; 
    }
    else if(num==2){
        return arr[1];
    }
    else if(num==3){
        return arr[7];   
    }
    else if (num==4){
        return arr[6];
    }
    else if (num==5){
        return arr[8];
    }
    else if(num==6){
        return arr[3];
    }
    else if(num==0){
        return arr[4];
    }
    else{
        return arr[2];
    }
}

//build table
struct table {
   myConnect4 cell=my_func();
   tableInput cells[42];  
};

typedef table myTable;
//function declarations
myConnect4 choose_cell(table , myConnect4 ,myConnect4);
myConnect4 random(myConnect4);
myConnect4 my_random_playOut(table ,myConnect4 );
myConnect4 my_move(table,myConnect4 ,myConnect4);
myConnect4 MCTS(table);
myConnect4 computer_and_human_competition(table,myConnect4);
void my_table(table);
myConnect4 computer_turn(table,myConnect4);
myConnect4 computer_choice(table);

// determine which cell to choose
myConnect4 choose_cell(myTable *myTablePointer, myConnect4 move, myConnect4 element) {
    
    myConnect4 my_cell=my_possible_choices(7);
    myConnect4 finish_point;
    finish_point=finish_point+my_possible_choices(7);
    myConnect4 my_move_Array[]={move,element,my_cell,finish_point};
    
    for (finish_point = my_possible_choices(2); finish_point < my_possible_choices(3); finish_point=finish_point+my_possible_choices(7)) {

        int my_first_step=0;
        int final_movement=0;
        int a_cell=6;
        int before_cell=5;
        int after_cell=7;
        int firstCondition=my_move_Array[0] < my_first_step;
        int secondCondition=finish_point > before_cell;
        int thirdCondition=finish_point < my_first_step;
        int fourthCondition=my_move_Array[0] > a_cell;
        int move_to_end=1;
        int first_value=0;
        int second_value=1;
        int value=0;
        int my_arr[2]={finish_point,after_cell};
        
        for (int i=0; i<2;i++){
            
            move_to_end=move_to_end * my_arr[i];
        }
        
        int stage1=1;
        int myArr[2]={before_cell,after_cell};
        
        for (int i=0; i<2;i++){
            
            stage1=stage1 * myArr[i];
        }
        
        int ignore_last_stage=my_move_Array[0]-move_to_end;
        int my_array[2]={stage1,ignore_last_stage};
        
        for (int i=0; i<2;i++){
            
            final_movement=final_movement + my_array[i];
        }
        
        int my_ar[2]={first_value,second_value};
        
        for (int i=0; i<2;i++){
            
            value = value - my_ar[i];
        }
        
        if (firstCondition){
            
            return value;
        }
        
        else if (secondCondition){
            
            return value;
        }
        
        else if (thirdCondition){
            
            return value;
        }
        
        else if (fourthCondition){
            
            return value;
        }
        
        if (myTablePointer->cells[final_movement]== my_possible_choices(2)) {
            
            int final_movement=my_possible_choices(2);
            int before_cell=my_possible_choices(4);
            int after_cell=my_possible_choices(5);
            
            int stage1=1;
            int myArr[2]={before_cell,after_cell};
            
            for (int i=0; i<2;i++){
                
                stage1=stage1 * myArr[i];
            }
            
            int move_to_end=1;
            int my_arr[2]={finish_point,after_cell};
            
            for (int i=0; i<2;i++){
                
                move_to_end=move_to_end * my_arr[i];
            }
           
            int ignore_last_stage=move-move_to_end;
            int my_array[2]={stage1,ignore_last_stage};
            
            for (int i=0; i<2;i++){
                
                final_movement=final_movement + my_array[i]; 
            }

            myTablePointer->cells[final_movement] = my_move_Array[1];
            
            break;
        }
    }
    return my_cell ;
}

//random choice
myConnect4 random(myConnect4 num){
    return rand()%num;
}

//random play out
myConnect4 my_random_playOut(table *myTablePointer,myConnect4 computerSteps){
    myConnect4 num_of_column_rand= random(7);
    return choose_cell(myTablePointer,num_of_column_rand,computerSteps);
}

//function for every movement
myConnect4 my_move(myTable *myTablePointer,myConnect4 move,myConnect4 finish_point){
    
    int my_first_step=0;
    int final_movement=0;
    int a_cell=6;
    int before_cell=5;
    int after_cell=7;
    int firstCondition=move < my_first_step;
    int secondCondition=finish_point > before_cell;
    int thirdCondition=finish_point < my_first_step;
    int fourthCondition=move > a_cell;
    int move_to_end=1;
    int first_value=0;
    int second_value=1;
    int value=0;
    int my_arr[2]={finish_point,after_cell};
    
    for (int i=0; i<2;i++){
        
        move_to_end=move_to_end * my_arr[i];
    }
    
    int stage1=1;
    int myArr[2]={before_cell,after_cell};
    
    for (int i=0; i<2;i++){
        
        stage1=stage1 * myArr[i];
    }
    
    int ignore_last_stage=move-move_to_end;
    int my_array[2]={stage1,ignore_last_stage};
    
    for (int i=0; i<2;i++){
        
        final_movement=final_movement + my_array[i];
    }
    
    int my_movement=myTablePointer->cells[final_movement];
   
    int my_ar[2]={first_value,second_value};
    
    for (int i=0; i<2;i++){
        
        value = value - my_ar[i];
    }
   
    if (firstCondition){
        return value;
    }
    
    else if (secondCondition){
        
        return value;
    }
    
    else if (thirdCondition){
        return value;
    }
    
    else if (fourthCondition){
        return value;
    }
    
    return my_movement;
}

//algorithm
myConnect4 MCTS(myTable *myTablePointer) {
    
    myConnect4 space= my_possible_choices(2);

    for (int finish_point= my_possible_choices(4); finish_point >= my_possible_choices(2); finish_point=finish_point-my_possible_choices(7)) {
        for (int move= my_possible_choices(2); move < my_possible_choices(5); move=move+my_possible_choices(7)) {

            myConnect4 myArray[7]={my_possible_choices(1),my_possible_choices(2),my_possible_choices(7),my_possible_choices(6),my_possible_choices(0),my_possible_choices(4),my_possible_choices(3)};
            myConnect4 first_choice=myArray[my_possible_choices(6)];
            myConnect4  second_choice=myArray[my_possible_choices(7)];
            myConnect4 third_choice=myArray[my_possible_choices(2)];
            myConnect4 fourth_choice=myArray[my_possible_choices(2)];
            myConnect4 fifth_choice=myArray[my_possible_choices(2)];
            
            struct filling_the_table{
                
                myConnect4 x;
                myConnect4 y;
                myConnect4 diagoanl1;
                myConnect4 diagonal2;
                myConnect4 diagoanl3;
                myConnect4 vertical;
                myConnect4 horizontal;
                
            } my_points[] = {
                {first_choice,second_choice},
                {second_choice,first_choice},
                {first_choice,first_choice},
                {third_choice,first_choice},
                {third_choice,fourth_choice},
                {fourth_choice,fifth_choice},
                {first_choice,fifth_choice}

            };

            int my_first_step=0;
            int final_movement=0;
            int a_cell=6;
            int my_movement_limit=my_possible_choices(0)+my_possible_choices(7);
            int next_move=1;
            int my_movement= move;
            int my_goal = finish_point;
            int before_cell=5;
            int last_cell=my_possible_choices(2);
            int after_cell=7;
            int firstCondition=move < my_first_step;
            int secondCondition=finish_point > before_cell;
            int thirdCondition=finish_point < my_first_step;
            int fourthCondition=move > a_cell;
            int move_to_end=1;
            int first_value=0;
            int second_value=1;
            int value=0;
            int cell;
 
            int my_arr[2]={finish_point,after_cell};
            
            for (int i=0; i<2;i++){
                
                move_to_end=move_to_end * my_arr[i];
            }
            
            int stage1=1;
            int myArr[2]={before_cell,after_cell};
            
            for (int i=0; i<2;i++){
                
                stage1=stage1 * myArr[i];
            }
            
            int ignore_last_stage=move-move_to_end;
            int my_array[2]={stage1,ignore_last_stage};
            
            for (int i=0; i<2;i++){
                
                final_movement=final_movement + my_array[i];
            }
            
            switch (myTablePointer->cells[final_movement]) {
                case 0:
                    space=space+next_move;
                    continue;
                    
                default:
                    break;
            }
            
            int my_ar[2]={first_value,second_value};
            
            for (int i=0; i<2;i++){
                
                value = value - my_ar[i];
            }
            
            if (firstCondition){
                return value;
            }
            
            else if (secondCondition){
                
                return value;
            }
            
            else if (thirdCondition){
                return value;
            }
            
            else if (fourthCondition){
                return value;
            }

            for (cell= my_possible_choices(2); cell < my_movement_limit; cell=cell+my_possible_choices(7)) {
                myConnect4 xValue= my_points[cell].x;
                myConnect4 total=last_cell>= my_movement_limit;
                myConnect4 yValue=my_points[cell].y;
                
                while(my_move(myTablePointer,my_movement-xValue,my_goal-yValue) == myTablePointer->cells[final_movement])   
                {
                    int pointValue=0;
                    int my_ar[2]={xValue,my_movement};
                    
                    for (int i=0; i<2;i++){
                        
                        pointValue= pointValue - my_ar[i];
                    }

                    myConnect4 pointValue2=0;
                    my_goal = my_goal-yValue;
                    my_movement= my_movement-xValue;
                    myConnect4 my_ar2[2]={yValue,my_goal};

                    for (int k=0; k<2;k++){
                        
                        pointValue2 = pointValue2 + my_ar2[k];
                    }
                    
                    int add_up=0;
                    int pointValue3=0;
                    int my_ar3[3]={yValue,my_goal,xValue};
                    
                    for (int v=0; v<3;v++){
                        
                        pointValue3 = pointValue3 + my_ar3[v];
                    }
                    
                    int bestMove;
                    bestMove=(add_up)+(pointValue+pointValue2+pointValue3);

                }

                while(my_move(myTablePointer,my_movement,my_goal) == myTablePointer->cells[final_movement])
                {
                    int val1=0;
                    
                    int my_array[2]={my_movement,xValue};
                    
                    for (int i=0; i<2;i++){
                        
                        val1=val1 + my_array[i];
                    }
                    
                    last_cell=last_cell+my_possible_choices(7);
                    my_movement=val1;
                    
                    int val2=0;
                    
                    int my_array2[2]={my_goal,yValue};
                    
                    for (int i=0; i<2;i++){
                        
                        val2=val2 + my_array2[i];
                    }
                
                    my_goal=val2;

                }

                if (total){
                    
                    return myTablePointer->cells[final_movement];
                }
            }
        }
    }

    if (!space){
        return my_possible_choices(0);
    }
    else{
        return my_possible_choices(2);
    }

}

//when human and computer are playing against each other
myConnect4 computer_and_human_competition(myTable *myTablePointer, myConnect4 next_step) 
{
    while(true) {
        
        if (my_random_playOut(myTablePointer,next_step)) {
       
            switch(next_step){
                case 1:{
                    next_step=my_possible_choices(6);
                    break;
                }
                default:
                    next_step=my_possible_choices(7);
                    break;        
            }
        }
       
        if (MCTS(myTablePointer) != my_possible_choices(2)){
    
            int space= my_possible_choices(2);
            int move;
            int finish_point;
            
            for (finish_point= my_possible_choices(4); finish_point >= my_possible_choices(2); finish_point=finish_point-my_possible_choices(7)) {
                for ( move= my_possible_choices(2); move < my_possible_choices(5); move=move+my_possible_choices(7)) {

                    myConnect4 myArray[7]={my_possible_choices(1),my_possible_choices(2),my_possible_choices(7),my_possible_choices(6),my_possible_choices(0),my_possible_choices(4),my_possible_choices(3)};
                    myConnect4 first_choice=myArray[my_possible_choices(6)];
                    myConnect4  second_choice=myArray[my_possible_choices(7)];
                    myConnect4 third_choice=myArray[my_possible_choices(2)];
                    myConnect4 fourth_choice=myArray[my_possible_choices(2)];
                    myConnect4 fifth_choice=myArray[my_possible_choices(2)];
                    
                    struct filling_the_table{
                        
                        myConnect4 x;
                        myConnect4 y;
                        myConnect4 diagoanl1;
                        myConnect4 diagonal2;
                        myConnect4 diagoanl3;
                        myConnect4 vertical;
                        myConnect4 horizontal;

                    } my_points[] = {
                        {first_choice,second_choice},
                        {second_choice,first_choice},
                        {first_choice,first_choice},
                        {third_choice,first_choice},
                        {third_choice,fourth_choice},
                        {fourth_choice,fifth_choice},
                        {first_choice,fifth_choice}
                    };

                    int my_first_step=0;
                    int final_movement=0;
                    int a_cell=6;
                    int my_movement_limit=4;
                    int next_move=1;
                    int before_cell=5;
                    int after_cell=7;
                    int firstCondition=move < my_first_step;
                    int secondCondition=finish_point > before_cell;
                    int thirdCondition=finish_point < my_first_step;
                    int fourthCondition=move > a_cell;
                    int move_to_end=1;
                    int first_value=0;
                    int second_value=1;
                    int value=0;

                    int my_arr[2]={finish_point,after_cell};
                    
                    for (int i=0; i<2;i++){
                        
                        move_to_end=move_to_end * my_arr[i];
                    }
                    
                    int stage1=1;
                    int myArr[2]={before_cell,after_cell};
                    
                    for (int i=0; i<2;i++){
                        
                        stage1=stage1 * myArr[i];
                    }
                    
                    int ignore_last_stage=move-move_to_end;
                    int my_array[2]={stage1,ignore_last_stage};
                    
                    for (int i=0; i<2;i++){
                        
                        final_movement=final_movement + my_array[i];
                    }

                    switch (myTablePointer->cells[final_movement]) {
                        case 0:
                            space=space+next_move;
                            continue;
                            
                        default:
                            break;
                    }
                    
                    int my_ar[2]={first_value,second_value};
                    
                    for (int i=0; i<2;i++){
                        
                        value = value - my_ar[i];
                    }

                    if (firstCondition){
                        return value;
                    }
                    
                    else if (secondCondition){
                        
                        return value;
                    }
                    
                    else if (thirdCondition){
                        return value;
                    }
                    
                    else if (fourthCondition){
                        return value;
                    }

                    for (int cell= 0; cell < my_movement_limit; cell++) {
      
                        myConnect4 my_movement= move;
                        myConnect4 limit=0;
                        myConnect4 xVal=my_points[cell].x;
                        myConnect4 yVal=my_points[cell].y;
                        myConnect4 my_goal = finish_point;
                        
                        while(my_move(myTablePointer,my_movement- xVal,my_goal-yVal) == myTablePointer->cells[final_movement]) 
                        {
                            
                            int pointValue=0;
                            int my_ar[2]={xVal,my_movement};
                            
                            for (int i=0; i<2;i++){
                                
                                pointValue= pointValue - my_ar[i];
                            }
                            my_movement= my_movement-xVal;

                            int pointValue2=0;
                            int my_ar2[2]={yVal,my_goal};
                            
                            for (int k=0; k<2;k++){
                                
                                pointValue2 = pointValue2 + my_ar2[k];
                            }

                            int add_up=0;
                            my_goal = my_goal-yVal;
                            int pointValue3=0;
                            int my_ar3[3]={yVal,my_goal,xVal};
                            
                            for (int v=0; v<3;v++){
                                
                                pointValue3 = pointValue3 + my_ar3[v];
                            }
                            int bestMove;
                            bestMove=(add_up)-(pointValue+pointValue2+pointValue3);
                            bestMove=abs(bestMove);

                        }

                        while(my_move(myTablePointer,my_movement,my_goal) == myTablePointer->cells[final_movement]) {

                            int val1=0;
                            
                            int my_array[2]={my_movement,xVal};
                            
                            for (int i=0; i<2;i++){
                                
                                val1=val1 + my_array[i];
                            }
                            
                            limit=limit+my_possible_choices(7);
                            my_movement=val1;
                            
                            int val2=0;
                            
                            int my_array2[2]={my_goal,yVal};
                            
                            for (int i=0; i<2;i++){
                                
                                val2=val2 + my_array2[i];
                            }
                            my_goal=val2;

                        }
                        myConnect4 total=limit >= my_movement_limit;

                        
                        if (total){
                            
                            return myTablePointer->cells[final_movement];
                        }
                    }
                }
            }
            
            if (!space){
                return my_possible_choices(0);
            }
            else{
                return my_possible_choices(2);
            }   
        }
    }
}

void my_table(myTable *myTablePointer){
    
    table myTable;
    myTablePointer= &myTable;
    
}

myConnect4 computer_turn(table *myTablePointer, myConnect4 choice) {
  
    int win=choice;
    float final_value=my_possible_choices(2);
    int end=my_possible_choices(1);
    int cell;
    int start=my_possible_choices(7);
    int in_value=start;
    int result=end;
    int first_step=my_possible_choices(2);
    int numer_of_rows=7;
    
    for (first_step = my_possible_choices(2); first_step < numer_of_rows; first_step=first_step+my_possible_choices(7)) {
       
        int computer = my_possible_choices(2);
        int human = my_possible_choices(2);
        float very_first_move=my_possible_choices(7);
        int my_steps=my_possible_choices(2);
        float very_last_move=my_possible_choices(7);
        int any_move=my_possible_choices(7);
        float first_human_move=my_possible_choices(2);
        float last_human_move=my_possible_choices(2);
        float any_human_move;
        
        for (my_steps = my_possible_choices(2); my_steps < 900; my_steps=my_steps+my_possible_choices(7)) {

            table a;
            table *my_cell;
            my_cell= &a;
            myConnect4 lenn=sizeof(my_cell->cells);
            memcpy(my_cell->cells,myTablePointer->cells,lenn);

            for (int finish_point = my_possible_choices(2); finish_point < my_possible_choices(3); finish_point=finish_point+my_possible_choices(7)) {

                int my_first_step=0;
                int final_movement=0;
                int a_cell=6;
                int before_cell=5;
                int after_cell=7;
                int firstCondition=first_step < my_first_step;
                int secondCondition=finish_point > before_cell;
                int thirdCondition=finish_point < my_first_step;
                int fourthCondition=first_step> a_cell;
                int move_to_end=1;
                int first_value=0;
                int second_value=1;
                int value=0;
                int my_arr[2]={finish_point,after_cell};
                
                for (int i=0; i<2;i++){
                    
                    move_to_end=move_to_end * my_arr[i];
                }
                
                int stage1=1;
                int myArr[2]={before_cell,after_cell};
                
                for (int i=0; i<2;i++){
                    
                    stage1=stage1 * myArr[i];
                }
                
                int ignore_last_stage=first_step-move_to_end;
                int my_array[2]={stage1,ignore_last_stage};
                
                for (int i=0; i<2;i++){
                    
                    final_movement=final_movement + my_array[i];
                }
                
                int my_ar[2]={first_value,second_value};
                
                for (int i=0; i<2;i++){
                    
                    value = value - my_ar[i];
                }
       
                if (firstCondition){
                    return value;
                }
                
                else if (secondCondition){
                    
                    return value;
                }
                
                else if (thirdCondition){
                    return value;
                }
                
                else if (fourthCondition){
                    return value;
                }

                if (myTablePointer->cells[final_movement]== my_possible_choices(2)) {
           
                    int final_movement=my_possible_choices(2);
                    int before_cell=my_possible_choices(4);
                    int after_cell=my_possible_choices(5);
  
                    int stage1=1;
                    int myArr[2]={before_cell,after_cell};
                    
                    for (int i=0; i<2;i++){
                        
                        stage1=stage1 * myArr[i];
                    }

                    int move_to_end=1;
                    int my_arr[2]={finish_point,after_cell};
                    
                    for (int i=0; i<2;i++){
                        
                        move_to_end=move_to_end * my_arr[i];
                    }
 
                    int ignore_last_stage=first_step-move_to_end;
                    int my_array[2]={stage1,ignore_last_stage};
                    
                    for (int i=0; i<2;i++){
                        
                        final_movement=final_movement + my_array[i];
                    }
                    
                    my_cell->cells[final_movement] = choice;
                    
                    break;
                }
                
            }
            
            myConnect4 human_H=human+in_value;
            myConnect4 turn= computer_and_human_competition(&a,cell);
            myConnect4 computer_c=computer+in_value;
            myConnect4 human_turn=human+my_possible_choices(7);
            myConnect4 computer_turn=computer+my_possible_choices(7);
            myConnect4 any_choice1=my_possible_choices(2);
            myConnect4 human_choice=my_possible_choices(7);
            myConnect4 any_choice2=my_possible_choices(2);
            myConnect4 computer_choice=my_possible_choices(7);
            
            if ( turn== my_possible_choices(6)) {
                
                if (turn!=win){
                    
                    any_choice1=my_possible_choices(6)+my_possible_choices(5);
                    human=human_H;
                    human_choice=any_choice1+my_possible_choices(7);
                }
                
                else{

                    any_choice2=my_possible_choices(6)+my_possible_choices(5);
                    computer=computer_c;
                    computer_choice=any_choice2+my_possible_choices(7);   
                }
            }
            
            if (turn==my_possible_choices(7)){
                
                if (turn!=win){
                    human=human_turn;   
                }
                else{
                    computer=computer_turn;
                    
                }     
            }
        }
             
         myConnect4 value=human+start;
         float my_value;
         my_value=static_cast<float>(computer);
         myConnect4 the_human;
         float value_of_the_element= my_value/value;
         myConnect4 the_result=result == end;
         float last_value= value_of_the_element > final_value;
         myConnect4 the_computer;
  
        if ( last_value ) {
         
            myConnect4 computerTurn= very_last_move;
            result = first_step;
            myConnect4 the_last=computerTurn+my_possible_choices(7);
            the_last=any_move;
            final_value= value_of_the_element;
            float distance=0;
            distance=(any_move+very_last_move)/very_first_move;
            distance=distance/42;
            the_computer=the_computer+my_possible_choices(7);

        }
        
        else if (the_result) {

            myConnect4 humanFirst= very_last_move;
            result = first_step;
            myConnect4 the_last=humanFirst+my_possible_choices(7);
            the_last=any_human_move;
            final_value= value_of_the_element;
            float human_distance=the_last;
            human_distance=(any_human_move+last_human_move)/first_human_move;
            human_distance=human_distance/42;
            the_human=the_human+my_possible_choices(7);
        }
    }
    return result;
}

myConnect4 computer_choice(myTable *myTablePointer){

    int optimal_choice = computer_turn(myTablePointer,my_possible_choices(7));
    
    return choose_cell(myTablePointer,optimal_choice,my_possible_choices(7));
    
}

int main() {
    
    cout<<"This is Connect4 game base on pure Monte Carlo Tree Search algorithm!"<<endl;
    cout<<"Please consider the following guide for entering your desired number:"<<endl;
    cout<<"________________________"<<endl;
    cout<<"| Enter 0 for column A |"<<endl;
    cout<<"| Enter 1 for column B |"<<endl;
    cout<<"| Enter 2 for column C |"<<endl;
    cout<<"| Enter 3 for column D |"<<endl;
    cout<<"| Enter 4 for column E |"<<endl;
    cout<<"| Enter 5 for column F |"<<endl;
    cout<<"| Enter 6 for column G |"<<endl;
    cout<<"________________________"<<endl;
    cout<<" You are H (i.e Human) and computer is C"<<endl;
    
   table myTable;
   table *my_cell;
   my_cell=&myTable;
   myConnect4 length=sizeof(my_cell->cells);
   memset(my_cell->cells,NULL,length);

    while(my_possible_choices(2)<my_possible_choices(7)) {
        myConnect4 initial_value=my_possible_choices(1);
        myConnect4 fixed_val=initial_value;
        myConnect4 finish_point;
        myConnect4 move;

       for (finish_point = my_possible_choices(4); finish_point >= my_possible_choices(2); finish_point=finish_point-my_possible_choices(7)) {
           for (move = my_possible_choices(2); move < my_possible_choices(5); move=move+my_possible_choices(7)) {
    
                int final_movement=my_possible_choices(2);
                int before_cell=my_possible_choices(4);
                int after_cell=my_possible_choices(5);
                int move_to_end=1;
           
                int my_arr[2]={finish_point,after_cell};
                
                for (int i=0; i<2;i++){
                    
                    move_to_end=move_to_end * my_arr[i];
                }
                
                myConnect4 stage1=1;
                const tableInput *input = " CH"; // computer C vs. human H
                int myArr[2]={before_cell,after_cell};
                
                for (int i=0; i<2;i++){
                    
                    stage1=stage1 * myArr[i];
                }
                
                int ignore_last_stage=move-move_to_end;
                int my_array[2]={stage1,ignore_last_stage};
                
                for (int i=0; i<2;i++){
                    
                    final_movement=final_movement + my_array[i];
                }
                
                printf("  %c  ",input[my_cell->cells[final_movement]]);   
            }
            cout<<endl;
            cout<<endl;
        }
        
        myConnect4 forward;
        
        string add[7]={"A","B","C","D","E","F","G"}; // 7 columns
    
        cout<<"---------------------------------"<<endl;
 
        for (forward =my_possible_choices(2); forward< my_possible_choices(5); forward=forward+my_possible_choices(7)){

            cout<<"  "<< add[forward]<<"  ";         
 }
        cout<<endl;
        cout<<endl;
 
        if (MCTS(my_cell) != my_possible_choices(2)) {
            cout<<"The Computer Won!"<<endl;
            
            float my_time=static_cast<float>(clock() - start_point);
            
            cout<<"Elapsed time is : "<< my_time/CLOCKS_PER_SEC<<"s"<<endl;
            
            cout<< "would you like to play again? (yes/no) :"<<endl;
            string answer;
            
            cin>>answer; // get user's input
            
            for (int k=my_possible_choices(2);k<answer.length();k=k+my_possible_choices(7)){
                answer[k]=tolower(answer[k]);
            }
         
            if (answer=="yes"){
                main();//start the game again
            }
            else if (answer=="no"){
                cout<<"Ok have a nice day!"<<endl;
                break;
            }

        }

        while(initial_value == fixed_val) {

            cout<<"It is your turn select a number and hit enter: ";
            myConnect4 first;
            tableInput get_each_move[]={};// declare an empty array
            myConnect4 my_size=42;

            for (int i=0;i<=my_size;i++){
                get_each_move[i]=i;
                
            }

            fgets(get_each_move,42,stdin);
            sscanf(get_each_move, "%d", &first);
            initial_value = first;
        }

        choose_cell(my_cell,initial_value,my_possible_choices(6));//call the function
        
        computer_choice(my_cell); //call the function
    }
    
    return 0;  
}
