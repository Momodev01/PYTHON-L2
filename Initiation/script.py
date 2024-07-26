
# First Program
a = "Hello World"
print(a)
# Second Program
def print_hello():
    b = "Hello Python"
    return b
c = print_hello()
print(c)

# Third Program - Function with Parameters
def add_numbers(x, y):
    sum = x + y
    return sum
d = add_numbers(5,  10)
print("The sum is: ", d)
e = add_numbers(3.14, 2.718)
print("The sum is: ", e)

# Fourth Program - Function Returning Multiple Values
def multiply_divide(num1, num2):
    product = num1 * num2
    quotient = num1 / num2
    remainder = num1 % num2
    return product, quotient, remainder
product, quotient, remainder = multiply_divide(9, 6)
print("Product is :", product)
print("Quotient is :", quotient)
print("Remainder is :", remainder)

# Fifth Program - Nested Functions
def outer_func():
    def inner_func():
        return "I am inside the nested function!"
    return inner_func
nested_func = outer_func()
print(nested_func())

# Sixth Program - Lambda Functions (Anonymous Functions)
result = lambda a, b: a * b
print("Result of multiplication: ", result(5, 10))

# Seven  Program - Local and Global Scope
global_var = 10
def local_scope():
    global_var = 5
    print("Inside the function, value of global variable is: ", global_var)
    print("Inside the function, value of local variable is: ")
local_scope()

# C'est quoi Python
"""
1. Langage de programmation
2. Open Source et gratuit
3. Plus de 1 million de développeurs dans le monde
4. Toujours en évolution
5. Popularité croissante
6. Communauté active et très ouverte
7. Facilite la récupération d'erreur
8. Multiplateforme (Windows, Linux, MacOS)
9. Intégré à un IDE (Python IDLE)
10. Documentation abondante et facile à utiliser

"""