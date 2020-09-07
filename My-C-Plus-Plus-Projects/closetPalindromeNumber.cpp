#include<iostream>
using namespace std;
#include<string>
#include<cmath>
#include<vector>
#include<cmath>
#include<algorithm>
#include <regex>

//-------------------------------------------------------------------Closest Palindrome Number-----------------------------------------------------------
// This program returns the closest palindrome number. If two palindrome numbers tie in absolute distance, then the program returns the smaller number.
// example: 23  --> the program returns 22 which is closest palindrome
// 100 --> the closest palindrome numbers are 99 and 101 so the program returns the smaller one which is 99
// single numbers 0,1,2,3,4,5,6,7,8,9 are palindrome

int closest_palindrome_number(int number);

int main(){

    closest_palindrome_number(100); // returns 99
    closest_palindrome_number(15);// returns 11
    closest_palindrome_number(5);// single number is palindrome
    closest_palindrome_number(55);//this number is palindrome itself
}

int closest_palindrome_number(int number){
    int length=0;
    int num=number;
    vector<int>smallerThan;//vector of all numbers that are smaller than number
    vector<int>biggerThan;//vector of all numbers that are bigger than number
    vector<int> v;//vector of palindromes that are smaller than number
    vector<int> v2;//vector of palindromes that are bigger than number

    string x=to_string(number);
    int y=x.length()/2;
    int smaller=x.length()-1;
    for(int digit=0;digit<y;digit++){
        int previous=smaller-digit;
        if(x[digit] == x[previous]){
            cout<<"the number is palindrome"<<endl;
        }
    }
    if (0<=number && number<=9){
        cout<<"single number is palindrome"<<endl;
    }
    
    //numbers that are smaller than current number
    while(number!=0){
        
        number--;
        smallerThan.push_back(number);   
    }
    
    for(int i=0;i<smallerThan.size();i++){
        
        string w=to_string(smallerThan[i]);
        int l=w.length()/2;
        int s=w.length()-1;
        for(int j=0;j<l;j++){
            int pre=s-j;
            if(w[j] == w[pre]){
                v.push_back(smallerThan[i]);
            }     
        }    
    }
    
    //find closest palindrome that is before number
    int closest_before=*max_element(v.begin(), v.end());
    cout<<"Closest palindrome that is before the number is "<<closest_before<<endl;
    
    //numbers that are bigger than current number
    int b=num+100;
    while(num!=b){
        
        num++;
        biggerThan.push_back(num);  
    }

    for(int i=0;i<biggerThan.size();i++){

        string a=to_string(biggerThan[i]);
        int e=a.length()/2;
        int u=a.length()-1;
        for(int n=0;n<e;n++){
            int p=u-n;
            if(a[n] == a[p]){
                v2.push_back(biggerThan[i]);
            }
        }  
    }
    
    //find closest palindrome that is after number
    int closest_after=*min_element(v2.begin(), v2.end());
    cout<<"Closest palindrome that is after the number is "<<closest_after<<endl;
    
    //calculate distances
    int before=abs(number-closest_before);
    int  after=abs(closest_after-number);
    
    //if we have palindromes in absolute distance then we return the smaller one
    if(before==1 && after==1){
        
        cout<<"closest palindrome is "<<closest_before<<endl;
    }
    
    //otherwise we return the one which is closer to the number
    else{
        cout<<"Hence the closest palindrome is "<<min(before,after)<<endl;
    }
    
    return 0;
}
