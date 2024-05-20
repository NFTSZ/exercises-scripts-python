
numbers = input("Insert two numbers (x, x): ") # 2.5, 7'
a, b = numbers.split(", ") # a = '2.5',  b = '7'
print(f'{type(a)}, {type(b)}') # <class 'str'>, <class 'str'>
print(f"{a.isdecimal()}, {b.isdecimal()}") # False, True 

# example with sum
the_sum = (int(a) if a.isdecimal() else float(a)) + (int(b) if b.isdecimal() else float(b)) # a == <class 'float'>,  b == <class 'int'>
print(f"Sum: {the_sum, type(the_sum)}") # 9.5, <class 'float'>

# example with name
'''complete_name = input("Name and surname ")
name, surname = complete_name.split(" ")

complete_name = (name.capitalize()) + " " + (surname.capitalize())
print(f"Ola, {complete_name}")'''