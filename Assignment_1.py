# 1.Define a variable as Integer(1) ,Float(1.0) and String(‘1’) and print and return the value and type of variable.
Integer_var=1
Float_var=1.0
String_var='1'
print('Interger value :',Integer_var,'Type:',type(Integer_var))
print('Float value :',Float_var,'Type:',type(Float_var))
print('String value :',String_var,'Type:',type(String_var))
#
#
# 2.Redeclare the same variable as another number.(2,2.0 and ‘2’) and share your observation on result.
# Integer_var=2
# Float_var=2.0
# String_var='2'
# print('Interger value :',Integer_var,'Type:',type(Integer_var))
# print('Float value :',Float_var,'Type:',type(Float_var))
# print('String value :',String_var,'Type:',type(String_var))
#Observation: New values are replaced with old Values
# 3. Assigning a single value to several variables simultaneously with “=” operators.(a=b=c=10) and print the values of a,b and c..
# a=10
# b=10
# c=10
# print("value of a:",a,"value of b:",b,"value of c:",c)
# 4.Assign two variables a and b as integer and print the sum of a+b.
# a=10
# b=10
# print("Sum of a and b:",a+b)
#
# 5.Write a Python program to create a list with five different fruits. eg:fruits = ["apple", "banana", "cherry", "date", "elderberry"]?
# fruits = ['Apple', 'Banana', 'Mango', 'Orange', 'Grapes']
# print("List of fruits:", fruits)

# # 6. How do you access the second and fourth elements from the list.
# print("List of fruits:", fruits[1],fruits[3])
#
# 7.Modify the third element in the list numbers = [10, 20, 30, 40, 50] to 35.
# list_numbers = [10, 20, 30, 40, 50]
# list_numbers[2]=35
# print("list_numbers:",list_numbers)
# Create a Tuple:How do you create a tuple with the following elements: "red", "green", "blue"?
# tuple_colors=("red", "green", "blue")
#
# Access Elements in a Tuple:How do you access the first and last elements in the tuple colors = ("red", "green", "blue", "yellow")?
# print("tuple_colrs:",tuple_colors)
#
# Immutable Nature of Tuples:What happens if you try to change the second element of the tuple colors = ("red", "green", "blue")?
# tuple_colors(1)="brown"
# print("tuple_colrs:",tuple_colors)
# observation: SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?

#
# Tuple Unpacking:Given the tuple coordinates = (10, 20, 30), write a Python program to unpack it into three variables x, y, and z.
# tuple_coordinates = (10, 20, 30)
# x,y,z=tuple_coordinates
# print("The value of x,y,z:",x,y,z)
#
# Check Element in Tuple:Write a Python program to check if the element "blue" is present in the tuple colors = ("red", "green", "blue").
# tuple_colors = ("red", "green", "blue")
# if "blue" in tuple_colors:
#     print("Color blue available in tuple_colors")
# else:
#     print("Color blue not available in tuple_colors")

# Tuple Length:Write a Python program to find the length of the tuple days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday").

# tuple_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
# print("length of tuple_days:",len(tuple_days))
# Create a Dictionary:Create a dictionary where the keys are student names and the values are their grades. For example:
#
# {"Alice": 85, "Bob": 90, "Charlie": 78}
# student_dict ={"Alice": 85, "Bob": 90, "Charlie": 78}


#
# Access Dictionary Values:How do you access Bob's grade from the dictionary students = {"Alice": 85, "Bob": 90, "Charlie": 78}?

# print("grade of bob:",student_dict["Bob"])
# Add and Remove Key-Value Pairs:Add a new student "David": 92 to the dictionary students = {"Alice": 85, "Bob": 90, "Charlie": 78} and remove "Charlie" from the dictionary.

# student_dict["David"]=92
# print("Students",student_dict)
# Update Dictionary Values:Write a Python program to update Bob's grade to 95 in the dictionary students = {"Alice": 85, "Bob": 90, "Charlie": 78}.
# student_dict["Bob"]=95
# print("grade of bob updated:",student_dict)
# Check if Key Exists in a Dictionary:Write a Python program to check if "Alice" is a key in the dictionary students = {"Alice": 85, "Bob": 90, "Charlie": 78}.
# if "Alice"in student_dict:
#     print("Alice is  a key in dictonary")
# else:
#     print("Alice not in dictonary")
# Dictionary Length:Write a Python program to find the number of key-value pairs in the dictionary students = {"Alice": 85, "Bob": 90, "Charlie": 78}.

# print("The number of key-value pairs in student_dict:", len(student_dict))