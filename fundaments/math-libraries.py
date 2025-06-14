import math

print(math.sqrt(16))  

def circle_area(radius):
    return math.pi * (radius ** 2)

print(circle_area(3))

def count_vowels(frase):
    vowels = "aeiouAEIOU"
    contador = 0
    for letter in frase:
        if letter in vowels:
            contador += 1
    return contador
    
frase = input("Digite uma frase: ")

print(f"Number of vowels in the phrase {frase} is {count_vowels(frase)}")    

