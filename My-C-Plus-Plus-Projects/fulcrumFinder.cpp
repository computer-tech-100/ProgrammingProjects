#include<iostream>
using namespace std;
#include<string>
#include<cmath>
#include<vector>
#include<cmath>
#include<algorithm>

//----------------------------------------------------------------Fulcrum Finder----------------------------------------------------------------------
//This program finds fulcrum of an array
//A fulcrum of an array is an integer such that all elements to its left and all elements to its right will be sum to the same value. for example : [1,2,-1,4,1,1] --> 4 will be Fulcrum because 1+2+(-1)=2 which is equal to 1+1 so the program returns 4

int fulcrum_finder();

int main(){
    
    fulcrum_finder();//call the function
    return 0;
    
}
int fulcrum_finder(){
    
    int s;
    int user_num;
    vector<int>v;
    
    vector< pair <int,int> > left;// vector of pairs to keep element with it's left sum
    vector< pair <int,int> > right;// vector of pairs to keep element with it's right sum
   
    cout<<"Welcome to Fulcrum Finder application:"<<endl;
    cout<<"Enter the size of your array:";
    cin>>s;
    for(int i=0;i<s;i++){
        cout<<"enter number:";
        cin>>user_num;
        v.push_back(user_num);//store all the user's numbers into a vector
        
    }
    cout<<"Here is your array with size "<<v.size()<<" :"<<endl;
    for(int i=0;i<s;i++){
        cout<<v[i]<<endl;
        
    }
    int sumAll=0;
    for(int i=0;i<v.size();i++){
        sumAll+=v[i];
    }
    cout<<"Sum of all numbers is: "<<sumAll<<endl;
    
    //left
    int sum_left=0; //initialize sum left to 0
    
    for(int i=0;i<v.size();i++){
        
        sum_left+=v[i-1];// for each number add up left elements of that number -->  sum_left = sum_left + v[i-1]
        
        cout<<"Sum of the numbers that are on left hand side of "<<v[i]<<" is "<<sum_left<<endl;
        left.push_back( make_pair(v[i],sum_left) );
    }
    
    cout<<endl;
    
    //right
    int sum_right=sumAll; //initialize sum_right to sum of all numbers
    
    for(int i=0;i<v.size();i++){
        
        sum_right-=v[i];// for each number add up right elements of that number -->  sum_right = sum_right - v[i]
        
        cout<<"Sum of the numbers that are on right hand side of "<<v[i]<<" is "<<sum_right<<endl;
        
        right.push_back(make_pair(v[i],sum_right) );
    }
    
    cout<<endl;
    cout<<"Vector of pairs containg the element with it's left sum:"<<endl;
    cout<<"element  left sum"<<endl;
    for(int i=0;i<left.size();i++){
        cout<<left[i].first<<"            "<< left[i].second<<endl;
    }
    cout<<endl;
    cout<<"Vector of pairs containg the element with it's right sum:"<<endl;
    cout<<"element  right sum"<<endl;
    for(int i=0;i<right.size();i++){
        
        cout<<right[i].first<<"           "<< right[i].second<<endl;
    }
    
    //check if Fulcrum exists (when sum of left = sum of right)
    for(int i=0;i<right.size();i++){
        if(left[i].first==right[i].first && left[i].second==right[i].second){
            cout<<"Fulcrum is:"<<left[i].first<<endl;
            return left[i].first; // return the Fulcrum
        }    
    }
    
    return 0;
}
