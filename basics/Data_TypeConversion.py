# Checking Data Types in Python
''' 1. type(): Returns the type of a variable.
    2. isinstance(): Checks if a variable belongs to a certain type.'''

a = 5.5
print(type(a))  # Output: <class 'float'>

print(isinstance(a, int))  # Output: False
print(isinstance(a, float))  # Output: True
# -----------------------------------------------------------------------------------------------------------------------------------
# TYPE OF DATA TYPE Conversion

# 1. Implicit data Type Conversion (Type Casting) or Coercion:
'''Python automatically converts one data type to another without user intervention. This is known as implicit type conversion or coercion. It takes place either during compilation or during run time and is handled directly by Python '''

a_int = 5
b_float = 1.0
c_sum = a_int + b_float
print(c_sum)
print(type(c_sum))

'''Why was the float data type chosen for the result? 
=> Because float has a higher precision than int, so Python automatically converts the int to float to avoid losing information.'''

