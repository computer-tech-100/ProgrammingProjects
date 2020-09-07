#include <iostream>
using namespace std;

void enque(int x);
int deqeue();
int queue[10];
int front =-1;
int back=-1;
int main() {
	enque(1);
	enque(2);
	enque(3);
	enque(4);
	enque(5);
	enque(6);
	enque(7);
	enque(8);
	enque(9);
	enque(10);
	cout<<endl;
	deqeue();
	deqeue();
	for(int i=front;i<back;i++){
		cout<<queue[i]<<" ";
	}
	return 0;
}
void enque(int x){

	if(back==9){
		cout<<"queue is full"<<endl;
	}
	else if(front==-1){
		front=0;
	}
	back=back+1;
	queue[back]=x;
	cout<<x<<" ";
}
int deqeue(){
	int element;
	if(front==-1||front==back+1){
		cout<<"the queue is empty";
	}
	element=queue[front];
	front=front+1;

	return element;
}
