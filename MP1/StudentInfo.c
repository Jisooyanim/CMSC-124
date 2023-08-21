#include <stdio.h>

struct Student{
    char name[50];
    int age;
    float gpa;
    char grade[10];
};
typedef struct Student Student;

void enroll(Student s[], int n);
void display(Student s[], int n);

int main(){
    int n;
    Student s[50];

    printf("Enter number of students: ");
    scanf("%i", &n);
    
    enroll(s, n);
    display(s, n);
    return 0;
}

void enroll(Student s[], int n){
    for (int i = 0; i < n; i++){
        printf("Enter name: ");
        scanf("%s", s[i].name);
        printf("Enter age: ");
        scanf("%d", &s[i].age);
        printf("Enter gpa: ");
        scanf("%f", &s[i].gpa);
        printf("Enter grade: ");
        scanf("%s", s[i].grade);
    }
}

void display(Student s[], int n){
    for (int i = 0; i < n; i++){
        printf("Name: %s\n", s[i].name);
        printf("Age: %d\n", s[i].age);
        printf("Gpa: %.2f\n", s[i].gpa);
        printf("Grade: %s\n",s[i].grade);
    }
}