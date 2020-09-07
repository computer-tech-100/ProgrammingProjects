#include <iostream>
using namespace std;

//this is Implementation of  an iteration version of BinarySearch for an array of numbers
int binarySearch(int array[], int size,int Value){

	int smallestIndex=0;
	int biggestIndex=size-1;
	int middleIndex;
	while (smallestIndex<=biggestIndex){

		middleIndex=(smallestIndex+biggestIndex)/2;

		if(Value==array[middleIndex]){
			return middleIndex;
		}
		else if(Value>array[middleIndex]){
			smallestIndex=middleIndex+1;
		}
		else{
			biggestIndex=middleIndex-1;
		}
	}
        // if the compiler cannot find the value we return -1
	return -1;
}

int main(){
	
	int a[]={4,7,9,12,13,20,25,30};
	int userValue;
	cout<<"enter a number among the array A={4,7,9,12,13,20,25,30}:"<<endl;
	cin>>userValue;
	//call the function
	int index=binarySearch(a,8,userValue); //8 is size of array and Value is the value or number that user enters
	if(index>=0){
		cout<<"the number "<<a[index] <<" is at index"<<index<<endl;
	}
	else{
		cout<<"the number"<<userValue<<"is not found"<<endl;
	}
	system("pause");
}
