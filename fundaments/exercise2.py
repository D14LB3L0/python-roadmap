# Exercise 2: Sum of several numbers

# Ask the user how many numbers they want to add.
# Then ask them for those numbers one by one.
# Calculate and display the total sum at the end.

def sum_of_numbers():
    while True:
        try:
            count = int(input("How many numbers do you want to add?"))
            if count <= 0:
                print("Please enter a possitive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    while True:
        try:
            numbers = []
            for i in range(count):    
                number = float(input(f"Enter number { i + 1 } of {count}: "))
                numbers.append(number)
            total_sum = sum(numbers)
            print(f"The total sum of the numbers is: {total_sum}")
            break
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

# Execute
sum_of_numbers()