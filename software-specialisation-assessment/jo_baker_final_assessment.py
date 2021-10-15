"""
TASK 1.

Please see example solution below.
Students are more than welcome to come up with alternative solutions,
as long as their code works as expected.
"""

"""
Design a parent class called CFGStudent. It should have general attributes like name, surname, age, email, student id 
and methods to fetch student’s full name and student’s id.
Important: there should be an option to pass student id when a new class object is generated, HOWEVER, if no id is 
passed, then student_id should be automatically generated and assigned to the class.Design a child class called 
NanoStudent, which inherits from CFGStudent class. This class
should have exactly the same attributes as its parent class, as well as additional two called ‘specialization’ and 
‘course grades’.
The child class ‘generate_id’ method should override its parent method to add the suffix ‘NANO’ in front of the id.
New methods ‘add_new_grade’ and ‘get_course_grades’ should be added. Please see the skeleton structure in the 
final_assessment.py file. You can use it as a skeleton code for your classes OR adjust it and create your own.
SEE ADDITIONAL COMMENTS in the file.
"""
import random

class CFGStudent:

    def __init__(self, name, surname, age, email):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        self.student_id = self.generate_id()

    def generate_id(self):
        self.student_id = str(random.randint(1000, 10000))
        return self.student_id

    def get_id(self):
        return self.student_id

    def get_fullname(self):
        return self.name + self.surname


class NanoStudent(CFGStudent):

    def __init__(self, specialisation, **kwargs):
        super().__init__(**kwargs)
        self.student_id = None
        self.specialisation = None
        self.course_grades = None

    def generate_id(self):
        self.student_id = "NANO" + str(random.randint(1000, 10000))
        return self.student_id

    def add_new_grade(self, module, grade=0):
        self.course_grades = {}
        self.course_grades = {module: grade}  # this only seems to work for one of the grades - need some sort of append

    def get_course_grades(self):
        return self.course_grades

############################################

# Example run

s = CFGStudent('Anna', 'Smith', 18, 'anna@mail.com')  # do not pass ID, it should be generated automatically
print(s.get_fullname())
# returns 'Anna Smith'
print(s.student_id)
# returns '3868' or some other random number

cfg_s = NanoStudent('Software', name='Mia', surname='Papandopulu', age=20, email='mia@mail.com')
print(cfg_s.get_fullname())
# returns 'Mia Papandopulu'
print(cfg_s.get_id())
# returns 'NANO6180' or some other random number

cfg_s.add_new_grade('theory', 95)
cfg_s.add_new_grade('project', 78)
print(cfg_s.get_course_grades())
# returns {'theory': 95, 'project': 78}


"""
TASK 2

Given an index limit, find all corresponding Fibonacci values up to that limit in a sequence
and return the sum of all even Fibonacci numbers. See more details in the task description in
your assessment paper.
"""


##### TESTS ####


def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)


def even_fibonacci_sum(limit):
    index = [i for i in range(limit)]
    print(index)

    # need to add the index and the fib function to this to return the correct sum
    # for n in index if:
    even = list(filter(lambda x: x % 2 == 0, index))  # this returns the even numbers
    print(even)
    return sum(even)


# # # the first 2 don't work
print(even_fibonacci_sum(limit=10))  # should be 44
print(even_fibonacci_sum(limit=15))  # should be 188
print(even_fibonacci_sum(limit=1))   # should be 0


"""
TASK 3

Validate subsequence. Use suggested tests below to check
correctness of your solution.
"""

#### TESTS ####


def is_valid_subsequence(array, sequence):
    array_index = 0
    sequence_index = 0
    while array_index < len(array) and sequence_index < len(sequence):
        if array[array_index] == sequence[sequence_index]:
            sequence_index += 1
        array_index += 1
    return sequence_index == len(sequence)

array1 = [5,1,22,25,6,-1,8,10]
sequence1 = [1,6,-1,-2]
print(is_valid_subsequence(array1, sequence1))  # FALSE


array2 = [5,1,22,25,6,-1,8,10]
sequence2 = [1,6,-1, 10]
print(is_valid_subsequence(array2, sequence2))  # TRUE


array3 = [5,1,22,25,6,-1,8,10]
sequence3 = [25]
print(is_valid_subsequence(array3, sequence3))  # TRUE


"""
TASK 4

WRITTEN ASSIGNMENT

Write a review on how 'class Employee' can be improved.
(See PDF document with the code example)
"""
# # # Did not have time to do this - too tired after 24 hours of working on the project this weekend! :(


"""
Reviewing this class based on the SOLID principles:

S: This employee class violates the single responsibility principle because it has multiple responsbilities.
It creates the employee, updates, removes, saves and prints. A class should only have one responsiblity and if it has 
more, then these should be refactored into multiple classes or subclasses.

O: 

L:

I: Not all of the subclasses created from this class may need all the methods in it, this can lead to a lot of 
unused and unneeded interfaces and can result in bugs if they are called.

D:


"""








