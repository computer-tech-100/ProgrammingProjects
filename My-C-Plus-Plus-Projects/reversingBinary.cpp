#include<iostream>
using namespace std;
#include<string>
#include<cmath>
#include<vector>
#include<cmath>
#include<algorithm>
#include <regex>
#include<bitset>

//-----------------------------------------------------------------------------Reversing a Binary--------------------------------------------------------
//This program returns a new integer from reveresed binary
//this function that takes in a positive integer , reverses the binary representation of that integer, and returns the new integer from the reversed binary.

int reversingBinary(int n);

int main(){
    
    reversingBinary(10); // 5
    // 10 = 1010 -> 0101 = 5
    
    reversingBinary(12); // 3
    // 12 = 1100 -> 0011 = 3
    
    reversingBinary(25); // 19
    // 25 = 11001 -> 10011 = 19
    
    reversingBinary(45); // 45
    // 45 = 101101 -> 101101 = 45
    
}

int reversingBinary(int my_number){
    
    int size=(int)log2(my_number)+1;//get size of binary
    int new_integer;
    
    if(my_number<0){
        cout<<"Number should be positive."<<endl;
    }
    else{
        if(size==2){

            string my_binary = bitset<2>(my_number).to_string(); //convert number to binary
            cout<<"Binary:"<<my_binary<<endl;
            reverse(my_binary.begin(),my_binary.end());//reverse the binary
            cout<<"Reversed Binary:"<<my_binary<<endl;
            
            int n = bitset<2>(my_binary).to_ulong();//convert binary to number
            new_integer=n;
            cout<<"New integer:"<<n<<endl;
        }
        if(size==3){

            string my_binary = bitset<3>(my_number).to_string();
            cout<<"Binary:"<<my_binary<<endl;
            reverse(my_binary.begin(),my_binary.end());
            cout<<"Reversed Binary:"<<my_binary<<endl;
            
            int n = bitset<3>(my_binary).to_ulong();
            new_integer=n;
            cout<<"New integer:"<<n<<endl;
        }
        if(size==4){

            string my_binary = bitset<4>(my_number).to_string();
            cout<<"Binary:"<<my_binary<<endl;
            reverse(my_binary.begin(),my_binary.end());
            cout<<"Reversed Binary:"<<my_binary<<endl;
            
            int n = bitset<4>(my_binary).to_ulong();
            new_integer=n;
            cout<<"New integer:"<<n<<endl;
        }
        if(size==5){

            string my_binary = bitset<5>(my_number).to_string();
            cout<<"Binary:"<<my_binary<<endl;
            reverse(my_binary.begin(),my_binary.end());
            cout<<"Reversed Binary:"<<my_binary<<endl;
            
            int n = bitset<5>(my_binary).to_ulong();
            new_integer=n;
            cout<<"New integer:"<<n<<endl;
        }
        if(size==6){

            string my_binary = bitset<6>(my_number).to_string();
            cout<<"Binary:"<<my_binary<<endl;
            reverse(my_binary.begin(),my_binary.end());
            cout<<"Reversed Binary:"<<my_binary<<endl;
            
            int n = bitset<6>(my_binary).to_ulong();
            new_integer=n;
            cout<<"New integer:"<<n<<endl;
        }
        if(size==7){

            string my_binary = bitset<7>(my_number).to_string();
            cout<<"Binary:"<<my_binary<<endl;
            reverse(my_binary.begin(),my_binary.end());
            cout<<"Reversed Binary:"<<my_binary<<endl;
            
            int n = bitset<7>(my_binary).to_ulong();
            new_integer=n;
            cout<<"New integer:"<<n<<endl;
        }
        if(size==8){

            string my_binary = bitset<8>(my_number).to_string();
            cout<<"Binary:"<<my_binary<<endl;
            reverse(my_binary.begin(),my_binary.end());
            cout<<"Reversed Binary:"<<my_binary<<endl;
            
            int n = bitset<8>(my_binary).to_ulong();
            new_integer=n;
            cout<<"New integer:"<<n<<endl;
        }
    }
    return new_integer ;
}
