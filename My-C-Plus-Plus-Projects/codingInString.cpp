#include<iostream>
using namespace std;
#include<string>
#include<cmath>
#include<vector>
#include<cmath>
#include<algorithm>
#include <regex>
#include<bitset>

//----------------------------------------------------------------------Coding in String---------------------------------------------------------------
// This program determines if the string contains a subsequence of the word coding or not.
// A string contains the word "coding" if a subsequence of its characters spell "coding".

//function that takes in a string and returns “yes” if the string contains a subsequence of the word coding or "no" if it does not.
void is_coding_in_string(string s);

int main(){
    
    is_coding_in_string("xbchelloadvneiwodnlg");//yes
    
    is_coding_in_string("cmterdksneqoacxdakml");//no
    
    is_coding_in_string("cdaaandt"); //no
    
    is_coding_in_string("cgwornisadletodiwnag");//yes
    
    is_coding_in_string("obndqcdfghigkamnopqrstvwxzngdc"); //no

}

void is_coding_in_string(string s){
    
 //vectors that contain indices
    vector<int>c;
    vector<int>o;
    vector<int>d;
    vector<int>ii;
    vector<int>n;
    vector<int>g;
    
    int c_index;
    
     //check if char c exists in string s(we do this for every other chars that is in 'coding')
     if (s.find('c') != string::npos) {
          c_index=s.find('c');
     }
     else{
         //if char c does not exist in the string then we set the index to -1 (we also do this for other chars in 'coding' )
         c_index=-1;
     }

    //find all indices of char 'o' and then add those indices to the corresponding vector
    for(int i=0;i<s.length();i++){
        if(s[i]=='o'){
            o.push_back(i);
        }
    }
    
    //we find indices of every char of the word 'coding' and push the indices into their corresponding vector
    for(int i=0;i<s.length();i++){
        if(s[i]=='d'){
            d.push_back(i);
        }
    }
    
    for(int i=0;i<s.length();i++){
        if(s[i]=='i'){
            ii.push_back(i);
        }
    }
    
    for(int i=0;i<s.length();i++){
        if(s[i]=='n'){
            n.push_back(i);
        }
    }
    for(int i=0;i<s.length();i++){
        if(s[i]=='g'){
            g.push_back(i);
        }
    }
    
    int o_index;
    
    if (s.find('o') != string::npos) {
     
        
        for(int i=0;i<o.size();i++){
            
            //we consider the first occurence of char 'o' that happened after char 'c'
            if(o[i]>c_index  ){
                o_index=o[i];
                break;
                
            }
        }
    }
    else{
        o_index=-1;//set index to -1 if char 'o' does not exist in the string
            
        }
    int d_index;
    
    if (s.find('d') != string::npos){
        
    for(int i=0;i<d.size();i++){
        //we consider the first occurence of char 'd' that happened after char 'o'
        if(d[i]>o_index){
            d_index=d[i];
            break;
        }
      }
    }
    else{
        d_index=-1;
    }
    
    int i_index;
    
    if (s.find('i') != string::npos){
    for(int i=0;i<ii.size();i++){
        
        //we consider the first occurence of char 'i' that happened after char 'd'
        if(ii[i]>d_index){
            i_index=ii[i];
            break;
        }
      }
    }
    else{
        i_index=-1;
    }
    
    int n_index;
    if (s.find('n') != string::npos) {
        
    //we consider the first occurence of char 'n' that happened after char 'i'
    for(int i=0;i<n.size();i++){
        if(n[i]>i_index){
            n_index=n[i];
            break;
        }
      }
    }
    else{
        n_index=-1;
    }
    
    int g_index;
    
    if (s.find('g') != string::npos){
        
    //we consider the first occurence of char 'g' that happened after char 'n'
     for(int i=0;i<g.size();i++){
        if(g[i]>n_index){
            g_index=g[i];
            break;
        }
      }
    }
  else{
      g_index=-1; 
  }
    
    //check if all the chars (that are in 'coding') exist and appear one after another in the string
    //If this is the case print yes otherwise print no
    for(int i=0;i<s.length();i++){
        if(c_index!=-1 && o_index!=-1 && d_index!=-1 && i_index!=-1 && n_index!=-1 && g_index!=-1){
            if(c_index<o_index && o_index<d_index && d_index<i_index && i_index<n_index&& n_index<g_index){
                cout<<"yes";
                break;
            }
            else{
                cout<<"no";
                break;
            }
        }
        else{
            cout<<"no";
            break;
        }    
    }
    
    cout<<"\n";
}
