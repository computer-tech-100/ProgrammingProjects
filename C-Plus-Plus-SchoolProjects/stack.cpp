#include <iostream>
#include<stack>
using namespace std;

int main() {
	stack <string> bunchOfFlowers;// make stack here
	//add flowers to our stack
	bunchOfFlowers.push("redRoses");
	bunchOfFlowers.push("yellowRoses");
	bunchOfFlowers.push("Iris flower");
	bunchOfFlowers.push("Narcissus flower");
	bunchOfFlowers.push("lilac flower");
	bunchOfFlowers.push("sun flower");
	
	//use size() function to see how many items you have in your stack
 	cout<<"there are "<<bunchOfFlowers.size()<<" flowers on our stack"<<endl;
	cout<<"the flower on the top is "<<bunchOfFlowers.top()<<endl;//use top() function to get the item which is at the top(the item that you add most recently)

	bunchOfFlowers.pop();//by using pop() method we actually remove item from stack

	cout<<"we remove the flower which was on the top,now the size of the stack is:"<< bunchOfFlowers.size()<<endl;
	cout<<"Now the flower which is on the top is "<<bunchOfFlowers.top()<<endl;

	return 0;
}
