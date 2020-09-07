#include <iostream>
using namespace std;

class rational {
private:
	int numerator, denominator;

public:
	//constructor
	rational(int x, int y);
	rational(int x);
	rational();

	//calculations
	friend rational operator+(rational& x,rational& y);//overloading
	friend rational operator-(rational& x,rational& y);//overloading

	rational multiplication(rational x);
	rational division(rational x);
	bool less(rational x);
	void output();

	//getters and setters
	int getNumerator();
	int getDenominator();
	void setNumerator(int x);
	void setDenominator(int x);
};
//In the main function define objects of the class
int main() {
	rational numberOne = rational(2,3);
	rational numberTwo = rational(4,7);

	rational object3;
	rational object4;
	object3=numberOne+numberTwo;//overloading
	object4=numberOne-numberTwo;//overloading

	rational numberFive = numberOne.multiplication(numberTwo);
	rational numberSix = numberOne.division(numberTwo);
	numberTwo.setNumerator(2);

	object3.output();//overloading
	object4.output();//overloading

	numberFive.getDenominator();
	//numberThree.output();
	//numberFour.output();
	numberFive.output();
	numberSix.output();
	cout << numberOne.less(numberTwo)<<endl;

	return 0;
}
//this is a/b + c/d = (a*d +b*c)/b*d
//overloading
rational operator+(rational& x,rational& y) {
	rational d1,d2;
	d1.numerator=(x.numerator*y.denominator)+(x.denominator*y.numerator);
	d2.denominator=x.denominator*y.denominator;
	return rational(d1.numerator,d2.denominator);
}
//this is a/b - c/d = (a*d - b*c)/b*d
//overloading
rational operator-(rational& x,rational& y){
	rational d3,d4;
	d3.numerator=(x.numerator*y.denominator)-(x.denominator*y.numerator);
	d4.denominator=x.denominator*y.denominator;
		return rational(d3.numerator,d4.denominator);
}
//this is a/b * c/d =(a*c)/(b*d)
rational rational::multiplication(rational num3) {
	int n3 = numerator*num3.getNumerator();//this is a*c
	int d3 = denominator*num3.getDenominator();//this is b*d
	return rational(n3, d3);
}
//this is (a/b) / (c/d) = (a*d)/(c*b)
rational rational::division(rational num4) {
	int n4 = numerator*num4.getDenominator();//this is a*d
	int d4 = denominator*num4.getNumerator();//this is b*c
	return rational(n4, d4);
}
//this is (a/b)<(c/d) means (a*d)<(c*b)
bool rational::less(rational less1) {
	int v = numerator * less1.getDenominator();//this is a*d
	int w = denominator*less1.getNumerator();//this is c*d
	return v< w;
}

void rational::setNumerator(int x) {
	numerator = x;
}

void  rational::setDenominator(int x) {
	denominator = x;	
}

int rational::getNumerator() {
	return numerator;
}

int rational::getDenominator() {
	return denominator;
}

rational::rational(int x, int y) {

	numerator = x;
	denominator = y;	
}

rational::rational(int x) {

	numerator=x;	
}

rational::rational() {
	return;	
}

void rational::output() {
	cout << numerator << "/" << denominator << endl;
}
