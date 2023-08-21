#include <iostream>
using namespace std;

int main(){
    float f, c;

    cout << "Enter temperature in Fahrenheit:";
    cin >> f;

    c = ((f - 32) * 5)/9;
    cout << "Celsius: " << setprecision(2) << c << endl;

    return 0;
}