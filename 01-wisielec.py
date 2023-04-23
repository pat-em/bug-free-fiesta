#ok sprawdzać czy użytkownik wpisuje tylko jedną literę
#ok nie pozwalać wpisać tej samej litery
#ok lista słów i losować słowa
#zamiast def słowa samemu to korzystać z biblioteki
#ok zawsze losować inne słowo
#ok restart gry
#ok? poziomy trudności w zależności od liczby prób

import random
from re import A
import sys

list_of_word = ['pies', 'kot', 'kura']
word = random.choice(list_of_word)

used_letters = []
user_word = []
empty_list = []
list_of_letters = ["a", "ą", "b", "c", "ć", "d", "e", "ę", "f", "g", "h", "i", "j", "k", "l", "ł", "m", "n", "ń", "o", "ó", "p", "q", "r", "s", "ś", "t", "u", "v", "w", "x", "y", "z", "ź", "ż"]

def game_difficulty():


    while True:
        difficulty_level = input("""Wybierz poziom trudności (wpisz 1, 2 lub 3):
    poziom 1 - 7 prób
    poziom 2 - 5 prób
    poziom 3 - 3 próby
    """)
        global no_of_tries
        if difficulty_level == str('1'):
            no_of_tries = 7
            return no_of_tries
        elif difficulty_level == str('2'):
            no_of_tries = 5
            return no_of_tries
        elif difficulty_level == str('3'):
            no_of_tries = 3
            return no_of_tries
        else:
            print("Podaj prawidłową wartość")
        
def find_indexes(word, letter):
    indexes = []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)

    return indexes

def show_state_of_game():
    print()
    print(user_word)
    print("Pozostało prób:", no_of_tries)
    print("Użyte litery", used_letters)

def game():
    for _ in word:
        user_word.append("_")
    print (user_word)

    while True:
        letter = input("Podaj literę: ")
        if letter in used_letters:
            print ("Ta litera już była. Spróbuj jeszcze raz.")

        else:
            used_letters.append(letter)

            found_indexes = find_indexes(word,letter)


            if letter in list_of_letters:
                if len(found_indexes) == 0:
                    print("Nie ma takiej litery.")
                    global no_of_tries
                    no_of_tries -=1

                    if no_of_tries==0:
                        print("Koniec gry")
                        break
                else:
                    for index in found_indexes:
                        user_word[index] = letter
                

                    if "".join(user_word) == word:
                        print ("Zgadłeś!")
                        list_of_word.remove(word)
                        if list_of_word == empty_list:
                            print ("Gratulacje! Odgadłeś wszystkie słowa! Koniec gry.")
                            sys.exit()
                        else:
                            break
            
            else:
                print("Podana nieprawidłowa wartość. Podaj literę.")


        show_state_of_game()
        print("* * * * * * *")

###

print("GRA WISIELEC")

game_difficulty()

game()

while True:  
    play_again = input ("Czy chcesz odganąć kolejne słowo? (tak lub nie)")
    if play_again == "tak":
        print ("Zaczynamy")
        no_of_tries = 5
        word = random.choice(list_of_word)

        used_letters = []
        user_word = []
        game()
    elif play_again == "nie":
        print ("Dziękuję za grę!")
        sys.exit(0)
    else:
        print ("Podaj prawidłową wartość (tak lub nie).")
