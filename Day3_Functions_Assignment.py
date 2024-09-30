# Write a Python function to find the maximum of three numbers
from operator import truediv

a = 10
b = 20
c = 40
print(max(a, b, c))
# Write a Python function to multiply all the numbers in a list.
def multiply(numbers):
    product=1
    for num in numbers:
        product *= num
    return product
Sample_List = (8, 2, 3, -1, 7)
print(multiply(Sample_List))
#reverse a string.
def revstring(string):
    length=len(string)
    for i in range(length - 1, -1, -1):
        print(string[i],end='')
Sample_String= "1234abcd"
revstring(Sample_String)
# Write a Python function to calculate the factorial of a number(a non - negative integer).The
# function accepts the  number as an argument.
def factorial(number):
    fact=1
    for i in range(number,1,-1):
        fact*=i
    print("Factorial is", fact)
number=6
factorial(number)

# WriteaPythonfunctionthattakesalist and returnsanewlistwith distinct elements from the first list.
Sample_List1 = [1,2,3,3,3,3,4,5]
print(list(set(Sample_List1)))
# Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
def isprime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
number=11
if isprime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

# Write a Python program to print the even numbers from a given list.
def iseven(list):
    even_numbers=[]
    for i in range(len(list)):
        if list[i]%2==0:
            even_numbers.append(list[i])
    print(even_numbers)
Sample_List= [1, 2, 3, 4, 5, 6, 7, 8, 9]
iseven(Sample_List)
# Write a Python function that accepts a string and counts the number of upper and lower case letters.
def upperorlower(string):
    upper_count=0
    lower_count=0
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    print(f"Uppercase letters: {upper_count}, Lowercase letters: {lower_count}")
string='The quick Brow Fox'
upperorlower(string)

# Write a Python function to sum all the numbers in a list.
def sum(list):
    result=0
    for i in list:
        result+=i
    print(result)
Sample_List2 = (8, 2, 3, 0, 7)
sum(Sample_List2)
# WriteaPythonfunctionthatcheckswhetherapassedstring is apalindrome or not.
def ispalindrome(string):
    length = len(string)
    new_string = ''
    for i in range(length - 1, -1, -1):
        new_string += string[i]
    if new_string==string:
        print ("string is Palindrome")
    else:
        print("string is not Palindrome")
string='nursesrun'
ispalindrome(string)
