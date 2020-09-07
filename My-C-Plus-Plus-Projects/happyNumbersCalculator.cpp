#include<iostream>
using namespace std;
#include<string>
#include<cmath>
#include<vector>
#include<cmath>
#include<algorithm>

//-------------------------------------------------------------Happy Numbers Calculator-----------------------------------------------------------------
// This calculator returns the total number of happy 0  and 1 numbers
// A 1 is unhappy when the digit to its left and the digit to its right are both 0s.
// A 0 is unhappy when the digit to its left and the digit to its right are both 1s.
// If a number has only one neighbor, it is unhappy if its only neighbor is different. Otherwise, a number is happy.

//function that takes in array of 0s and 1s
int happyNumbersCalculator(int arr[],int sizeOfArr);

int main(){
    
    int a[5]={1, 0, 0, 1, 1};
    
    int b[6]={1, 0, 0, 0, 1, 0};
    
    int c[7]={0, 1, 0, 0, 1, 0 ,0};
    
    int d[13]={0, 1, 1, 0,1,0,1,1,1,1,0,1,1};
    
    happyNumbersCalculator(a,5);
    happyNumbersCalculator(b,6);
    happyNumbersCalculator(c,7);
    happyNumbersCalculator(d, 13);    
}

int happyNumbersCalculator(int arr[],int sizeOfArr){
    
    vector<int>happy1;
    vector<int>happy0;
    vector<int>unhappy1;
    vector<int>unhappy0;
    vector<int>totalNumberOfZeros;
    vector<int>totalNumberOfOnes;
    
    //check the elements with one neighbor
    //check element at index 0
    if(arr[0]==1){
        if(arr[1]==0){
            unhappy1.push_back(1);
        }
        else{
            happy1.push_back(1);
        }
    }
    
    else if(arr[0]==0){
        if(arr[1]==1){
            unhappy0.push_back(1);
        }
        else{
            happy0.push_back(1);
        }
    }
    
    //last index is size of array minus 1
    //check the element located at last index
    if(arr[sizeOfArr-1]==1){
        if(arr[sizeOfArr-2]==0){
            unhappy1.push_back(1);
        }
        else{
            happy1.push_back(1);
        }
    }
    else if(arr[sizeOfArr-1]==0){
        if(arr[sizeOfArr-2]==1){
            unhappy0.push_back(1);
        }
        else{
            happy0.push_back(1);
        }
    }
    
    //check the elements with two neighbors
    //start from index 1 to second last (because we checked the last element in above)
    for(int i=1;i<sizeOfArr-1;i++){
        
        if(arr[i]==0){
            
            if(  (arr[i-1]==1 && arr[i+1]==1) || (arr[i-1]==0 && arr[i+1]==1) ||  (arr[i-1]==1 && arr[i+1]==0)  ){
                unhappy0.push_back(1);
            }
            
            //i.e if(arr[i-1]==0 && arr[i+1]==0)
            else{
                
                happy0.push_back(1);  
            }
        }
        
        //i.e if(arr[i]==1)
        else{
            
            if(  (arr[i-1]==0 && arr[i+1]==0) ||(arr[i-1]==1 && arr[i+1]==0) ||  (arr[i-1]==0 && arr[i+1]==1)  ){
                unhappy1.push_back(1);
            }
            
            //i.e if(arr[i-1]==1 && arr[i+1]==1)
            else{
                happy1.push_back(1);
            }
        }
    }
    
    for(int i=0;i<sizeOfArr;i++){
        if(arr[i]==1){
            totalNumberOfOnes.push_back(1);
        }
    }

    for(int i=0;i<sizeOfArr;i++){
        if(arr[i]==0){
            totalNumberOfZeros.push_back(0);
        }
    }

    cout<<"number of happy 0s are:"<<happy0.size()<<endl;
    cout<<"number of happy 1s are:"<<happy1.size()<<endl;
    cout<<"number of unhappy 0s are:"<<unhappy0.size()<<endl;
    cout<<"number of unhappy 1s are:"<<unhappy1.size()<<endl;
    cout<<"total number of 1s are: "<<totalNumberOfOnes.size()<<endl;
    cout<<"total number of 0s are: "<<totalNumberOfZeros.size()<<endl;
    int totalHappy=happy0.size()+happy1.size();
    cout<<"Total happy numbers are:"<<totalHappy<<endl;

    return totalHappy;
    
}
