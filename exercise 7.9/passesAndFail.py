# passesAndFails.py
# prompts the user to enter 6
# student names and their marks
# and then displays if the students
# have passed or failed. The pass mark is
# greater to or equal to 40%
# D.H. February 2005

# Create lists to hold the names of the students and their marks
name = ["","","","","","", ""]
marks = [0,0,0,0,0,0,0]

#Enter the names and marks
print "Please type in 7 names and marks:"
for i in range(7):
    print "Enter name", i + 1,
    name[i] = raw_input()
    print "Enter mark", i + 1,
    marks[i] = input()

print
print "These are the passes and fails:"
print

for i in range(7):
    print name[i],":",
    if marks[i] >= 40:
        print "Pass"
    else:
        print "Fail"




-----------------------------------------------------------------------------
-----------------------------------------------------------------------------



Python 2.7.6 (default, Nov 10 2013, 19:24:24) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
Please type in 7 names and marks:
Enter name 1 Madiha
Enter mark 1 90
Enter name 2 Ella
Enter mark 2 90
Enter name 3 Andrea
Enter mark 3 90
Enter name 4 Bella
Enter mark 4 90
Enter name 5 Jasmin
Enter mark 5 50
Enter name 6 Anne
Enter mark 6 85
Please type in 7 names and marks:
Enter name 1 
>>> ================================ RESTART ================================
>>> 
Please type in 7 names and marks:
Enter name 1 Madiha
Enter mark 1 90
Enter name 2 Ella
Enter mark 2 90
Enter name 3 Andrea
Enter mark 3 90
Enter name 4 Bella
Enter mark 4 90
Enter name 5 Jasmin
Enter mark 5 50
Enter name 6 Anne
Enter mark 6 85
Enter name 7 Lizzie
Enter mark 7 70
Please type in 7 names and marks:
Enter name 1 
>>> ================================ RESTART ================================
>>> 
Please type in 7 names and marks:
Enter name 1 Madiha
Enter mark 1 90
Enter name 2 Ella
Enter mark 2 90
Enter name 3 Andrea
Enter mark 3 90
Enter name 4 Bella
Enter mark 4 90
Enter name 5 JASMIN
Enter mark 5 50
Enter name 6 Anne
Enter mark 6 85
Enter name 7 Lizzie
Enter mark 7 70

These are the passes and fails:

 : Pass
Lizzie : Pass
 : Pass
 : Pass
 : Pass
 : Pass
 : Pass
>>> ================================ RESTART ================================
>>> 
Please type in 7 names and marks:
Enter name 1 Madiha
Enter mark 1 90
Enter name 2 Ella
Enter mark 2 90
Enter name 3 Andrea
Enter mark 3 90
Enter name 4 Bella
Enter mark 4 90
Enter name 5 Jasmin
Enter mark 5 50
Enter name 6 Anne
Enter mark 6 85
Enter name 7 Lizzie
Enter mark 7 70

These are the passes and fails:

Madiha : Pass
Ella : Pass
Andrea : Pass
Bella : Pass
Jasmin : Pass
Anne : Pass
Lizzie : Pass
