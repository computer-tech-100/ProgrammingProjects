#include <iostream>
using namespace std;

struct node{
	int data;
	node*next;
};
// in queue you need 2 pointers
node*front=NULL;
node*rear=NULL;

bool isEmpty();
void enqueue(int value);
void dequeue();
void showFront();
void display();

int main() {
	enqueue(6);
	enqueue(7);
	enqueue(8);
	enqueue(9);
	enqueue(10);
	enqueue(11);
	display();
	dequeue();
	dequeue();
	cout<<"we dequeue the two number in the front i.e 6 and 7"<<endl;
	display();
	cout<<endl;
	cout<<"the number in the front is";
	showFront();

	return 0;
}
bool isEmpty(){
	if(front==NULL && rear==NULL){
		return true;
	}
	else{
		return false;
	}
}
void enqueue(int value){

	node*firstNode=new node;
	firstNode->data=value;
	firstNode->next=NULL;
	if(front==NULL){
		front=firstNode;
		rear=firstNode;
	}
	else{
		rear->next=firstNode;
		rear=firstNode;
	}
}
void dequeue(){
	if(isEmpty()){
		cout<<"the queue is empty you cannot dequeue";

	}
	else if(front==rear){
		free(front);
		front=rear=NULL;
	}
	else{
	node*removingNode=new node;
	removingNode=front;
	front=front->next;
	free(removingNode);

	}
}
void showFront(){
	if(isEmpty()){
		cout<<"queue is empty nothing to show";
	}
	else{
		cout<<front->data;
	}
}
void display(){
	node* printing=new node;
	printing=front;
	while(printing !=NULL){
		cout<<printing->data<<" ";
		printing=printing->next;
	}
}
