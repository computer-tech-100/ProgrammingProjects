#include<iostream>
using namespace std;
#include<string>
#include<cmath>
#include<vector>
#include<cmath>
#include<algorithm>
#include <regex>

//-------------------------------------------------------------------------Digits Battle------------------------------------------------------------------
//This program returns the digits who won the battle
//Rules of the game:
//We Start from left side of an integer, adjacent digits pair up in "battle" and the larger digit wins.
//If two digits are the same, they both lose.
//Alone digit automatically wins.
//example: 49 --> 9 wins so the program retuns 9
//5867 --> 8 defeats 5 and 7 defeats 6 --> hence the program returns 8 7
//44--> both loses
//3--> this is alone digit that is always a winner
/// NOTES:
//// In odd length numbers alone number at the end is always a winner for example--> 42719--> 4 defeats 2 , 7 defeats 1 , 9 remains alone hence ---> the program returns 4 7 9
/// 222 -->pair up first two : 22 hence none of them wins -->2 will remain at the end hence 2 wins --> the program returns 2

int digits_battle_game(int number);

int main(){
    
    digits_battle_game(4981);
    
    digits_battle_game(18);
    
    digits_battle_game(5867);
    
    digits_battle_game(44);
    
    digits_battle_game(3);
    
    digits_battle_game(2);
    
    digits_battle_game(42719);
    
    digits_battle_game(222);
    
    digits_battle_game(6143802);
    
}

int digits_battle_game(int number){
    
    int n=number;// store number in another variable
    
    int length_of_number = 0;//this gives number of digits in number
    
    vector <int>  v1 ; //store digits of number into a vector
    
    vector <pair<int,int> > v2 ;//store the pairs
    
    vector <int> winners;// store winners of the game
    
    //get length
    do {
        ++length_of_number;
        n /=10;
    } while (n);
    
    if(length_of_number>=10){
        cout<<"please enter an int with length shorter than 10"<<endl;
    }
    
    if(length_of_number==1){
        cout<<number<< " is alone digit hence it is a winner"<<endl;  
    }
    
    //even length
    if(length_of_number%2==0){
        
        // store all digits of number into a vector  --> pair
        while(number)
        {
            int digit= (number%10);
            number /= 10;
            v1.push_back(digit);
        }
        reverse( v1.begin(), v1.end() );
        
        // pair up the digits of number
        for(int i=0;i<v1.size();i++){
            v2.push_back(make_pair(v1[i],v1[i+1] ));
            v1.erase(std::find(v1.begin(),v1.end(),v1[i]));  
        }
        
        for(int i=0;i<v2.size();i++){
            
            if(v2[i].second>v2[i].first ){
                winners.push_back(v2[i].second);
            }
            
            if(v2[i].first>v2[i].second){
                winners.push_back(v2[i].first);
            }
            
            if(v2[i].first==v2[i].second){
                cout<<"losers of the game are:"<< v2[i].first<<" "<<v2[i].second<<endl;
                break;
                
            }     
        }
        
        cout<<"the winners are: "<<endl;
        for(int i=0;i<winners.size();i++){
            cout<<winners[i]<<endl;
        }  
    }
    
    //odd length
    if(length_of_number>1 && length_of_number%2!=0){
        
        int last_digit= number % 10;
        
        while(number)
        {
            int digit= (number%10);
            number /= 10;
            v1.push_back(digit);
        }
        reverse( v1.begin(), v1.end() );
        v1.pop_back();// remove the last digit because it is always a winner then later we add it to winner vector
        
        // pair up the digits of number
        for(int i=0;i<v1.size();i++){
            v2.push_back(make_pair(v1[i],v1[i+1] ));
            v1.erase(std::find(v1.begin(),v1.end(),v1[i]));  
        }
        
        for(int i=0;i<v2.size();i++){
            
            
            if(v2[i].second>v2[i].first ){
                winners.push_back(v2[i].second);
            }
            
            if(v2[i].first>v2[i].second){
                winners.push_back(v2[i].first);
            }
            
            if(v2[i].first==v2[i].second){
                cout<<"losers of the game are:"<< v2[i].first<<" "<<v2[i].second<<endl;
                break;
                
            } 
        }
        winners.push_back(last_digit);// now add the last digit to the vector of winners
        cout<<"the winners are: "<<endl;
        for(int i=0;i<winners.size();i++){
            cout<<winners[i]<<endl;
        }  
    }
    
    return 0;
}
