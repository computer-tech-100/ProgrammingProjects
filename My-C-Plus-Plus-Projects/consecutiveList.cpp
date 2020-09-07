#include<iostream>
using namespace std;
#include<string>
#include<cmath>
#include<vector>
#include<cmath>
#include<algorithm>
#include <regex>
#include<bitset>

//------------------------------------------------------------------------------Consecutive List---------------------------------------------------------
//This program determines if elements in an array can be rearranged to form a consecutive list of numbers where each
//number appears exactly once.

bool consecutive_list(int arr[],int size);

int main(){
    int a[]={5, 1, 4, 3, 2};
    int b[]={2, 5, 4, 10, 3,8 };
    int c[]={6, 7, 8, 9, 10, 10};
    
    cout<<consecutive_list(a,5)<<endl; //true --> because after rearrangement we will have 1,2,3,4,5
    
    cout<<consecutive_list(b,6)<<endl;//false
    
    cout<<consecutive_list(c,6)<<endl; //false because 10 is appeared twice
      
}

bool consecutive_list(int arr[],int size){
    
    vector<bool>consecutive;
    sort(arr, arr+size);
    for(int i=0;i<size-1;i++){
        
        if(arr[i]==arr[i+1]-1){
            consecutive.push_back(true);
        }
        
        else{
            consecutive.push_back(false);
        }
        
    }
    
    if ( std::equal(consecutive.begin() + 1, consecutive.end(), consecutive.begin()) ){
        return true;
    }
    else{
        return false;
    }
      
}
