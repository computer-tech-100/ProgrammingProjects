#include<iostream>
using namespace std;
#include<string>
#include<cmath>
#include<vector>
#include<cmath>
#include<algorithm>

//----------------------------------------------------------Common Char Counter-------------------------------------------------------------------------
// The following program counts the number of common charactors between two given words

int commonChar(string s1,string s2); //declare function
int main() {
    
    //call the function
    commonChar("lemon", "orange"); // 3 because "eon" is common between "lemon" and "orange"
    
    commonChar("meat", "meet"); // 3
    
    commonChar("son", "sun"); // 2
     
}

int commonChar(string str1,string str2){
    
    vector<char>arr1; // to store characters of s1
    vector<char>arr2;// to store characters of s2
    vector<char>common;// to store common characters between two words
    
    // insert characters of str1 to arr1
    for(int i=0;i<=str1.length();i++){
        
        arr1.push_back(str1[i]);  
        
    }
    // insert characters of str2 to arr2
    for(int i=0;i<str2.length();i++){
        
        arr2.push_back(str2[i]);
        
    }
    for(int i=0;i<arr1.size();i++){
        cout<<arr1[i]<<endl;
        
    }
    
    for(int i=0;i<arr2.size();i++){
        cout<<arr2[i]<<endl;
        
    }
    
    cout<<endl;
    
    //find shared characters and insert them into common vector
    for (vector<char>::iterator j = str1.begin(); j != str1.end(); j++)
    {
        if (find(str2.begin(), str2.end(), *j) != str2.end())
        {
            common.push_back(*j);
        }
    }
    cout<<"common element(s) between two words:"<<endl;
    for(int i=0;i<common.size();i++){
        
        cout<<common[i]<<endl;
    }
    int count=common.size();
    cout<<"number of common elements is:"<<count<<endl;
    return count;
     
}
