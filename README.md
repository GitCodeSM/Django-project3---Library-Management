# Django-project3---Library-Management

Project: mylibrary
App    : management
Files  : requirements.txt
         links.txt

Function: A library management project using Django ModelForm, crispy_forms and rest_framework to display and add, change and remove books and their details as well as             status like issued or available and assign borrower member object.
          A librarian is the admin who can add, remove and change all the fields.
          A new logged-in user from sign-up click can only read previously added books. Can add new book details, status as 'issued' with their own name object only if             librarian has already saved the member name object in the database. New logged in user can't change any details. New logged in user can see book model                   serialization using /book after homepage url.
          Admin librarian has to always add a new member name with every book or add the same name but as new 'member object' for every new book or change the name in             previous book to show it being issued by another name or returned and 'available' in status with a member name 'none'.

Project made by: Swati Mishra
Date: 24th September 2022
