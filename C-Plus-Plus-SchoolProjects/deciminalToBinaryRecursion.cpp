#include <iostream>
using namespace std;

void binary(int n){
	int remainder;
	remainder=n%2;
	if(n>0){
		binary(n/2);
		cout<<remainder;
	}
}

int main() {

	int n;
	cout<<"enter a number:"<<endl;
	cin>>n;
	binary(n);
	return 0;
}
