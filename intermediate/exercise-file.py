# 🧪 Tu primer ejercicio:
# Crea un programa que:

# Pida al usuario una frase

# Guarde esa frase en frases.txt

# Luego lea todo el contenido de ese archivo y lo muestre por pantalla

import os

# os > operatin system
# os.makedirs() > Crea un directorio, si no existe

# def save_phrase_to_file():
#     phrase = input("Type a phrase: ")
#     os.makedirs("intermediate", exist_ok=True)
#     with open("intermediate/phrases.txt", "w") as file:
#         file.write(phrase + "\n")
    
# def read_phrases_from_file():
#     try:
#         with open("intermediate/phrases.txt", "r") as file:
#             content = file.read()
#             print("Content of phrases.txt:")
#             print(content)
#     except FileNotFoundError:
#         print("The file phrases.txt does not exist. Please save a phrase first.")
    
# save_phrase_to_file()

# read_phrases_from_file()

# def append_phrase_to_file():
#     os.makedirs("intermediate", exist_ok=True)
    
#     while True: 
#         phrase = input("Type a phrase (or 'fin' to quit): ")
#         if phrase.lower() == "fin":
#             break
#         with open("intermediate/phrases.txt", "a") as file:
#             file.write(phrase + "\n")
            
# append_phrase_to_file()

# def read_phrases_from_file():
    
#     try:
#         with open("intermediate/phrases.txt", "r") as file:
#             content = file.read()
#             print("Content of phrases.txt:")
#             print(content)
#     except FileNotFoundError:
#         print("The file phrases.txt does not exist. Please save a phrase first.")
        
# read_phrases_from_file()

# 🔜 Ejercicio siguiente: Leer frases como lista y analizarlas
# 🎯 Objetivo:
# Leer todas las frases de phrases.txt como una lista de líneas

# Mostrar cuántas frases hay

# Mostrar cada frase una por una con su número de línea

# Preguntar al usuario una palabra y decir si aparece en alguna frase

# def read_phrases_as_list():
#     try:
#         with open("intermediate/phrases.txt", "r") as file:
#             phrases = file.readlines() # devuelve un array
#             print(f"Total phrases: {len(phrases)}")
#             for index, phrase in enumerate(phrases, start=1):
#                 print(f"Phrase {index}: {phrase.strip()}")
#             search_word = input("Enter a word to search in the phrases: ")
#             found = any(search_word.lower() in phrase.lower() for phrase in phrases)
#             if found:
#                 print(f"The word '{search_word}' was found in the phrases.")
#             else:
#                 print(f"The word '{search_word}' was not found in any phrase.")     
#     except FileNotFoundError:
#         print("The file phrases.txt does not exist. Please save a phrase first.")
        
# read_phrases_as_list()

