#include<iostream>
using namespace std;
#include<string>
#include<cmath>
#include<vector>
#include<cmath>
#include<algorithm>
#include <regex>
#include<bitset>

//-----------------------------------------------------------------------longest common ending------------------------------------------------------------
//This program returns the longest common ending between two strings.

void l_c_e(string, string);

int main(){
    
    l_c_e("addition", "action"); // "tion"
    
    l_c_e("exponent", "talent"); // "ent"
    
    l_c_e("funny","sunny" );//nny
    
    l_c_e("cat", "dog"); //""
    
}

void l_c_e(string s1,string s2){
    
    vector<char>same;
    
    //reverse two strings
    reverse(s1.begin(), s1.end());
    
    reverse(s2.begin(), s2.end());
    
    //check each char one by one
    for(int i=0;i<s1.length();i++){
        if(s1[i]==s2[i] && s2[i]==s1[i]){
            same.push_back(s1[i]);
        }
        else{
            cout<<" "<<endl;
            break;
        }
    }
    reverse(same.begin(), same.end());
    for(int i=0;i<same.size();i++){
        cout<<same[i];
        
    }
    cout<<endl;
}
