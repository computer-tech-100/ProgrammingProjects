#include<iostream>
using namespace std;
#include<string>
#include<cmath>
#include<vector>
#include<cmath>
#include<algorithm>
#include <regex>
#include<bitset>

//-----------------------------------------------------------------------Strong Password-----------------------------------------------------------
//This program determines the minimum number of characters needed to make a strong password.
//A password is considered strong if it satisfies the following criteria:
//Its length is at least 6.
//It contains at least one digit.
//It contains at least one lowercase English character.
//It contains at least one uppercase English character.
//It contains at least one special character: !@#$%^&*()-+

int main(){
    
    //if the email is valid, then all of these conditions should become true
    bool upperCase=false;
    bool lowerCase=false;
    bool special=false;
    bool length=false;
    bool digit=false;
    
    char uppercase_letters[26] =
    {
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
        'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R',
        'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};
    
    
    char lowerCase_letters[26] =
    {
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
        'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r',
        's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
    
    char specials[9]={'!','@','#','$','%','&','*','-','+'};
    
    cout<<"Enter your password:";
    
    string userInput;
    getline(cin, userInput);
    
    //check if user's input contains all necessary characters
    for(int i=0;i<26;i++){

        if (userInput.find(uppercase_letters[i]) != string::npos){
            upperCase=true;
            break;
        }
        else{
            upperCase=false;
        } 
    }
    for(int i=0;i<26;i++){
        
        if( userInput.find(lowerCase_letters[i]) != string::npos){
            lowerCase=true;
            break;
        }
        else{
            lowerCase=false; 
        } 
    }
    for(int i=0;i<9;i++){
        
        if( userInput.find(specials[i]) != string::npos){
            special=true;
            break;  
        }
        else{
            special=false;  
        } 
    }
    
    for(int i=0;i<userInput.length();i++){
        
        if( isdigit(userInput[i])){
            digit=true;
            break;
        }
        else{
            digit=false;  
        }
    }
    if( userInput.length()>=6){
        length=true;     
    }
    else{
        length=false;   
    }
    int count=0;
    
    if(upperCase==true && lowerCase==true && special==true && digit==true && length==true){
        cout<<"Your password is strong"<<endl;  
    }
    else{
        cout<<"Your password is not strong"<<endl;
        if(upperCase==false){
            count++;
        }
        if(lowerCase==false){
            count++;
        }
        if(special==false){
            count++;
        }
        if(digit==false){
            count++;
        }
        if(length==false){
            count++;
        }
        cout<<"You need to consider "<<count<<" more requirements to get a valid password"<<endl;
    }
}
