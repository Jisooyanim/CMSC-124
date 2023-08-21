#include <iostream>
using namespace std;

int main(){
    int num = 1;

    //A pointer variable that stores the address of num
    int *ptr = &num;

    //Prints the value of *ptr
    cout << "The value of num is " << *ptr << endl;
    //Prints the memory addresses of num and ptr
    cout << "Memory address of num = " << &num << endl << "Memory address of ptr = " << ptr << "\n\n"; 

    //Changing the value of ptr
    *ptr = 2;

    //Prints the new value of *ptr
    cout << "The new value of ptr is " << *ptr << endl;
    //Prints the new value of num
    cout << "The new value of num is " << num << endl;

    return 0;
}