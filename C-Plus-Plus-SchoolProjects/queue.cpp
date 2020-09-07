#include <iostream>
using namespace std;
#include <queue>

int main() {
	queue <string> myqueue;
	myqueue.push("John");
	myqueue.push("James");
	myqueue.push("Anna");
	myqueue.push("Amy");
	myqueue.push("sharon");
	myqueue.push("Jerry");
	myqueue.push("Max");
	myqueue.push("Misha");
	cout<<"There are "<<myqueue.size()<<" people in the line at the bank"<<endl;
	cout<<"the first person is "<<myqueue.front()<<endl;
	cout<<"the last person is "<<myqueue.back()<<endl;
	myqueue.pop();
	cout<<"when first person goes to the counter to talk to the representatives, the number of remaining person are "<<myqueue.size()<<endl;
	cout<<"now the first person will become "<<myqueue.front()<<endl;
	return 0;
}
