from unittest.mock import patch
import pytest

"""
Answers for the coding questions of the second assessment for the code first girls nanodegree, summer 2021
"""

# # # Question 1.

# What is the program?
""" A program is a set of instructions written by a person in a programming language that can be executed by a computer
to perform a task that is specified in the code """

# What is the process?
""" This is the set of instructions currently being executed by a computer processor """

# What is Cache?
""" This is part of the CPU. It is a small amount of memory that temporarily stores instructions and data that will be
reused by the CPU """

# What is Thread and Multithreading?
""" A thread is part of a process. Multiple threads can exist within one process that can execute at the same time. They
share resources like memory. A thread is the smallest sequence of programmed instructions that can be managed by a 
scheduler """

# What is GIL in Python and how does it work?
""" GIL = Global interpreter lock. It is there to prevent multithreading from happening in memory concurrently and it 
stops race conditions """

# What is Concurrency and Parallelism and what are the differences?
""" Parallelism is where tasks run at the same time. Concurrency is where 2 or more tasks might not be running at the 
same time but they can start, run and complete in overlapping periods of time """

# What do these stand for in programming: DRY, KISS, BDUF
"""DRY: Don't repeat yourself, KISS: Keep is simple stupid, BDUF: Big design up front"""

# What is Garbage collector? How does it work?
"""The garbage collector removes dead objects from the memory when their reference counter = 0
e.g. 
x1 = blah (reference counter for blah object 1 = 1)
x2 = x1 (reference counter for blah object 1 = 2)
x1 = None (reference counter for blah object 1 = 1)
x2 = blah (creates a new blah object, blah object 2, and the first blah object reference counter = 0)
The garbage collector would then remove this dead object from the memory """

# What are ‘deadlock’ and ‘livelock’ in a relational database?
""" Deadlock is where 2+ transactions are waiting for each other to give up locks on the database
e.g. if a transaction locks rows in one table and needs to update rows in another table to finish that update, but a 
different transaction has a lock on those rows and IT needs to update rows that the first transaction has a lock on to 
finish its task then neither task can finish and there is a 'deadlock'.

A livelock is where the transactions requests for locks are denied because the requests overlap with each other. To try
and fix it the transactions adapt their requests, but the new requests also overlap - this is continous and is called a
'livelock'.
"""

# What is Flask and what can we use it for?
""" Flask is a 3rd party library that can be installed and used for developing web applications"""

# # # Question 2. Discuss the difference between Python 2 and Python 3
""" Python 2 was a previous version/release of python that was sunset. This was meant to happen in around 2015 but 
people continued to use it and so it didn't happen until 2020.
There were some changes to functions and syntax between python 2 and python 3 such as in python 2 print was statement 
whereas in python 3 print is a function. There was also problems with integer division e.g. 3/2 = 1, decimals would have
to be included to get the correct answer of 1.5 -> 3.0/2.0 = 1.5.
 """

# # # Question 3. Write a function that can define whether a word is a Palindrome or not  (a word, phrase, or sequence
# # # that reads the same backwards as forwards, e.g. madam)

def define_palindrome():
    reversed_palindrome = palindrome[::-1]
    is_palindrome = False
    if (palindrome == reversed_palindrome):
        is_palindrome = True
    return is_palindrome


palindrome = input("Enter the word to test for a palindrome: ")
is_palindrome = define_palindrome()
if is_palindrome:
    print("It is a palindrome!")
else:
    print("Sorry! That is not a palindrome!")

# # # Re-written for testing # # #

def define_palindrome():
    try:
        palindrome = input("Enter the word to test for a palindrome: ").isalpha()
        reversed_palindrome = palindrome[::-1]
        is_palindrome = False
        if (palindrome == reversed_palindrome):
            is_palindrome = True
        return is_palindrome
    except TypeError:
        raise Exception("Sorry! You have entered something that isn't a word!")

is_palindrome = define_palindrome()
if is_palindrome:
    print("It is a palindrome!")
else:
    print("Sorry! That is not a palindrome!")

# # # Question 4. Write tests for the newly created Palindrome function. Provide a brief explanation for your test
# # # case options.

"""This doesn't work but I can't fix it - too tired =) """
@patch('builtins.input', lambda *args: 5)
def test_define_palindrome_non_alpha_input():
    with pytest.raises(Exception) as exception_info:
        define_palindrome()
    assert "isn't a word!" in str(exception_info.value)


# # # Question 5. Agile methodology, Scrum: name at least 3 types of meetings that are exercised by Agile teams and
# # # describe the objective of each meeting.
""" 
A daily scrum: this is a meeting for the development team often held at the same time daily it is for discussing
what has been worked on for the past 24 hours and what will be worked on for the next 24 hours

Sprint retrospective: this looks at the last sprint and looks at things that went well and things that need improving

Sprint planning: this is for planning what work needs doing and how it will be completed, it is to get the development
team and product owner on the same page. A sprint goal is created by the scrum team and the development team picks items
from the backlog to achieve the goal. """


# # # Question 6. Exception handling in Python, explain what each of the following blocks means in the program flow:
""" 
Try: This is the code that is executed - literally try and execute this code - if it is fine carry on

Except: If the code fails to run, this part of the code is there to catch whatever is wrong with it - a specific type
of exception can and should be specified e.g. except TypeError will catch if a wrong type is entered for input e.g. a
character instead of a number.

Else: This part of the code is executed if there is no exception raised

Finally: This part of the code is always executed
"""

# # # Question 7. How can we connect a Python program (process) with a database? Explain how it works and how do we
# # # fetch / insert data into DB tables from a python program.
""" To connect a database and a python program a module called mql connector would be installed into python. A config 
file is created with the database information in it and then a main file is created with functions to complete certain
methods like GET which gets information from the database, POST which sends data to the database, PUT updates data on the 
server and replaces what was there and DELETE which deletes information

e.g.
@app.route('/fruitbowl')
def get_fruit():
    return jsonify(fruit)
    
In this example it is querying the address <address>/fruitbowl and returning a list in the json format of fruits in the
fruitbowl"""


# # # Question 8. Given two SQL tables below: authors and books.
# # # The authors dataset has 1M+ rows
# # # The books dataset also has 1M+ rows
# # # Create an SQL query that shows the TOP 3 authors who sold the most books in total!

""" to do: 
- join the tables together based on some shared value
- sort sold values descending(highest at the top), select top 3
- must be booked sold column in books or authors

SELECT TOP 3 
    FROM authors a
        JOIN books b
            ON a.book_name=b.book_name
                ORDER BY sold_copies DESC
"""


# # # Question 9.
"""
- Write a function that accepts an array of number and an integer representing a target sum. 
- If any two numbers from the accepted numbers sum up to the target sum then the function should return them in array, 
in any order. 
- If no numbers sum to the target sum, the function should return an empty array. 
- The target has to be achieved using different numbers from the array.
"""

def two_number_sum(numbers, target):
    summed_numbers = []
    for number in numbers:
        complementary_number = target - number
        if complementary_number in summed_numbers:
            return [number, complementary_number]
        summed_numbers.append(number)
    return []

numbers = [3, 5, -4, 8, 11, 1, -1]
target = 10

result = two_number_sum(numbers, target)
print(result)



