"""
Escribe una función que tome un caracter y devuelva True si es una vocal, o de lo contrario devuelva false
"""

def is_vowel(character):
    vowels_list = ['a', 'e', 'i', 'o', 'u']
    if character in vowels_list:
        return True
    else:
        return False

print(is_vowel('a'))
