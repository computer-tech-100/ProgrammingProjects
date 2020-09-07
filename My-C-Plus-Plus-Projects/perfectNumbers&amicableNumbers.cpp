#include<iostream>
using namespace std;
#include<string>
#include<cmath>
#include<vector>
#include<cmath>
#include<algorithm>
#include <regex>

//-------------------------------------------------------------Perfect Numbers and Amicable Numbers------------------------------------------------------
//This program returns perfect if given number is perfect or returns amicable if the number is amicable or none otherwise
//Given a positive number x, if all the positive divisors of x (excluding x) add up to x, then x is said to be a perfect number.
//For example, the set of positive divisors of 6 excluding 6 itself is (1, 2, 3). The sum of this set is 6. Therefore, 6 is a perfect number.
//Given a positive number x, if all the positive divisors of x add up to a second number y, and all the positive divisors of y add up to x, then x and y are said to be a pair of amicable numbers.

int p_or_a(int x, int y);

int main(){
    
    p_or_a(6, 0);//perfect
    
    p_or_a(220,284);//amicable pair
    
    p_or_a(24,20);//none
     
}

int p_or_a(int x, int y){
    
    vector<int> x_divisors;//vector of divisors of first number i.e x
    
    vector<int> y_divisors;//vector of divisors of second number i.e y
    
    //find divisors of number x
    for(int i=1;i<x;i++){
        if(x%i==0){
            x_divisors.push_back(i);
        }
    }
    
    int sum_of_x_divisors=0;
    for(int i=0;i<x_divisors.size();i++){
        
        sum_of_x_divisors+=x_divisors[i];
    }
    
    cout<<"Divisors of first number are: "<<endl;
    for(int i=0;i<x_divisors.size();i++){
        cout<<x_divisors[i]<<endl;
    }
    cout<<"Sum of the divisors of first number is "<<sum_of_x_divisors<<endl;
    
    if(sum_of_x_divisors==x){
        cout<<"The number is perfect"<<endl;
    }
    
    //find divisors of number y
    for(int i=1;i<y;i++){
        if(y%i==0){
            y_divisors.push_back(i);
        }
    }
    
    int sum_of_y_divisors=0;
    for(int i=0;i<y_divisors.size();i++){
        
        sum_of_y_divisors+=y_divisors[i];
    }
    
    cout<<"Divisors of second number are: "<<endl;
    for(int i=0;i<y_divisors.size();i++){
        cout<<y_divisors[i]<<endl;
    }
    cout<<"Sum of the divisors of second number is "<<sum_of_y_divisors<<endl;
    
    
    if(sum_of_x_divisors==y && sum_of_y_divisors==x){
        cout<<"This is a pair of amicable numbers"<<endl;
    }
    else{
        cout<<"None"<<endl;
    }
    
    return -1;  
}
