# Defining a function
def greet():
    print("Hello")

greet()

# Parameters and arguments
def greet(name):
    print(f"Hello, {name}!")

greet("Alex")

# Return values
def add(x, y):
    return x + y

result = add(3,4)
print(result)

# Default parameter values
def greet(name="there"):
    print(f"Hello, {name}!")

greet()     # Hello, there!
greet("Alex")   # Hello, Alex!
5
# Keyword args
def describe_pet(animal, name):
    print(f"I have a {animal} named {name}.")

describe_pet(name="Charlie", animal="dog")

# Scope (important)
def example():
    x = 10  # local variable
    print(x)

x = 5   # global variable
example()   # prints 10
print(x)    # prints 5
