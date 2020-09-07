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
	rational addition(rational x);
	rational subtraction(rational x);
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
	rational numberOne = rational(2, 3);
	rational numberTwo = rational(4, 7);
	rational numberThree = numberOne.addition(numberTwo);
	rational numberFour = numberOne.subtraction(numberTwo);
	rational numberFive = numberOne.multiplication(numberTwo);
	rational numberSix = numberOne.division(numberTwo);

	numberTwo.setNumerator(2);
	numberThree.setDenominator(3);
	numberFour.getNumerator();
	numberFive.getDenominator();
	numberThree.output();
	numberFour.output();
	numberFive.output();
	numberSix.output();
	cout << numberOne.less(numberTwo)<<endl;

	return 0;
}
//this is a/b + c/d = (a*d +b*c)/b*d
rational rational::addition(rational num1) {
	int n1 = numerator*num1.getDenominator() + denominator*num1.getNumerator();//this is (a*d+b*c)
	int d1 = denominator*num1.getDenominator();//this is b*d
	return rational(n1, d1);
}
//this is a/b - c/d = (a*d - b*c)/b*d
rational rational::subtraction(rational num2) {
	int n2 = numerator*num2.getDenominator() - denominator*num2.getNumerator();//this is (a*d-b*c)
	int d2 = denominator*num2.getDenominator();//this is b*d
	return rational(n2, d2);
}
//this is a/b * c/d =(a*c)/(b*d)
rational rational::multiplication(rational num3) {
	int n3 = numerator*num3.getNumerator(); //this is a*c
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
