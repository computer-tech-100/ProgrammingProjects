#include <iostream>
using namespace std;

int main() {
	int array[100];
	int i=0,j;
	int number;
	cout<<"enter positive number:"<<endl;
	cin>>number;
	while(number>0){
		array[i]=number%2;
		i++;
		number=number/2;
	}
	cout<<"Binary number is:"<<endl;
	for(j=i-1;j>=0;j--){
		cout<<array[j];
	}
	return 0;
}
