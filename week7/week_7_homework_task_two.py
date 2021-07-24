"""

TASK 2

Write a base class to represent a student. Below is a starter code.
Feel free to add any more new features to your class.
As a minimum a student has a name and age and a unique ID.

Create a new child class from student to represent a concrete student doing a specialisation, for example:
Software Student and Data Science student.

#     create new methods that manage student's subjects (add/remove new subject and its grade to the dict)
#     create a method to view all subjects taken by a student
#     create a method  (and a new variable) to get student's overall mark (use average)

"""


class Student:

    def __init__(self):
        self.students = []
        self.subjects = []

    def add_student(self):
        self.name = input("Please enter your name: ")
        self.age = input("Please enter your age: ")
        self.id = input("Please enter your student ID number: ")

        self.students.append({'name': self.name, 'age': self.age, 'id': self.id})
        print(f"The student's name is {self.name}, they are {self.age} years old and their id is {self.id}.")


class CFGStudent(Student):

    def add_subjects(self):
        number_of_subjects_input = int(input(
            "Please enter how many subjects and grades would you would like to add?: "))
        for subject in range(number_of_subjects_input):
            user_input = input("Please enter the student id, subject and grade separated by a colon: ")
            split = user_input.split(':')
            self.subjects.append({'id': split[0], 'subject': split[1], 'grade': split[2]})
        print(self.subjects)

    def remove_subject(self, subject_name):
        for subject in self.subjects:
            if subject_name == subject['subject']:
                self.subjects.remove(subject)
                print(f"The {subject_name} subject has been removed from the student's list")
                print(f"The remaining subjects are {self.subjects}")
                break

    def check_subjects(self, id):
        print(f"These are all the subjects for student id {id}: {', '.join([item['subject'] for item in self.subjects])}")


    def overall_grade(self, id):
        grades = [int(grade['grade']) for grade in self.subjects]
        number_of_grades = len(grades)
        total_of_grades = sum(grades)
        average = total_of_grades / number_of_grades
        print(f"The mean of student {id}'s grades is {average}")


student2 = CFGStudent()
student2.add_student()
student2.add_subjects()
student2.overall_grade(1234)
student2.check_subjects(1234)
student2.remove_subject('Software')

# # # example usage # # #
"""
Geraldine
21
1234
3
1234:Software:75
1234:Data:50
1234:Theory:83

Output:

The student's name is Geraldine, they are 21 years old and their id is 1234.

[
  {'id': '1234', 'subject': 'Software', 'grade': '75'}, 
  {'id': '1234', 'subject': 'Data', 'grade': '50'}, 
  {'id': '1234', 'subject': 'Theory', 'grade': '83'}
]

The mean of student 1234's grades is 69.33333333333333

These are all the subjects for student id 1234: Software, Software, Software

The Software subject has been removed from the student's list

The remaining subjects are 
[
  {'id': '1234', 'subject': 'Data', 'grade': '50'}, 
  {'id': '1234', 'subject': 'Theory', 'grade': '83'}
]
"""



