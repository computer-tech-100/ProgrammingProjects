#include<iostream>
using namespace std;
#include<string>
#include<cmath>
#include<vector>
#include<cmath>
#include<algorithm>
#include <regex>
#include<bitset>

//-----------------------------------------------------------------------A Capital Challenge----------------------------------------------------------------
//Given two strings, s1 and s2, select only the characters in each string where the character in the same position in the
//other string is in uppercase. The program returns these as a single string.

void capital_challenge(string x,string y);

int main(){
    
    capital_challenge("heLLO", "GUlp");//help
    
    capital_challenge("98765", "YyYyY");//975
    
    capital_challenge("cOmputer", "CanadaxO");//car
        
}

void capital_challenge(string x,string y){
    vector<char>box;
    
    for(int i=0;i<x.length();i++){
        
        if(isupper(y[i])){
            box.push_back(x[i]);
        }
        if(isupper(x[i])){
            box.push_back(y[i]);
        }
    }
    for(int i=0;i<box.size();i++){
        cout<<box[i];
    }
    cout<<endl;    
}
