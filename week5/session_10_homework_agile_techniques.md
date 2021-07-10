# Question 1.
# <ins>**Scrum Ceremonies**</ins>

_**Product backlog refinement:**_ During this process items are reviewed and revised by the product owner and the development team, details are decided on, estimates are added, and the items are ordered. How the refinement is done is decided by the Scrum Team.

_**Sprint planning:**_ Sprint planning addresses two questions: what and how? The purpose of sprint planning is to get the development team and product owner on the same page on what will be built next. A new objective is introduced that should be completed in the next sprint and then a sprint goal is created by the Scrum Team; from this the development team picking items from the product backlog based on what will be needed to achieve the sprint goal. Furthermore, the development team picks a high priority improvement issue from the previous sprint retrospective to complete and creates a plan on how to accomplish its forecast.

_**Daily scrum:**_ A daily scrum is a meeting for the development team held at the same time every day during a sprint. During the meeting the tasks that need completing for the next 24 hours are decided on and the work completed from the last 24 hours are discussed – they keep everyone on track for achieving goals and up-to-date on what everyone else is doing too.

_**Sprint review:**_ During a sprint review the Scrum Team, Product Owner and key stakeholders are in attendance to hear about which items from the product backlog have been completed and what is left to do. The development team will review what was successful and any problems they encountered during the sprint as well as how any of the problems were solved – they also answer questions about the increment. Further to this, target delivery dates based on current progress are projected by the product owner and the whole group collaborates on the next goals. Moreover, the potentiality of the product is reviewed as well as the timeline and budget.

_**Sprint retrospective:**_ This is used to look at the last sprint and see how well it went in regards to tools, relationships, people and process. It is used to identify items that need to be improved and also major items that went well. Furthermore, a plan is created for ways that the Scrum Team can improve their work practices. 

# <ins>**Scrum Roles**</ins>

_**Scrum Master:**_ A Scrum Master is someone who leads – they serve the Scrum Team and the organisation they work for. A Scrum Master has many roles: they coach team members and help them in creating high-value increments, help remove impediments to progress and make sure all events are positive and happen within the timebox. The Scrum Master also serves the Product Owner: they help with product backlog management and product goal definition, product planning and facilitate collaboration with stakeholders. Furthermore, the Scrum Master serves the organisation through leading, training and coaching, planning and advising Scrum implementations, helping employees and stakeholders understand a good approach to complex work and finally removing barriers between stakeholders and Scrum Teams.

_**Product Owner:**_ A Product Owner is responsible for getting the maximum value of the product from the work done by the Scrum Team. They are also responsible for management of product backlog, including: developing and communicating the product goal, creating and communicating product backlog items and ordering product backlog items. Sometimes the Product Owner completes this work themselves, other times they may delegate the work to someone else.

_**Development Team:**_ The development team are the people that do the work – a person in the development team is a team member who has the right skills to do the work required as part of the team. A development team has to be able to self-organise to make decisions on work and get the work complete. Responsibilities include: delivering work throughout the sprint, attending the daily scrum and discussing progress.

# Question 2.
# <ins>**Yoga Booking System**</ins>

**<ins>Epic</ins>**
<br />Create a yoga class booking system<br />

**Task:** Create an SQL database for a yoga booking system<br />
There needs to be an SQL database for the yoga booking system.<br />
Tables needed:
- classes
- bookings
- customer information

<ins>**Story**</ins><br />
**_As a:_ <ins>yoga customer</ins>**<br />*I want to:* view a list of yoga classes<br />
**_As a:_ <ins>yoga instructor</ins>**<br />*I want to:* view a list of yoga classes<br />

**<ins>Tasks</ins>**<br />

**Task:** Create a table for classes<br />
There needs to be an SQL table with that classes information can be added to.<br />
Information needed:
- Instructor name
- Class name
- Class data and time
- Class ID

**Task:** Add API route to list all classes<br />
There needs to be an API route to list all classes. It should return all classes as a json object.<br />
**Route:** '/classes'<br />**Method:** GET<br />**Example:**<br />[<br />{<br />title: 'Hatha Yoga'<br />datetime: '2021-07-10 18:00'
<br />instructor_name: 'Gerald'<br />class_id: 07865<br />}<br />]

<ins>**Story**</ins><br />
**_As a:_ <ins>yoga instructor</ins>**<br />*I want to:* be able to add a yoga class<br />

**<ins>Tasks</ins>**<br />
**Task:** Add API route to add a class to the schedule<br />
There needs to be an API route to add a class to the schedule.<br />
**Route:** '/classes/{int:id}'<br />**Method:** POST<br />**Example:**<br />[<br />{<br />title: 'Hatha Yoga'<br />datetime: '2021-07-10 18:00'
<br />instructor_name: 'Gerald'<br />class_id: 07865<br />}<br />]

<ins>**Story**</ins><br />
**_As a:_ <ins>yoga customer</ins>**<br />*I want to:* be able to book a yoga class<br />


**<ins>Tasks</ins>**<br />

**Task:** Create a table for customer information<br />
There needs to be an SQL table containing customer information.<br />
Information needed:
- Customer name
- Customer telephone number
- Customer email
- Customer ID

**Task:** Create a table for bookings<br />
There needs to be an SQL table that customer bookings can be added to.<br />
Information needed:
- Customer name 
- Customer ID
- Instructor name
- Class ID

**Task:** Add API route to add a customer booking<br />
There needs to be an API route to add a customer booking.<br />
**Route:** '/booking/{int:id}'<br />**Method:** POST<br />**Example:**<br />[<br />{<br />title: 'Hatha Yoga'<br />datetime: '2021-07-10 18:00'
<br />customer_name: 'Samantha Jones'<br />customer_ID: '000245'<br />instructor_name: 'Gerald'<br />class_id: 07865<br />}<br />]

<ins>**Story**</ins><br />
**_As a:_ <ins>yoga instructor</ins>**<br />*I want to:* be able to delete a yoga class<br />

**<ins>Tasks</ins>**<br />
**Task:** Add API route to delete a class from the schedule<br />
There needs to be an API route to delete a class from the schedule.<br />
**Route:** '/classes/{int:id}'<br />**Method:** DELETE<br />**Example:**<br />[<br />{<br />class_id: 07865<br />}<br />]

**<ins>Tasks</ins>**<br />

**Task:** Create a customer interface<br />
There needs to be a customer interface which shows:
- A list of yoga classes with: 
  - Class Name 
  - Date and time
  - Name of instructor
  - Has a book now button
    
**Task:** Create an instructor interface<br />
There needs to be an instructor interface which is:
- An HTML form to schedule a class with: 
  - Class Name 
  - Date and time
  - Name of instructor
  
<ins>**TASK ORDER**</ins>
- Create yoga booking database
- Create classes table and API route retrieve classes information
- Create API route to add a class to the table
- Create customer information table
- Create bookings table and API route to add a booking to the table
- Create API route to delete a class from the schedule
- Create user interfaces