#include<iostream>
using namespace std;
#include<string>
#include<cmath>
#include<vector>
#include<cmath>
#include<algorithm>
#include <regex>

//-------------------------------------------------------------------------Stretched String---------------------------------------------------------------
//This programs determines if a string is Stretched or not.(input string should have unique characters)
//It returns 1 (i.e true) if the first string is the stretched version of second string. Otherwise it returns 0 (i.e false)
//A stretched version is to repeat each character in a string the same number of times.
//for example: ccoommppuutteerr is stretched version of computer but cccccompputterrrr is not a stretched version because each charactor is not repeated same number of times.

bool isStretched(string first,string second);

int main(){

    cout<<isStretched("ccccoommmpuutteer","computer")<<endl; // not Stretched String so the program returns 0
    cout<<isStretched("ttaabbllee","table")<<endl; // Stretched String so the program returns 1
}

bool isStretched(string first,string second){

    vector <char> counter_array; // store just the characters of first string
    vector <pair  <char,int> > counter_vector; //characters and their number of occurrences
    vector<int> count;//just store number of occurrences
    vector<int>f;

    for(int i=0;i<first.length();i++){

        size_t counter = std::count(first.begin(), first.end(), first[i]);
        
        counter_vector.push_back(make_pair(first[i],counter));

    }
    counter_vector.erase( unique( counter_vector.begin(), counter_vector.end() ),counter_vector.end() );
  
    cout<<"Char  number of occurrences "<<endl;
    for(int i=0;i<counter_vector.size();i++){
        
        cout<<counter_vector[i].first<<"        "<<counter_vector[i].second<<endl;  
    }
    cout<<endl;
    cout<<"The program returns ";
    
    for(int i=0;i<counter_vector.size();i++){
        count.push_back(counter_vector[i].second);
    }
    
    for(int i=0;i<count.size();i++){
        if(count[i]!=count[0]){
            return false;
        }
    }
    
    for(int i=0;i<count.size();i++){
        if(count[i]==count[0]){
            return true;
        }
    }
    
    return true;
}
