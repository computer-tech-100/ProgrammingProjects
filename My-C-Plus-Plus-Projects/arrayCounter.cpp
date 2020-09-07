#include<iostream>
using namespace std;
#include<string>
#include<cmath>
#include<vector>
#include<cmath>
#include<algorithm>
#include <regex>
#include<bitset>

//--------------------------------------------------------------------------Array Counter-----------------------------------------------------------------
//This program returns the number of days between the first and second date.
//for example 10 Dec 2019, 10 Jan 2020 --> 30 days in between

int days_in_between(string date1,string date2);

int main(){
    
    days_in_between("2010/11/10", "2012/10/30");
    
}

int days_in_between(string date1,string date2){
    
    cout<<"The two dates are:"<<endl;
    //validate date1
    sregex_iterator end;
    
    //use regex to vailidate date
    regex myFormat("\\w{4}[/]\\w{2}[/]\\w{2}");// 4 digits for year, 2 digits for month, 2 digits for day
    sregex_iterator d(date1.begin(),date1.end(), myFormat);
      
    while(d!= end){
        smatch validate = *d;
        cout << validate.str();
        d++;
    }
    
    cout<<"\n";
    
    //validate date2
    sregex_iterator end2;
    
    // use regex to vailidate date
    regex myFormat2("\\w{4}[/]\\w{2}[/]\\w{2}");// 4 digits for year,2 digits for month, 2 digits for day
    sregex_iterator d2(date2.begin(),date2.end(), myFormat2);
    
    while(d2!= end2){
        smatch validate2 = *d2;
        cout << validate2.str();
        d2++;
    }
    cout<<"\n";
    
    //get year
    string  year1 = date1.substr(0, 4);
    
    string year2 = date2.substr(0, 4);
    
    //get month
    string  month1 = date1.substr(5, 2);
    
    string month2 = date2.substr(5, 2);
    
    //get day
    string  day1 = date1.substr(8, 2);
    
    string day2 = date2.substr(8, 2);
    
    int y1=stoi(year1);
    int y2=stoi(year2);
    int year_difference=abs(y1-y2);
    
    int m1=stoi( month1 );
    int m2=stoi(month2);
    
    int month_difference=abs(m1-m2);
    
    int d1=stoi(day1);
    int dd2=stoi(day2);
    int day_difference=abs(d1-dd2);
    int y=year_difference*365;//1 year = 365 days
    int m=month_difference*30;
    int total=y+m+day_difference;
    
    cout<<"The number of the days between first and second date is:"<<total<<endl;
    
    return total;
}
