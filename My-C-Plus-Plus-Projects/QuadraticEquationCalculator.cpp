#include<iostream>
using namespace std;
#include<string>
#include<cmath>
#include<vector>
#include<cmath>
#include<algorithm>

//--------------------------------------------------------------Quadratic Equation Calculator ----------------------------------------------------------
//Quadratic equation calculator is a program that solves quadratic equation ax^2+bx+c=0
//the user enters a,b and c
//If a=0 and b=0 then we have no root.
//If a=0 then we have one root, -c/b.
//If delta<0 then we have no root.
//If all above conditions are False, then we have two roots.
//if delta>0 then we have two different roots
//if delta=0 then we have two real identical roots
//if delta<0 then we have no real roots

int main(){
    int a,b,c;
    cout<<"Welcome to  Quadratic Equation Calculator! we have equation of the form ax^2+bx+c=0 and we want to find it's roots. "<<endl;
    cout<<"please enter a:";
    cin>>a;
    cout<<"please enter b:";
    cin>>b;
    cout<<"please enter c:";
    cin>>c;
    
    int delta=pow(b,2)-(4*a*c) ;
    int root1=((-b)+sqrt(delta))/2*a;
    int root2=((-b)-sqrt(delta))/2*a;
    int x=(-1*(c))/b;

    if(a==0 and b==0){

        cout<<"there is no root"<<endl;
    }
    else if (a==0){

        cout<<"we have only one root which is "<<x<<endl;
    }
    else if (delta<0){
        

        cout<<" no root since delta is less than 0"<<endl;
    }
    
    // if all above are false
    else{
        cout<<"We have two roots which are"<<root1<<" and "<<root2<<endl;
    }
        
    return 0;
}
