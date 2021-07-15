# Task: Create a design process for a cinema booking system<br />

# <ins>**Requirements**</ins>
- Customer: Can search for films on a specific date and time
- Customer: Can book seat(s) for a specific date and time
- Customer: Create a user account to book tickets
- Customer: Can pay securely for their tickets
- Make seats unavailable to other customers once reserved
- Admin: Can add a new film with dates and times
- Admin: Can set run dates for films - premiere date to end date
- Admin: Can assign films to screens in the cinema 
- Customer: Review system for films
- Be able to handle large amounts of customers during a popular film ticket release

# <ins>**Potential problems**</ins>
- Multiple users trying to book the same seats at the same times
- Other customers could be blocked from booking seats while seats are reserved
- Assigning screening times to films in a non-staggered fashion causing too many customers in blocks of time
- Double booking of seats
- Customers could leave multiple bad reviews on a film
- Too many customers could slow down the system

# <ins>**Tools**</ins>
- Set a time limit on how long seats are reserved for, say 5-15 minutes before they are released for other customers if 
  booking has not been made
- Secure payment gateway
- Database table to store customer bookings
- Database table to store film times and dates
- Customer interface for booking films
- Admin interface for timetabling films : some sort of calendar function that stops more than x number of films being 
  timetabled at once


