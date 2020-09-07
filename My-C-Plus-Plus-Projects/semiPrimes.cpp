#include<iostream>
using namespace std;
#include<string>
#include<cmath>
#include<vector>
#include<cmath>
#include<algorithm>

//-----------------------------------------------------------------------Semi Primes-----------------------------------------------------------------
//The program takes in a number and returns "Squarefree Semiprime" or "Semiprime", or "Neither".
//A semiprime is the product of two primes. Apart from these two primes, its only other proper divisor is 1.
//The two prime factors of a semiprime can be the same number (the semiprime 49 is the product of 7x7).
//A semiprime that has two distinct prime factors is called a squarefree semiprime.

void semi_primes(int num);

int main(){
    
    semi_primes(25);// "Semiprime"
    
    semi_primes(33); // "Squarefree Semiprime"
    
    semi_primes(53); // "Neither"
    
    semi_primes(15); // "Squarefree Semiprime"
    
    semi_primes(97); // "Neither"
    
    semi_primes(49);// "Semiprime"
    
}

void semi_primes(int num){
    
    vector<int> prime; //this vector contains all prime numbers from 2 to 97
    vector<int> not_prime;
    vector<int>squarefree_semiprime;
    
    //we generate prime numbers and store them into a vector
    for (int number=2; number<=97; number++)
    {
        bool is_prime=true;
        for (int i=2; i*i<=number; i++)
        {
            if (number % i == 0) // if the number has any divisor other than 1 and itself then it is not a prime
            {
                is_prime=false;
                not_prime.push_back(number);
                break;
            }
        }
        if(is_prime) {
            prime.push_back(number);
        }
    }
    for(int i=0;i<prime.size();i++){
        
        //Squarefree Semiprime
        for(int j=0;j<prime.size();j++){
            if(prime[i]!=prime[j] && prime[i]*prime[j]==num){
                squarefree_semiprime.push_back(1);
            }
        }

        //semiPrime
        if(prime[i]==prime[i] && prime[i] *prime[i]==num){
            cout << "SemiPrime"<<endl;
        }
        
        //neither
        if( 1*prime[i]==num){
            cout<<"Neither"<<endl;
        }
    }
    
    //if squarefree_semiprime is not empty
    if(squarefree_semiprime.size()!=0){
        cout<<"Squarefree Semiprime"<<endl;
    }
}
