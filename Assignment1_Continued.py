# Question 1: Write a Python program that takes two numbers as input from the user and performs the following operations:
# n1 = int(input("Enter First Number:"))
# n2 = int(input("Enter Second Number:"))
# print("Addition of numbers:",n1+n2)
# print("subtraction of numbers:",n1-n2)
# print("multiplication of numbers:",n1*n2)
# if n1>=n2:
#     print("Division of numbers:", n1 / n2)
#     print("modulus of numbers:",n1%n2)
# else:
#     print("Division of numbers:", n2 / n1)
#     print("modulus of numbers:", n1 % n2)



# Addition
# Subtraction
# Multiplication
# Division
# Modulus
# Display the results for each operation.
#
# Question 2: Write a Python program that checks whether a given number is even or odd using the modulus operator.
# n3 = int(input("Enter third Number:"))
# if n3%2==0:
#     print("Given number is even")
# else:
#     print("Given number is odd")
#
# # Question 3: Write a Python program that takes a number as input from the user and checks if it is positive, negative, or zero.
# n4 = int(input("Enter fourth Number:"))
# if n4>0:
#     print("Number is postive")
# elif n4<0:
#     print("number is negative")
# else:
#     print("number is zero")

#
# Question 4: Write a Python program that calculates the grade of a student based on the marks entered by the user. The grading scale is as follows:
# Grade= int(input("Enter Grade:"))
# if Grade >=90:
#     print("Grade of student: A")
# elif Grade >=80 and Grade < 90:
#     print("Grade of student: B")
# elif Grade >=70 and Grade < 80:
#     print("Grade of student: C")
# elif Grade >=60 and Grade < 70:
#     print("Grade of student: D")
# else :
#     print("Grade of student: F")



# 90 and above: A
# 80 - 89: B
# 70 - 79: C
# 60 - 69: D
# Below 60: F
# Question 5: Write a Python program to create a text file called sample.txt and write the sentence "Hello, this is a sample file." to the file. Then, read and display the content from the file.
file = open("sample.txt", "w")
file.write("Hello, this is a sample file.")

file.close()
file = open("sample.txt", "r")
content = file.read()
print(content)
# Opens in read mode

# Question 6: Write a Python program that reads a text file called data.txt and counts the number of words in the file.
file = open("data.txt", "w")
file.write("Hello, this is a data file.")

file.close()
file = open("data.txt", "r")
content = file.read()
print(len(content.split()))
# Question 7: Write a Python program to print the numbers from 1 to 10 using a for loop.
for i in range(1,11):
    print("number:",i)
# Question 8: Write a Python program to display the multiplication table of a number entered by the user using a for loop.
n6 = int(input("Enter  Number for multiplication table:"))
for i in range(1,11):
    result=n6*i
    print(f"{n6} x {i} = {result}")