#include<iostream>
using namespace std;
#include<string>
#include<cmath>
#include<vector>
#include<cmath>
#include<algorithm>

//---------------------------------------------------------------String Remixer-------------------------------------------------------------------------
// This is a program that remixes the string
// Our function takes a string and an array of numbers as arguments. Rearrange the letters in the string to be in the order specified by the index number then return the "remixed" string.

string remix_my_string(string s, int arr[],int sizeOfArr);

int main(){

    int a1[4]={0, 3, 1, 2};
    int a2[4]={1, 3, 0, 2};
    int a3[8]={0, 2, 1, 5, 3, 6, 7, 4};
    
    remix_my_string("wxyz", a1,4); // the remixed string is "wyzx"
    
    remix_my_string("four",a2,4) ;//ufro
    
    remix_my_string("engineer", a3,8); // egnnriee
    
}

string remix_my_string(string s, int arr[],int sizeOfArr){
    
    vector<char> v1;// we split our string and store it's characters inside vector v1
    vector<int>v2;// we store elements of our array insode vector v2
    
    //we append the vector v1 by charactors of our string
    for(int i=0;i<=s.length();i++){
        v1.push_back(s[i]);
        
    }
    
    cout<<"This is a vector containing charactors of our string:"<<endl;
    for(int i=0;i<=v1.size();i++){
        
        cout<<v1[i]<<endl;
    }
    
    //we append the vector v2 by elements of our array
    cout<<"This is a vector containing elements of our array:"<<endl;
    for(int i=0;i<=sizeOfArr;i++){
        
        v2.push_back(arr[i]);
        
    }
    for(int i=0;i<=v2.size();i++){
        cout<<v2[i]<<endl;
    }
    
    for(int i=0;i<sizeOfArr;i++){
        //get charactor i of string and element i of array
        int index=v2[i];
        char x=v1[i];// x is a char that is at position i
        cout<<" Now the char "<<x<< " should be moved to index --> "<<index<<endl;
    
        s.insert(index,1,x);// insert char x to index only once
        s.erase(index+1,1);//erase the charactor at index+1 becuae it was moved to another index and is no longer needed
    }
    
    cout<<s<<endl;
    return s;
}
