#include<iostream>
using namespace std;
#include<string>
#include<cmath>
#include<vector>
#include<cmath>
#include<algorithm>

//---------------------------------------------------camelCase and snake_case string Conventor---------------------------------------------------------
//This program converts the string to camelCase or snake_case

//camelCase function converts the string into camelCase
string camelCaseFunction(string s);

//snake_case function converts the string into snake_case
string snake_case_function(string s);

int main(){
    
    camelCaseFunction("hello_world_this_is_programming");
    camelCaseFunction("computer_science");
    
    snake_case_function("computerScienceIsInteresting");
    snake_case_function("canadaIsBeautiful");
     
    return 0;
}

string camelCaseFunction(string s){

    for(int i=0;i<=s.length();i++){
        
        // find underscore
        if(s[i]=='_'){
            
            //underscore is at ith position
            // capitilize the char which is at position i+1 i.e after the underscore and store it into "after" variable
            char after=toupper(s[i+1]);
            
            s[i]=after;//replace underscore with uppercased char
            
            //remove the char at position i+1 (this char was lowercase version of newly capitilized char)
            s.erase(i+1,1);     
            
        }
          
    }
    cout<<s<<endl;
    return s;
}

string snake_case_function(string s){
    
    for(int i=0;i<=s.length();i++){
        char x=s[i];
        if(isupper(x)){
            char lower=tolower(x);
            s[i]=lower;
            s=s.insert(i,1,'_');// insert underscore before the char that was converted to lower case
            
        }
    }
    cout<<s<<endl;
    
    return s;
}
