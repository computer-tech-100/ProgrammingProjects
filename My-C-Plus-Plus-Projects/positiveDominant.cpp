#include<iostream>
using namespace std;
#include<string>
#include<cmath>
#include<vector>
#include<cmath>
#include<algorithm>
#include <regex>
#include<bitset>

//------------------------------------------------------------------------Positive Dominant-------------------------------------------------------
//Positive Dominant: if we have more unique positive values than unique negative values in our array then we return true
//otherwise we return false
//zero is not positive and not negative

bool positiveDominant(int arr[],int size);
int main(){
    
    //false since 2 is an only one unique positive value. -2 and -5 are two unique negative values
    int arr1[]={2, 2, 2, 2, -2, -5};
    
    int arr2[]={6, 88, 401, -1, -4}; // true
    
    int arr3[]={4, 3,-2}; // true
    
    int arr4[]={0, -2, -9,-9}; // false
    
    cout<<positiveDominant(arr1,6)<<endl;
    
    cout<<positiveDominant(arr2,5)<<endl;
    
    cout<<positiveDominant(arr3,3)<<endl;
    
    cout<<positiveDominant(arr4,3)<<endl;  
}

bool positiveDominant(int arr[],int size){
    
    vector<int>positives;
    vector<int>negatives;
    
    for(int i=0;i<size;i++){
        if(arr[i]>0){
            
            positives.push_back(arr[i]);
        }
        else{
            
            negatives.push_back(arr[i]);
        }
    }
    
    //consider unique positive values
    positives.erase( unique( positives.begin(), positives.end() ), positives.end() );

    //consider unique negative values
    negatives.erase( unique( negatives.begin(), negatives.end() ), negatives.end() );

    if(positives.size()>negatives.size()){
        
        return true;
    }
    else{
        return false;
    }   
}
