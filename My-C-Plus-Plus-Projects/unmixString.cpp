#include<iostream>
using namespace std;
#include<string>
#include<cmath>
#include<vector>
#include<cmath>
#include<algorithm>
#include <regex>
#include<bitset>

//-----------------------------------------------------------------------------Unmix Strig-----------------------------------------------------------------
//The program unmixes the string to make it readable.

void unmix(string s);

int main(){
    string s1="123456";//--> 214365
    string s2="hTsii  s aimex dpus rtni.g";//--> This is a mixed up string.
    string s3="badce";//-->abcde
    string s4="ehllo";//-->hello
    unmix(s1);
    unmix(s2);
    unmix(s3);
    unmix(s4);
}
void unmix(string s){

    for(int i=0;i<s.length();i++){
        swap(s[i],s[i+1]);//swap two chars
        cout<<s[i];
        cout<<s[i+1];
        s.erase(s.begin() + (i+1));//remove char at position i+1
    }
    cout<<endl;
}
