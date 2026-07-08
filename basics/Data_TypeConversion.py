# Checking Data Types in Python
''' 1. type(): Returns the type of a variable.
    2. isinstance(): Checks if a variable belongs to a certain type.'''

a = 5.5
print(type(a))  # Output: <class 'float'>

print(isinstance(a, int))  # Output: False
print(isinstance(a, float))  # Output: True
# -----------------------------------------------------------------------------------------------------------------------------------
# TYPES OF DATA TYPE Conversion

# 1. Implicit data Type Conversion (Type Casting) or Coercion:
'''Python automatically converts one data type to another without user intervention. This is known as implicit type conversion or coercion. It takes place either during compilation or during run time and is handled directly by Python '''
# Example: When we add an integer and a float, Python automatically converts the integer to a float to avoid losing information.
a_int = 5
b_float = 1.0
c_sum = a_int + b_float
print(c_sum)
print(type(c_sum))

'''Why was the float data type chosen for the result? 
=> Because float has a higher precision than int, so Python automatically converts the int to float to avoid losing information.'''
print('-------------------------------')
# 2. Exlicit data Type Conversion (Manual):
'''In explicit type conversion, the user manually converts one data type to another using built-in functions. This is also known as type casting.'''
# We use the built-in functions like int(), float(), str(), etc to perform explicit type conversion.

# Example: Adding of String and Integer using Explicit Type Conversion
a_str = "5"
b_int = 10
print("Before Conversion: ", type(a_str))  # Output: <class 'str'>
print("Before Conversion: ", type(b_int))  # Output: <class 'int'>

# explicit type conversion
a_int = int(a_str)  # Convert string to integer
print("After Conversion: ", type(a_int))  # Output: <class 'int'>

num_sum = a_int + b_int
print("Sum: ", num_sum)  # Output: 15
print("Data type of num_sum: ", type(num_sum))  # Output: <class 'int'>


