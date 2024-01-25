Problem Statement:
==========================

In a university, your attendance determines whether you will be
allowed to attend your graduation ceremony.
You are not allowed to miss classes for four or more consecutive days.
Your graduation ceremony is on the last day of the academic year,
which is the Nth day.
 
Your task is to determine the following:

1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.

Represent the solution in the string format as "Answer of (2) / Answer
of (1)", don't actually divide or reduce the fraction to decimal


Assumptions:
==========================
1) No persistence layer (DB) usage

Entities:
==========================
1) University
2) Student

Notes:
==========================
1) Cannot miss >= 4 consecutive days of classes
2) graduation ceremony is on the last day of the academic year (Nth day)
3) **no_of_classes_cant_miss is dynamic we can provide any number instead of 4 in the input**


Solve:
==========================
1) The number of ways to attend classes over N days.
2) The probability that you will miss your graduation ceremony.

Output:
==========================
The solution is represented in the string format as "Answer of (2) / Answer of (1)".


Steps to Run:
==========================
python3 main.py

CD university   
python3 main.py 

**Enter | seperated values of University: name|graduation_days|no_of_classes_cant_miss**

    nalanda|5|4

**Enter | seperated values of Student Details: name**

    student1

**output**

    for 5 days : 14/29

➜  university python3 main.py 

**Enter | seperated values of University: name|graduation_days|no_of_classes_cant_miss**

    nalanda|10|4

**Enter | seperated values of Student Details: name**

    student1  

**output**

    for 10 days : 372/773


Approach
========
1) we calculated and formulated all the strings of len equal to days where on a day a student will attend class or not
2) if a student way has missed n consecutive classes we wont consider them as valid
3) we store valid ways in student obj for further processing
1) StudentServices.calculate_ways takes O(2^N) as all the ways are calculated and stored
2) to calculate all valid ways it takes O(N) as we are working on the stored ways
