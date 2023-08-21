import java.util.Scanner;

public class StudentInfo{
    private String name;
    private int age;
    private float gpa;
    private String grade;

    public StudentInfo(String name, int age, float gpa, String grade){
        this.name = name;
        this.age = age;
        this.gpa = gpa;
        this.grade = grade;
    }

    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.print("Enter number of students:");
        int n = input.nextInt();
        StudentInfo[] s = new StudentInfo[n];

        for(int i = 0; i < n; i++){
            System.out.print("Enter name:");
            String name = input.nextLine();
            System.out.print("Enter age:");
            int age = input.nextInt();
            System.out.print("Enter gpa:");
            float gpa = input.nextFloat();
            System.out.print("Enter grade level:");
            String grade = input.nextLine();
            s[i] = new StudentInfo(name, age, gpa, grade); 
        }
        /* 
        for(int i = 0; i < n; i++){
            System.out.printf("Name:%s", s[i].name);
            System.out.printf("Age:%d", s[i].age);
            System.out.printf("GPA:%f", s[i].gpa);
            System.out.printf("Grade level:%s", s[i].grade);
        }*/

        input.close();
    }
}