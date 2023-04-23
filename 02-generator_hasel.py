from ast import Not
import random
import string

password = []
characters_left = 0

def update_characters_left(number_of_characters):
    global characters_left
    while number_of_characters<0 or number_of_characters>characters_left:
        print('Liczba znaków spoza przedziału 0,', characters_left)
        print('Podaj prawidłową wartość')
        number_of_characters=int(input('> '))
        if number_of_characters>0 and number_of_characters<characters_left:
            characters_left-=number_of_characters
            print("Pozostało znaków", characters_left)
            break



password_lenght = input("Jak długie ma być hasło?")
while not password_lenght.isdecimal():
    print ("Podaj prawidłową wartość")
    password_lenght = input('> ')
password_lenght = int(password_lenght)

while password_lenght < 5:
    print("Hasło musi mieć minimum 5 znaków, spróbuj jeszcze raz.")
    password_lenght = int(input("> "))
    if password_lenght>=5:
        break

characters_left = password_lenght

lowercase_letters = input("Ile małych liter ma mieć hasło?")
while not lowercase_letters.isdecimal():
    print ("Podaj prawidłową wartość")
    lowercase_letters = input('> ')
lowercase_letters = int(lowercase_letters)
update_characters_left(lowercase_letters)


uppercase_letters = (input("Ile dużych liter ma mieć hasło?"))
while not uppercase_letters.isdecimal():
    print ("Podaj prawidłową wartość")
    uppercase_letters = input('> ')
uppercase_letters = int(uppercase_letters)
update_characters_left(uppercase_letters)


special_characters = input("Ile znaków specjalnych ma mieć hasło?")
while not special_characters.isdecimal():
    print ("Podaj prawidłową wartość")
    special_characters = input('> ')
special_characters = int(special_characters)
update_characters_left(special_characters)


digits = input("Ile cyfr ma mieć hasło?")
while not digits.isdecimal():
    print ("Podaj prawidłową wartość")
    digits = input('> ')
digits = int(digits)
update_characters_left(digits)

if characters_left>0:
    print("Nie wszystkie znaki zostały wykorzystane. Hasło zostanie uzupełnione małymi literami")
    lowercase_letters +=lowercase_letters

print()
print("Długość hasła:", password_lenght)
print("Małe litery:", lowercase_letters)
print("Duże litery", uppercase_letters)
print("Znaki specjalne", special_characters)
print("Cyfry:", digits)

for _ in range(password_lenght):
    if lowercase_letters >0:
        password.append(random.choice(string.ascii_lowercase))
        lowercase_letters -= 1
    if uppercase_letters >0:
        password.append(random.choice(string.ascii_uppercase))
        uppercase_letters -= 1
    if special_characters >0:
        password.append(random.choice(string.punctuation))
        special_characters -= 1
    if digits >0:
        password.append(random.choice(string.digits))
        digits -= 1

random.shuffle(password)
print("Wygenerowane hasło:", "".join(password))