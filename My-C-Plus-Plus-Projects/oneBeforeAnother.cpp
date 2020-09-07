#include<iostream>
using namespace std;
#include<string>
#include<cmath>
#include<vector>
#include<cmath>
#include<algorithm>
#include <regex>
#include<bitset>

//-------------------------------------------------------------------------One Before Another----------------------------------------------------------
//This program determines if every instance of the first char occurs before every instance of the second char.If this is a case then it returns true otherwise false

//function gets three inputs: a string, first char, second char
bool oneBeforeAnother(string s, char x, char y);

int main(){
    
    cout<<oneBeforeAnother("a cat jumps joyfully", 'a', 'j')<<endl;//  true
    //every instance of "a" occurs before every instance of "j"
    
    cout<<oneBeforeAnother("Computer science is interesting", 'c', 'g')<<endl;// true
    
    cout<<oneBeforeAnother("happy birthday ", 'a', 'y')<<endl;// false since the "a" in "birthday" occurs after the "y" in "happy"
    
    cout<<oneBeforeAnother("Canada is beautiful", 'a', 's')<<endl;// false since "a" in beautiful occures after "s" in "is"
    
}

bool oneBeforeAnother(string s, char x, char y){
    
    vector<int>index_firstChar;//this vector contains indices of first char
    
    vector<int>index_secondChar;////this vector contains indices of second char
    
    vector<bool>not_before;//this vector is empty if all occurences of first char happen before the second char
    
    //get index
    for(int i=0;i<s.length();i++){
        
        if(s[i]==x){
            index_firstChar.push_back(i);
        }
        
        if(s[i]==y){
            index_secondChar.push_back(i);  
        }
    }
    
    //if index of first char is smaller than index of second char then first char is occured before the second char
    //we check this for every occurence of first char
    for(int i=0;i<index_firstChar.size();i++){
        for(int j=0;j<index_secondChar.size();j++){
            if(index_firstChar[i]>index_secondChar[j]){
                
                // if first char occurs after second char then we append true to not_before vector
                not_before.push_back(true);
            }
        }
    }
    
    //since first char occured after the second char we return false (i.e not_before vector is not empty)
    if(not_before.size()!=0){
        return false;
    }
    else{
        return true;
    }
}
