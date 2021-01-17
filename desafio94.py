"""Create a program that reads the name, gender and age of several people in a dictionary 
and all dictionaries in a list. At the end, shows:
A) How many people has been registered
B) The age average of the group.
C) A list of all women.
D) A list of all people above the age average"""

import random
person = dict()
contacts = list()
for i in range(0,15):
    name = random.choice(["Armano", "Ermilton","Andre", "Julio", "Gabriel", "Saymon", 
    "Carlos", "Gustavo", "Fonseca", "Mateus", "Thiago", "Fernando", "Juliano", "Rafhael",
    "Fulano", "Sicrano", "Beltrano"])
    age = random.randrange(10, 100)
    gender = random.choice(['M', 'F'])
    person[i] = {'name': name, "gender": gender, "age": age}
    contacts.append(person[i])

print(f"Has been registered a total of: {len(contacts)} people.")
#print(f"The contact list is :{contacts}")




"""name = str(input('Digite um número: '))
gender = str(input('Digite o seu gender [M/F]: ')).strip().upper()
age = int(input('Digite a sua age: '))
"""


print(person)

#lista = {"person": person[i]}
