#include<iostream>
using namespace std;
#include<string>
#include<cmath>
#include<vector>
#include<cmath>
#include<algorithm>

//----------------------------------------------------------Smiley Faces Counter----------------------------------------------------------------------
//This program returns the number of smiley faces :)
//These are the components that make up a valid smiley:
//A smiley has eyes. Eyes can be : or ;
//A smiley has a nose but it doesn't have to. A nose can be - or ~   Noses are optional i.e :) and :-) are both valid
//A smiley has a mouth which can be ) or D or ]
//An empty array should return 0.

//function that takes in an array and returns the number of smiley faces in it
int count_smiley_faces(string a[],int size_of_arr);

int main(){

    string c[7]={":)",";]", ":[", ";*", ":$",";-D",";~D"};
    
    count_smiley_faces(c,7); // --> 4 happy faces
    
}
int count_smiley_faces(string a[],int size_of_arr){
    
    vector<int>s; // the size of this vector will be incremented by 1 if we have a happy face
    
    for(int i=0;i<=size_of_arr;i++){
        
        std::string myStr = a[i]; // consider each item in array and store that item into myStr variable
        
        //check if each string is happyface
        if (myStr.find(":-)") != std::string::npos){
            s.push_back(1);
        }
        if (myStr.find(":-D") != std::string::npos){
            s.push_back(1);
        }
        if (myStr.find(":)") != std::string::npos){
            s.push_back(1);
        }
        if (myStr.find(":D") != std::string::npos){
            s.push_back(1);
        }
        if (myStr.find(":~D") != std::string::npos){
            s.push_back(1);
        }
        if (myStr.find(":~)") != std::string::npos){
            s.push_back(1);
        }
        if (myStr.find(";-)") != std::string::npos){
            s.push_back(1);
        }
        if (myStr.find(";-D") != std::string::npos){
            s.push_back(1);
        }
        if (myStr.find(";)") != std::string::npos){
            s.push_back(1);
        }
        if (myStr.find(";D") != std::string::npos){
            s.push_back(1);
        }
        if (myStr.find(";~D") != std::string::npos){
            s.push_back(1);
        }
        if (myStr.find(";~)") != std::string::npos){
            s.push_back(1);
        }
        if (myStr.find(":-]") != std::string::npos){
            s.push_back(1);
        }
        if (myStr.find(":]") != std::string::npos){
            s.push_back(1);
        }
        if (myStr.find(":~]") != std::string::npos){
            s.push_back(1);
        }
        if (myStr.find(";-]") != std::string::npos){
            s.push_back(1);
        }
        if (myStr.find(";]") != std::string::npos){
            s.push_back(1);
        }
    }

    cout<<"number of happy faces are: "<<s.size()<<endl;
    return s.size();
}
