#include <iostream>
#include <iomanip> 
using namespace std;


class Student{
    private:
        char name[50];
        int age;
        float gpa;
        char grade[10];
    public:
        void enroll(){
            cout << "Enter name: ";
            cin >> name;
            cout << "Enter age: ";
            cin >> age;
            cout << "Enter gpa: ";
            cin >> gpa;
            cout << "Enter grade: ";
            cin >> grade;
        }
        /*void display(){
            cout << "Name: " << name << endl;
            cout << "Age: " << age << endl;
            cout << "GPA: " << setprecision(2) << gpa << endl;
            cout << "Grade: " << grade << endl;
        }*/
};

int main(){
    int n;
    Student s[50];

    cout << "Enter number of students: ";
    cin >> n;

    for(int i = 0; i < n; i++){
        s[i].enroll();
    }
    /* 
    for(int i = 0; i < n; i++){
        s[i].display();
    }
    */
    return 0;
}