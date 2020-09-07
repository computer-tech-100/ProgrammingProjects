#include<fstream>
#include <iostream>
#include<string>
#include<cstdlib>
using namespace std;

int main(){

	ifstream input_file;
	ofstream output_file;
	string person_name;
	char text;

        //ask user to enter a name
	cout<<"Enter name of the person:";
	cin>>person_name;

        //open input file
	input_file.open("letter1.txt");

        //check if input file cannot be found
	if(input_file.fail()){
		cout<<"error in opening input file";
		exit(1);
	}
	
       //open output file
	output_file.open("letter2.txt");

        //check for errors in opening output file
	if(output_file.fail()){
			cout<<"error in opening output file";
			exit(1);
		}

        //read characters one by one from input file using get() function
	input_file.get(text);

        //use while loop to go through all of the characters in the text until end of the file
	while(!input_file.eof()){
          //use nested if statements to get #N# one by one and replace the name
	  input_file.get(text);
          if(text=='#'){
    	    input_file.get(text);
    	    if(text=='N'){
    	      input_file.get(text);
    	      if(text=='#'){
    		input_file.get(text);
    	        output_file<<person_name;
    	     }
    	 }
     }

           output_file<<text;
		
    }
        //close both files
	input_file.close();
	output_file.close();
	return 0;
}
