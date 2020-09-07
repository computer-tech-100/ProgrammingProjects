#include<iostream>
using namespace std;
#include<string>
#include<cmath>
#include<vector>
#include<cmath>
#include<algorithm>

//----------------------------------------------------------------------Boomerangs---------------------------------------------------------------------
// The following program counts the number of boomerangs in an array
// Boomerang is a sub array that has following characteristics:
// length of sub array is 3
// Both first and last elements are identical but middle element is different from first and last elements
// boomerangs can overlap

int boomerang_counter(int arr[],int s);
int main(){
    
    int arr1[10]={2,3,2,1,2,4,5,4,5,0};
    boomerang_counter(arr1,10); //4
    
    int arr2[9]={ 9, 5, 9, 5, 1, 1, 1, 2 , 1};
    boomerang_counter(arr2,9); // 3
    
    int arr3[7]={10, 6, 6, 13, 6, 13, 9};
    boomerang_counter(arr3,7); // 2
    
    int arr4[7]={3, 1, 3, 9, 2, 1, 6};
    boomerang_counter(arr4,7); //1
    
    int arr5[7]={3, 3, 3, 7, 7, 7, 7};
    boomerang_counter(arr5,7); //0
    
    int arr6[]={}; // empty array
    boomerang_counter(arr6,0);
     
}

int boomerang_counter(int arr[],int s){
    
    int oneToLast=s-1;
    int counter=0;
    
    // if input array is empty
    if(s==0){
        cout<<"Array is empty and we have no boomerang"<<endl;
    }
    
    //if input array is not empty
    else{
        //start loop from index 1 to one to last element
        cout<<"The sub arrays of length 3 are:"<<endl;
        for(int i=1;i<oneToLast;i++){
            
            int before=arr[i-1];//first
            int middle=arr[i];// middle
            int after=arr[i+1];//last
            cout<<before<<endl;
            cout<<middle<<endl;
            cout<<after<<endl;
            cout<<endl;
            cout<<endl;
            
            // we increment the counter if first and last elements are the same but both are different from middle element
            if(before==after && middle!=before && middle!=after){
                counter++;
            }
        }
    }
    cout<<"Number of boomerangs are:"<<counter<<endl;
    
    return counter;
}
