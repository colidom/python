import random

students = [
    "Abraham",
    "Víctor Carvajal",
    "Sergio",
    "Carlos Delgado",
    "Alejandro",
    "Víctor García",
    "Carmelo",
    "Alfonso",
    "Noelia",
    "Kevin",
    "Omar",
    "Roberto",
    "Adrián",
    "Yared",
    "Óscar",
    "Carlos Oliva",
    "Adán",
    "Pablo"
]

while students:
    random.shuffle(students)
    print(students.pop(0))
    input()
print("All students got a present!")
