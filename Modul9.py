import os
import json

os.system('cls')
# Spara en inmatning & läs in den när man startar programmet

# with open("text.txt", "w") as my_file:
#     my_file.write("Hello world\n")
#     my_file.write("How are you doing\n")
#     my_file.write("Yay!\n")

# with open("text.txt") as my_file:
#     print(my_file.read())

# Gör så programmet matar ut “Inget sparat” om filen inte existerar

# try:
#     my_file = open("doesntexist.txt" "w")
#     my_file.write("Hii")
# except FileNotFoundError:
#     print("No such file found")
# Läs om json-format

# Skapa ett program som sparar flera saker med bibliotek och JSON-format

bibl = {
    "Name":"Toilet",
    "Model":"Gaming-Toilet123"
}

with open("text.json", "w") as my_file:
    json.dump(bibl, my_file)
    my_file.flush() 
    with open("text.json", "r") as my_file:
        subjects = json.load(my_file)
        print(subjects["Model"])


# Skapa/uppdatera ett program som sparar en lista med saker/namn (t.ex. bästa vänner projektet)
