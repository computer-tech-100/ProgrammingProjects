#include<iostream>
using namespace std;
#include<string>
#include<cmath>
#include<vector>
#include<cmath>
#include<algorithm>
#include <regex>
#include<bitset>

//-----------------------------------------------------------------------------Triple and Double-------------------------------------------------------
//This program returns true ( i.e 1) if a number repeats three times in a row at any place in integer1 AND that same number repeats two times in a row in integer2.

bool repeat(long n1,long n2);

int main(){
    
    cout<<repeat(451999277, 4117772299)<<endl; //true
    
    cout<<repeat(1222345, 12345)<<endl; //false
    
    cout<<repeat(666789, 12345667)<<endl; //true
    
    cout<<repeat(33789, 12345337)<<endl;; //false
      
}

bool repeat(long n1,long n2){
    vector<char>common;
    vector<bool>isTripleDouble;
    vector<bool>isNotTripleDouble;
    
    string s1=to_string(n1);
    string s2=to_string(n2);
    
    for(int i=0;i<s2.length();i++){
        for(int j=0;j<s1.length();j++){
            if( s1[j]==s2[i]){
                common.push_back(s1[j]);
                break;
            }   
        }      
    }
    
    for(int i=0;i<s1.length();i++){
        
        for(int j=0;j<s2.length();j++){
            
            //3 times in first int and 2 times in second int
            if(s1[i]==s1[i-1] && s1[i]==s1[i+1]){
                if(s2[j]==s2[j+1] || s2[j]==s2[j-1]){
                    
                    isTripleDouble.push_back(true);
                    
                    break;  
                }
            }
            else{
                
                isNotTripleDouble.push_back(true);
                break;
            }  
        }
    }
    
    if(isTripleDouble.size()!=0){
        
        return true;
    }
    else {
        
        return false;
    }
}
