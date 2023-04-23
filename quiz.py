import json
import random

types_of_responses = ["a", "b", "c", "d"]
points = 0


def show_question(question):
    global points

    print()
    print(question["pytanie"])
    print("a:", question["a"])
    print("b:", question["b"])
    print("c:", question["c"])
    print("d:", question["d"])
    print()

    answer = input("Którą odpowiedź wybierasz? ")
    while not answer in types_of_responses:
        print ("Podaj prawidłową wartość.")
        answer = input ('> ')
        if answer in types_of_responses:
            break

    if answer == question["prawidlowa_odpowiedz"]:
        points += 1
        print("To prawidłowa odpowiedź, brawo! Masz już", points, "punktów.")
    else:
        print("Niestety to zła odpowiedź, prawidłowa odpowiedź to " + question["prawidlowa_odpowiedz"] + ".")


with open("quiz.json", encoding="utf-8") as json_file:
    questions = json.load(json_file)
    random.shuffle(questions)

    for i in range(0, len(questions)):
        show_question(questions[i])

print()
print("To koniec gry, zdobyta liczba punktów to " + str(points) + ".")

#DONE odpowiednia walidacja danych
#DONE losowanie pytań
#zapisywać które pytania już były
#różne kategorie pytań
#różny poziom trudności i różna punktacja
#dodanie opcji "nie wiem" i punkty ujemne
#pół na pół i inne odpowiedzi
#ranking najlepszych wyników