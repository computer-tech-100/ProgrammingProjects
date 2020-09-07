#include<iostream>
using namespace std;
#include<string>
#include<cmath>
#include<vector>
#include<cmath>
#include<algorithm>
#include <regex>
#include<bitset>

//---------------------------------------------------------------------String Incrementer--------------------------------------------------------------
//Write a function which increments a string to create a new string.
//If the string ends with a number, the number should be incremented by 1.
//If the string doesn't end with a number, 1 should be added to the new string.
//If the number has leading zeros, the amount of digits should be considered.

void string_incrementer(string s);

int main(){
    
    string_incrementer("hello");// "hello1"
    
    string_incrementer("computer0009");// "computer0010"
    
    string_incrementer("coding099");// "coding100"
    
    string_incrementer("dog88");// "dog89"
    
    string_incrementer("sun000999");// "coding001000"
    
    string_incrementer("cat");// "cat1"
    
    string_incrementer("happiness2");// "happiness3"
    
    string_incrementer("cs0009999");// cs0010000
    
}

void string_incrementer(string s){
    vector<int>number;//this vector contains all non zero digits
    int size=s.length();
    int a=0;
    int b=0;
    vector<int> v;
    vector<int> my_vec(1);
    
    //when the string ends with no digits
    int last_char_index=size-1;
    if(!isdigit(s[last_char_index])){
        
        s=s.append("1");
        cout<<s<<endl;
        
    }

    //when the string ends with digits
    else{
        
        for(int i=0;i<size;i++){

            if(isdigit(s[i]) && s[i]!='0' ){
                
                char x = s[i];
                int y = x - '0';
                number.push_back(y);

            }
        }
    }
    
    //when there is only one non zero digit at the end
    if(number.size()==1){
        
        for(int i=0;i<number.size();i++){
            a=number[i]+1;  
        }
    }
    
    //when there is more than one non zero digit at the end
    else{
        
        for (int i = 0; i <number.size(); i++)
        {
            v.push_back(number[i]);
        }
        
        int count = 0;
        for (vector<int>::reverse_iterator element = v.rbegin(); element != v.rend(); element++) {
            
            my_vec[0] =my_vec[0] + ((*element) * pow(10, count));
            count++;
        }
        
        b=my_vec[0]+1;//incerement

    }
    
    string a1=to_string(a);//covert to string
    string b1=to_string(b);
    int a1_len=a1.length();
    int b1_len=b1.length();
    if(number.size()==1){
        
        //number of chars that we remove from the string = length of incremented number
        s.erase(s.length()-a1_len);
        s=s.append(a1);//append inceremented number to the string
        cout<<s<<endl;   
    }
    else{
        
        s.erase(s.length()-b1_len);
        s=s.append(b1);
        cout<<s<<endl;
    }
}
