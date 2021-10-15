**1. How does Object Oriented Programming differ from Process Oriented Programming?**

Procedual programming:
   - Uses a list of instructions to tell the computer what to do step by step
   - Relies on procedures (routines/sub-routines)
   - If something needs changing then every line of code that corresponds to the change must be edited

OOP:
   - All computations are carried out using objects
      - An object is a program component that knows how to perform certain actions as well as how to interact with other
   elements in the program
         - e.g. an object has an identity which makes it distinct, it has a state (various properties that may change)
   and it has behaviour (it can both do things and have things done to it)
   - Is easy to maintain and modify
      - objects can inherit from other objects and the children can be modified which cuts down on development time
   

- OOP uses methods, PP uses procedures
- OOP uses objects, PP uses records
- OOP uses classes, PP uses modules
- OOP uses messages, PP uses procudure calls

**2. What's polymorphism in OOP?**

<ins>Polymorphism:</ins> 

Methods that are able to take on many forms.
   
There are two types of polymorphism - Dynamic and Static
   
**Dynamic:** occurs during runtime of the program - this type of polymorphism describes when a method signature is 
in both a child class and a parent class - the methods have the same name but have different implementation
        
    e.g. class Car
            .drive(miles)
    
         class SportsCar
            .drive(miles)
                
The SportsCar implementation of .drive(miles) overrides the parent class Car implementation  

**Static:** occurs during compile-time rather than runtime - when multiple methods with the same name but different 
arguments are defined in the same class

- take a different number of parameters OR
- take different type of paramters OR
- take different order of paramters
            
   <br />**_this is method overloading_**
        
although the methods have the same name their signatures are different due to the different arguments.
        
    e.g. class Car
        .drive(int speed, string distance)
        .drive(int speed, int distance)
        .drive(string destination, int speed) 


**3. What's inheritance in OOP?**

<ins>Inheritance:</ins>

The principle that allows a class to derive from other classes
    
    e.g. class Weapon
        contains methods and attributes common to all weapons
        - Weapon.damage
        - Weapon.attack
        
Then make new classes of more specific weapons 

    e.g. class Sword and class Club
        - Sword: weapon.damageType = "sharp"
        - Club: weapon.damageType = "blunt"
    
The Weapon class is a parent class and the sword and club classes are child classes
    
Other child classes can be created from these child classes e.g. type of Sword (Bastard, Long etc.)
    
Access Modifiers:
- Public:
  Can be accessed from anywhere in the program
- Private:
  Can only be accessed from within the same class that the member is defined
- Protected:
  Can be accessed within the class it is defined as well as any children of that class 


**4. If you had to make a program that could vote for the top three funniest people in the office, 
how would you do that? How would you make it possible to vote on those people?**

I would create a class called Vote that has the following functions:
- __ init __
  - a dictionary that stores the scores for each candidate
- candidates():
  - asks for user input 3 times for names of people to vote for and assigns each name to the dictionary as a key
- votes():
   - asks for user input to vote for one of the 3 candidates in the dictionary
   - increments += 1 to the value of that candidate key
- final_tally():
   - prints out the results of the vote based on the key value pairs in the dictionary


**5. What's the software development cycle?**

The software development cycle (SDC) is the process a business uses to build software - it is the application of 
standard business practices. It is made up of :
- Planning
- Requirements
- Design
- Implementation
- Testing and Integration
- Deployment
- Maintenance

In planning a project leader will evaluate the things needed for the project such as labour and costs, a timetable with 
goals, creating teams and assigning leaders.

Requirements include what the application made in the project will do and the requirements the application needs to meet.

Design is used to say how the application will work and will include things like programming language, user interface, 
security and also which platforms the application will work on e.g. windows/linux etc.

Implementation is implementing the plan so far and actually writing the program.

Testing is testing the program to make sure it does what it is meant to and to check for bugs/security flaws.

In deployment, the product is made available to users.

The maintenance phase is for keeping the product working - if a bug is found by a user for e.g. a new SDC could be
started where a plan is made to test the bug, it is fixed, tested, deployed etc.

**6. What's the difference between agile and waterfall?**

Agile and waterfall are both SDC models.

The waterfall model is where the phases of the SDC are followed in a linear fashion and one phase must be completed
before moving on to the next.

Whereas with the agile model the SDC is broken into smaller iterations where 1 requirement will be worked on, designed, 
developed and tested and then presented to the client and the cycle repeats. Rather than creating a whole product and 
showing that and then having to change parts, each part is developed and shown in for e.g. a 2 week sprint.

**7. What is the reduce function used for?**

The reduce() function is equivalent to this two argument function:
                        
    def reduce(function, iterable, initialiser=None):
        it = iter(iterable)
        if initialiser is None:
            value = next(it)
        else:
            value = initialiser
        for element in it:
            value = function(value, element)
        return value

An example of how this would work passing in the function and the iterable would be this using this addition function
alongside a list of numbers:

    def my_add(a, b):
        result = a + b
        print(f"{a} + {b} = {result}")
        return result

    numbers = [0, 1, 2, 3, 4]

    reduce(my_add, numbers)

    output:
            0 + 1 = 1
            1 + 2 = 3
            3 + 3 = 6
            6 + 4 = 10

Using reduce on this function and list of numbers is the equivalent of the sum 
((((0 + 1) + 2) + 3) + 4) = 10

The optional initialiser can be used to set the initial value:
    
    e.g.
        reduce(my_add, numbers, 100)
        
        output:
                100 + 0 = 100
                100 + 1 = 101
                ...
                106 + 4 = 110


It is also possible to carry this out using a lambda function:

    e.g. 
        number = [1, 2, 3, 4]

        reduce(lambda a, b: a + b, numbers)

        output = 10


**8. How does merge sort work**

Merge sort is a sorting algorithm that works on the principle of 'divide and conquer'. It breaks down a list of 
(for e.g.) numbers into several sublists until the sublist is just a single element. The single element lists are 
then merged into a sorted list.

     e.g 
         unsorted list:  [14, 7, 3, 12, 9, 11, 6, 2]
              divide --> [14, 7, 3, 12] [9, 11, 6, 2]
              divide --> [14, 7] [3, 12] [9, 11] [6, 2]
              divide --> [14] [7] [3] [12] [9] [11] [6] [2]
            
                     The list is then merged and sorted
            
              merge --> [7, 14] [3, 12] [9, 11] [2, 6]
              merge --> [3, 7, 12, 14] [2, 6, 9, 11]
         sorted list:    [2, 3, 6, 7, 9, 11, 12, 14]

**9. Generators - Generator functions allow you to declare a function that behaves like an iterator, i.e. it can be used 
   in a for loop. What is the use case?**

A generator uses 'yield' instead of return after iterating through a list, which saves the state of the function. 
This is so the next time the function is called it continues from where it was with the same variable values.
They are good for using on large datasets or for a function that is too small to warrant creating a class.

For e.g. you could use a generator to create an infinite sequence:

    def infinite_sequence():
        num = 0
        while True:
            yield num
            num += 1


    for i in infinite_sequence():
        print(i, end=" ")


**10. Decorators - A page for useful (or potentially abusive?) decorator ideas. What is the return 
type of the decorator?**

Decorators are used to modify function or class behaviour without changing any of the code in the function. This is 
done by defining a function that returns another function. The decorator can be applied to multiple functions.

- Decorators wrap a function, modifying its behaviour
- Use decorators in a simpler way with the @ symbol
- A decorator is just a regular Python function, so it can be reused as many times as wanted
- Good practice is to move decorators to its own module, so that it can be used in many other functions and to use 
import to make it available in other modules and scripts

        

    e.g 
    def decorator(f):
        def inner_wrapper():
            print("Before the function")
            f()
            print("After the function")
        return inner_wrapper()

    def func():
        print("Hello, my name is Jo")

    decorator(func)

    output:
            Before the function
            Hello, my name is Jo
            After the function

To use this code as a decorator, the syntax would be:
    
    @decorator
    def func():
        print("Hello, my name is Jo")

    output:
            Before the function
            Hello, my name is Jo
            After the function

If you wanted to pass something into your function, you need to add the ability of the function to take arguments, but 
that can also be used on functions that you _don't_ pass an argument to:
    
    e.g 
        def decorator(f):
            def inner_wrapper(*args, **kwargs):
                print("Before the function")
                f(*args, **kwargs)
                print("After the function")
            return inner_wrapper

using *args and **kwargs allows the function to take any amount of arguments and key-word arguments passed to the 
function

    e.g. 
        @decorator
        def func(name):
            print(f"Hello, my name is {name}")

        func("Jo")

        output:
                Before the function
                Hello, my name is Jo
                After the function
    
Decorators are useful for many reasons such as checking argument type or timing how fast a function runs:

checking argument type:
    
    def decorator(f):
        def inner_wrapper(x, y):
            if type(x) and type(y) == int:
                result = f(x, y)
                return result
            elif type(x) or type(y) != int:
                print("Invalid input")
        return inner_wrapper
    
    
    @decorator
    def add(a, b):
        return a+b
    
    print(add(4, 5))

timer:

    import time

    def timer(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            return_value = func()
            total = time.time() - start
            print("Time: ", total)
            return return_value

        return wrapper

    @timer
    def test():
        for _ in range(100000):
            pass

Decorators can be chained in Python - they can all be applied to the same function:

    @decorator_one
    @decorator_two
    @decorator_three
    def simple_function():
        # some logic

Decorators can also be classes where a   _ _ call _ _ method is overwritten:

    class MyClass:

        def __init__(self, function):
            self.function = function

        def __call__(self, *args, **kwargs):
            print("Before the function")
            self.function(*args, **kwargs)
            print("After the function")

    @myclass
    def add(a, b):
        print(a + b)

    add(4, 5)

    output:
        Before the function
        9
        After the function

A decorator can also be used to create a registry of functions:

    registry = []

    def registered(f):
        registry.append(f)
        return f

    @registered
    def one():
        print("hi")

    @registered
    def two():
        print("there")

    def run_all():
        for function in registry:
            function()
    
    run_all()

    output:
            hi
            there

A decorator can also be used to count the function calls:

    def call_counter(f):
        def decorator(*args, **kwargs):
            decorator.calls += 1
            return f(*args, **kwargs)
        decorator.calls = 0
    
        return helper

    @call_counter
    def func(x):
        return x + 1
  
    func.calls = 0
    for i in range(10):
        func(i)
    
    print(func.calls)

Bad example of a decorator:

    @text
    @user
    
    def create_post(user, text):
        backend.callCreatePost(user, text)


    create_post(request) # request??


In this example the decorators need to be passed a request but the user will not know this unless they know how the 
decorator is implemented.


WHAT DOES A DECORATOR RETURN: A decorator returns a modified function or class. 