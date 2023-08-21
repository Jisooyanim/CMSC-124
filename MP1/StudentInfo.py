list = []
class Student:
    def __init__(self, studentName:str, studentAge:int, studentGPA:float, studentGradeLevel:str):
        self.__name = studentName
        self.__age = studentAge
        self.__gpa = studentGPA
        self.__gradelevel = studentGradeLevel 
    
    def enroll(self, name, age, gpa, gradeLevel):
        enrollee = Student(name, age, gpa, gradeLevel)
        list.append(enrollee)
    #Testing purposes
    #def display(self, enrollee):
    #    print("Name        : ", enrollee.__name)
    #    print("Age         : ", enrollee.__age)
    #    print("GPA         : ", enrollee.__gpa)
    #    print("Grade Level : ", enrollee.__gradelevel)
    #    print("\n") 

#s:Student = Student('', 0,0, '')
#s.enroll("Mark", 18, 1.5, "Freshie")
#s.enroll("Angel", 19, 1.0, "Sophomore")
#s.enroll("Charles", 20, 1.45, "Junior")

#for i in range(list.__len__()):
#    s.display(list[i])