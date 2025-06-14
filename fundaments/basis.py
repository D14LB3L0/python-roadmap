
# variables
name = "Diego"
age = 21
height = 1.65
is_student = True

print(f"My name is {name}")
print(f"I am {age} years old")
print(f"My height is {height} meters")
print(f"Am I a student? {is_student}")


# operators
addition = 2 + 3
compare = age > 18
logical = True and False

# control structure
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
    
    
for i in range(5):
    print(f"Iteration {i}")
    
    
count = 0
    
while count < 3:
    print(f"Count is {count}")
    count += 1
    

# functions
def greet(name):
    print(f"Hello, {name}!")
    
greet("Diego")

# Dictionaries
Person = {
    "name": "Diego",
    "age": 21,
    "active": True,
}

print(f"Name: {Person['name']}")    
print(f"Age: {Person['age']}")

# Functions
def multiply(a, b):
    return a * b

result = multiply(3, 4)
print(f"Multiplication result: {result}")