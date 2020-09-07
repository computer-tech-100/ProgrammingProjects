#include <iostream>
#include<string>
using namespace std;

//declare functions
double length(double& value1,string& from1,string& to1);
//converts length from one to another unit
double weight(double value2,string from2,string to2);
//converts weight from one unit to another unit
double volume(double value3,string from3,string to3);
//converts volume from one to another unit

int main(){
	double value1,value2,value3;
	string from1,to1,one,from2,to2,from3,to3;
        //ask user to choose from menu
	cout<<"enter 1 for lengh,2 for weight, 3 for volume:";
	cin>>one;
        //access lenght menu
	if(one=="1"){
	cout<<"This is lenght menu,enter a number:";
	cin>>value1;
	cout<<" which unit(cm,inch,feet,meter,mile,km) do you want to convert from:";
	cin>>from1;
	cout<<"which unit(cm,inch,feet,meter,mile,km) do you want to convert to:";
	cin>>to1;
        //call the function
	length(value1,from1,to1);
	}
      //access weight menu
      else if(one=="2"){
	    	 cout<<"this is weight menu,enter a number:";
	    	 cin>>value2;
	    	 cout<<" which unit(ton,kg,gram,milligram,pound) do you want to convert from:";
	    	 cin>>from2;
	    	 cout<<"which unit(ton,kg,gram,milligram,pound) do you want to convert to:";
	    	 cin>>to2;
      //call the function
	 weight(value2,from2,to2);
      }

      //access volume menu
      else if(one=="3"){
    	  cout<<"this is volume menu,enter a number:";
    	  cin>>value3;
		  cout<<" which unit(liter,gallon,milliliter,cubic centimeter,cubic meter) do you want to convert from:";
		  cin>>from3;
		  cout<<"which unit(liter,gallon,milliliter,cubic centimeter,cubic meter) do you want to convert to:";
		  cin>>to3;
        //call the function
	volume(value3,from3,to3);
      }
       return 0;
}
//function definition for lenght
double length(double& value1,string& from1,string& to1)
{
    if(from1=="cm" && to1=="inch"){
    	 cout<<"the conversion from cm to inch is equal to:"<<value1*0.39;
     return value1*0.39;
     }
        else if(from1=="inch" && to1=="cm"){
    	  cout<<"the conversion from inch to cm is equal to:"<<value1*2.54;
    	  return value1*2.54;
        }
        else if(from1=="meter" && to1=="feet"){
        	cout<<"the conversion from meter to feet is equal to:"<<value1*3.28;
        	return value1*3.28;
        }
        else if(from1=="feet" && to1=="meter"){
        	cout<<"the conversion from feet to meter is equal to:"<<value1*0.304;
        	return value1*0.304;
        }
        else if(from1=="mile" && to1=="km"){
        	cout<<"the conversion from mile to km is equal to:"<<value1*1.61;
        	return value1*1.61;
        }
        else if(from1=="km"&& to1=="mile")
        	cout<<"the conversion from km to mile is equal to:"<<value1*0.621;
        	return value1*0.621;
}
//function definition for weight
double weight(double value2,string from2,string to2)
{
	  if(from2=="ton" && to2=="kg"){
	    	 cout<<"the conversion from ton to kg is equal to:"<<value2*1000;
	     return value2*1000;
	     }
	        else if(from2=="kg" && to2=="ton"){
	    	  cout<<"the conversion from kg to ton is equal to:"<<value2*0.001;
	    	  return value2*0.001;
	        }
	        else if(from2=="gram" && to2=="milligram"){
	        	cout<<"the conversion from gram to milligram is equal to:"<<value2*1000;
	        	return value2*1000;
	        }
	        else if(from2=="milligram" && to2=="gram"){
	        	cout<<"the conversion from milligram to gram is equal to:"<<value2*0.001;
	        	return value2*0.001;
	        }
	        else if(from2=="pound" && to2=="kg"){
	        	cout<<"the conversion from pound to kg is equal to:"<<value2*0.45;
	        	return value2*0.45;
	        }
	        else if(from2=="kg"&& to2=="pound")
	        	cout<<"the conversion from kg to pound is equal to:"<<value2*2.20;
	        	return value2*2.20;
}
//function definition for volume
double volume(double value3,string from3,string to3)
{
	  if(from3=="liter" && to3=="gallon"){
	    	 cout<<"the conversion from liter to gallon is equal to:"<<value3*0.26;
	     return value3*0.26;
	     }
	        else if(from3=="gallon" && to3=="liter"){
	    	  cout<<"the conversion from gallon to liter is equal to:"<<value3*3.78;
	    	  return value3*3.78;
	        }
	        else if(from3=="cubic centimeter" && to3=="cubic meter"){
	        	cout<<"the conversion from cubic centimeter to cubic meter is equal to:"<<value3*0.000001;
	        	return value3*0.000001;
	        }
	        else if(from3=="cubic meter" && to3=="cubic centimeter"){
	        	cout<<"the conversion from cubic meter to cubic centimeter is equal to:"<<value3*1000000;
	        	return value3*1000000;
	        }
	        else if(from3=="liter" && to3=="milliliter"){
	        	cout<<"the conversion from liter to milliliter is equal to:"<<value3*1000;
	        	return value3*1000;
	        }
	        else if(from3=="milliliter"&& to3=="liter")
	        	cout<<"the conversion from milliliter to liter is equal to:"<<value3*0.001;
	        	return value3*0.001;
}
