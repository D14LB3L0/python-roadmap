# Exercise 1: User Input and Conditional Logic

# Ask the user for their name and age.
# Display a message like: "Hi Diego, you're 21."
# If they're 18 or older, tell them they can vote. If not, tell them they can't yet.


# Get user input for name and age 
def get_user_info():
    name = input("Please enter your name: ")
    
    while True:
        try:
            age = int(input("Please enter your age: "))
            break  
        except ValueError:
            print("Please enter a valid number.")
    
    if age >= 18:
        print(f"Hi {name}, you're {age}. You can vote.")
    else:
        print(f"Hi {name}, you're {age}. You can't vote yet.")
    
# Execute the function to get user input   
get_user_info()