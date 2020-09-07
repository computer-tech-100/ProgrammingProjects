#include<iostream>
using namespace std;
#include<string>
#include<cmath>
#include<vector>
#include<cmath>
#include<algorithm>
#include <regex>
#include<bitset>

//--------------------------------------------------------------------------Next Largest Number---------------------------------------------------------
//The program returns the next largest number that can be created from the same digits as the input.

int nextLargestNumber(int x);

int main(){
    
    nextLargestNumber(19);// 91
    
    nextLargestNumber(3542);//4235
    
    nextLargestNumber(58943);//59348

}

int nextLargestNumber(int x)
{
    string my_string=to_string(x);//convert int to string
    vector<int>numbers;
    vector<int>larger;
    
    do {
        
        numbers.push_back(stoi(my_string));
    } while (next_permutation(my_string.begin(), my_string.end()));
    
    //those numbers that are greater than original number
    for(int i=0;i<numbers.size();i++){
        if(numbers[i]>x){
            larger.push_back(numbers[i]);
        }
    }
    
    //get the very first larger number
    int l=*min_element(larger.begin(), larger.end());
    cout<<l<<endl;

    return l;
}
