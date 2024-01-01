#Create a dictionary of student names and their grades:
#Store student names as keys and their grades as values in a dictionary.
#Calculate the average grade of all students:
#Use sum() and len() functions to calculate the total and number of grades, respectively, and then divide the total by the number to get the average.
#Remove students with grades below 80 from the dictionary:
#Create a set of student names with grades below 80.
#Check if a specific student exists in the dictionary:
#Input a student name from the user.
#Use the in operator to check if the student name exists in the dictionary.
#Print a message indicating whether the student name is found or not.


#Student ={"name": "grades"}
number_of_student = int(input("Enter the number of student :"))
Student = {}
for student in range(number_of_student):
    student_name = input("Enter the student name :")
    student_grade = int(input("Enter their grades"))
    Student[student_name]=student_grade

print(Student)
Grade_of_student = sum(Student.values())/len(Student.values())
print(f"Grade of student is {Grade_of_student}")

new_student={}
for name,grade in Student.items():
    if grade>=80:
        new_student[name]=grade

print(new_student)



