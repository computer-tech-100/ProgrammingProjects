#include<iostream>
using namespace std;
#include<string>
#include<cmath>
#include<vector>
#include<cmath>
#include<algorithm>
#include <regex>
#include<bitset>

//--------------------------------------------------------------------------Array Formatting--------------------------------------------------------------
//This program formats the array such that the first letter of each word becomes capitalized
//If all of the letters are capitalized then you just lowercase all letters except the first letter for example:
//JERRY becomes Jerry
//Don't change the order of the original array.
//function that takes an array of names and returns an array with the first letter capitalized
void format(string arr[],int size);

int main(){
    
    string names1[]={"jerry", "john", "lucas"};
    
    string names2[]={"samuel", "LIAM", "letitia", "meridith"};
    
    string names3[]={"Slyvia", "William", "Tom", "Calista"};
    
    format(names1,3); //["Jerry", "John", "Lucas"]
    
    format(names2,4);//["Samuel", "Liam", "Letitia", "Meridith"]
    
    format(names3,4);//["Slyvia", "William", "Tom", "Calista"]
     
}

void format(string arr[],int size){
    
    //convert everything to lowercase
    for(int i=0;i<size;i++){
        
        for_each(arr[i].begin(), arr[i].end(), [](char & letter){
            letter = ::tolower(letter);
        }
                 );
        
    }
    
    //capitalize the first letter of each word
    for(int i=0;i<size;i++){
        if(islower(arr[i][0])){
            arr[i][0]=toupper(arr[i][0]);
        }
        
        cout<<arr[i]<<endl;
    }
       
}
