with open("intermediate/archivo.txt", "w") as file:
    file.write("Hello Word!!\n")
    
with open("intermediate/archivo.txt", "r") as file:
    content = file.read()
    print(content)