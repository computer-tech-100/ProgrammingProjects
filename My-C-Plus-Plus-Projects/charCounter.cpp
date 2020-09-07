#include<iostream>
using namespace std;
#include<string>
#include<cmath>
#include<vector>
#include<cmath>
#include<algorithm>
#include <regex>
#include<bitset>

//------------------------------------------------------------------------Char Counter-------------------------------------------------------------------
// The program returns array of numbers. These are number of times a character appears in each word in a sentence.
// example:  Jerry stdies harder than ever.--> we want to count character e in each word so the program returns [1,1,1,0,2]
// note that uppercase and lowercase are both counted for example :
// I eat an Apple And An orange --> count character A ---> [0,1,1,1,1,1,1]  -> i.e beside uppercase A we also count the lowercase ones

void ArrOfNum(char c);

int main(){
    
    ArrOfNum('a');   
}

void ArrOfNum(char c){
    string s;
    string w;
    char my_char1=toupper(c);
    char my_char2=tolower(c);
    
    cout<<"Enter a sentence:";
    getline(cin,s);
    
    for(int i=0;i<s.length();i++){
        
        if(s[i]==c){
            s[i]=c;
        }
        else{
            if(s[i]==my_char1 || s[i]==my_char2){
                s[i]=c;
            }
        }
    }
    
    vector<string>words;
    string each_word = " ";
    vector<int>num;
    
    for (char my_str : s)
    {
        if (my_str != ' ')
        {
            
            each_word +=  my_str;
        }
        else
        {
            
            words.push_back(each_word);
            each_word = " ";   
        }
    }
    
    words.push_back(each_word);
    
    for(int i=0;i<words.size();i++){
        
        //count number of times character c apears in each word
        size_t counter = count(words[i].begin(), words[i].end(), c);
        num.push_back(counter);    
    }
    
    for(int i=0;i<num.size();i++){
        cout<<num[i]<<endl;   
    }
}
