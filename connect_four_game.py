import sys
import time

row_count = int(6)
column_count = int(7)
no_of_files = row_count * column_count

board = [[0 for i in range(column_count)] for j in range(row_count)]
list_of_players = ["Player 1", "Player 2"]
list_of_move = []
player = 0
i=1

        
def next_move(no_of_player):

    def move_validation(move_to_check):
        while not move_to_check.isdecimal() or int(move_to_check)<1 or int(move_to_check)>column_count:
            print('Select a number in range 1 - {}'.format(column_count))
            move_to_check = input('> ')
        return move_to_check

    print(list_of_players[no_of_player])
    
    move = input("Select a column number: ")
    move = int(move_validation(move))

    list_of_move.append(move)

#--------------sprawdzanie czy kolumna jest pełna------------------
    while list_of_move.count(move) > row_count:
        print('This column is full, please choose another one:')
        list_of_move.remove(move)
        move = input('> ')
        move = int(move_validation(move))
        list_of_move.append(move)

#--------------uzupełnianie tablicy------------------
    row = row_count
    if no_of_player == 0:
        while board[row-1][move-1] != 0: #dopóki miejsce jest różne od zera tj zajęte
            row -= 1 #zmieniaj rząd na 1 mniejszy
        board[row-1][move-1] = 1
         
    else:
        while board[row-1][move-1] != 0:
            row -= 1
        board[row-1][move-1] = 2

#--------------wyświetlanie tablicy------------------ 
    global i
    i=1
    print("   1  2  3  4  5  6  7")       
    for row in board:
        print(i, row)
        i+=1

def check_winner(check_board):

#--------------sprawdzanie wygranej w rzędzie------------------      
    
    for x in range(row_count):
        for y in range(column_count-3): #Dla każdego y w przedziale (0,4)
            if check_board[x][y] == check_board[x][y+1] == check_board[x][y+2] == check_board[x][y+3] == 1: #Jeśli [0][0] = [0][1] = [0][2] = [0][4] = 1
                print('Player 1 wins')
                time.sleep(10)
                sys.exit(0)
            elif check_board[x][y] == check_board[x][y+1] == check_board[x][y+2] == check_board[x][y+3] == 2:
                print('Player 2 wins')
                time.sleep(10)
                sys.exit(0)

#--------------sprawdzanie wygranej w kolumnie------------------ 

    for y in range(column_count):        
        for x in range(row_count-3):
            if check_board[x][y] == check_board[x+1][y] == check_board[x+2][y] == check_board[x+3][y] == 1:
                print('Player 1 wins')
                time.sleep(10)
                sys.exit(0)
            elif check_board[x][y] == check_board[x+1][y] == check_board[x+2][y] == check_board[x+3][y] == 2:
                print('Player 2 wins')
                time.sleep(10)
                sys.exit(0)

#--------------sprawdzanie wygranej po skosie malejąco------------------ 

    for x in range (row_count-3):
        for y in range(column_count-3):
            if check_board[x][y] == check_board[x+1][y+1] == check_board[x+2][y+2] == check_board[x+3][y+3] == 1:
                print('Player 1 wins')
                time.sleep(10)
                sys.exit(0)
            elif check_board[x][y] == check_board[x+1][y+1] == check_board[x+2][y+2] == check_board[x+3][y+3] == 2:
                print('Player 2 wins')
                time.sleep(10)
                sys.exit(0)

 #--------------sprawdzanie wygranej po skosie rosnąco------------------ 

    for x in range (row_count-3):
        for y in range(column_count-3):
            if check_board[x][y+3] == check_board[x+1][y+2] == check_board[x+2][y+1] == check_board[x+3][y] == 1:
                print('Player 1 wins')
                time.sleep(10)
                sys.exit(0)
            elif check_board[x][y+3] == check_board[x+1][y+2] == check_board[x+2][y+1] == check_board[x+3][y] == 2:
                print('Player 2 wins')
                time.sleep(10)
                sys.exit(0)               

print("""\nConnect four\n""")

print("   1  2  3  4  5  6  7")

for row in board:
    print(i, row)
    i+=1

while True:
    if len(list_of_move)<no_of_files:
        next_move(player)
        if player == 0:
            player = 1
        else:
            player = 0 
        check_winner(board)
    else:
        print('All fields are filled')
        time.sleep(10)
        sys.exit(0)

    
