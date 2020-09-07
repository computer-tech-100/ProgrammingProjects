#include<iostream>
using namespace std;
#include<string>
#include<cmath>
#include<vector>
#include<cmath>
#include<algorithm>
#include <regex>

//---------------------------------------------------------------------------Anagram---------------------------------------------------------------------
//This program returns true(1) if Anagram exits otherwise returns false(0)
//Anagram of first string should exist in second string for example Anagrams of "bag" are "bag", "bga", "abg", "agb", "gab", "gba"

bool anagram(string s1,string s2);

int main(){
    
    anagram("bag", "bga");//true
    
    anagram("cat", "act"); // true
    
    anagram("sun", "son"); //false
    
    anagram("good", "friend"); //false   
}

bool anagram(string s1,string s2){
    
    //we need to have all permutation of s1
    sort(s1.begin(), s1.end());
    vector<string> anagrams; // this vector contains all anagrams
    vector<bool>isAangram;
    
    //add anagrams to vector
    do {
        
        anagrams.push_back(s1);
    }while (next_permutation(s1.begin(), s1.end()));
    
    cout<<"All anagrams of string 1 are:"<<endl;
    for(int i=0;i<anagrams.size();i++){
        cout<<anagrams[i]<<endl;
    }
    cout<<endl;
    cout<<"In the following if anagram exists in string2 then 1 is infront of that anagram otherwise it is 0."<<endl;
    cout<<"Anagrams   T/F"<<endl;
    
    for(int i=0;i<anagrams.size();i++){
        
        //if any of the anagrams is in string s2
        if (s2.find(anagrams[i]) != string::npos){
            
            cout<<anagrams[i]<<"         "<<true<<endl;
            isAangram.push_back(true);   
        }
        
        //if any of the anagrams is not in string s2
        else{
            
            cout<<anagrams[i]<<"         "<<false<<endl;   
        }    
    }
    // at last the program returns true if anagram exits otherwise it returns false
    if(isAangram.size()!=0){
        cout<<true<<endl;
    }
    else{
        cout<<false<<endl;
    }
    
    return true;
}
