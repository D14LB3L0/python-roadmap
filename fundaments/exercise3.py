# 1 

# numbers = [5,2,1,4,3]

# numbers.sort()

# for i in range(len(numbers)):
#     print(f"Number at index {i}: {numbers[i]}") 

# print(f"Sorted numbers: {numbers}")

# 2

# def search_number(number_required):
#     for number in numbers:
#         if number == number_required:
#             for i in range(len(numbers)):
#                 if numbers[i] == number_required:
#                     print(f"Number {number_required} found at index {i}")
#             return
#     else:
#         print(f"Number {number_required} not found in the list")
            
# while True:
#     try:
#         number_required = int(input("Put a number: "))
#         break
#     except ValueError:
#         print("Please enter a valid integer.")

# search_number(int(number_required))


# 3

def bucle_names():
    nombres = []
    secretKey = "fin"
    
    while True:
        name = input("Enter a name (or type 'fin' to finish): ")
        if name.lower() == secretKey:
            break
        nombres.append(name)
    
    print("You entered the following names:")
    nombres.sort()
    print(nombres)
        
    print(f"Total names entered: {len(nombres)}")
    
bucle_names()