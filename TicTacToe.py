# Tic Tac Toe game in Python

# Initialize an empty board
board = [' ' for _ in range(9)]

# Function to print the board
def print_board():
    row1 = '| {} | {} | {} |'.format(board[0], board[1], board[2])
    row2 = '| {} | {} | {} |'.format(board[3], board[4], board[5])
    row3 = '| {} | {} | {} |'.format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

# Function to handle player moves
def player_move(icon):
    if icon == 'X':
        number = 1
    elif icon == 'O':
        number = 2

    print("Player {}, enter your move (1-9): ".format(number))
    choice = int(input().strip())
    if board[choice - 1] == ' ':
        board[choice - 1] = icon
    else:
        print()
        print("That space is taken! Try again.")
        player_move(icon)

# Function to check for victory
def is_victory(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
        (board[3] == icon and board[4] == icon and board[5] == icon) or \
        (board[6] == icon and board[7] == icon and board[8] == icon) or \
        (board[0] == icon and board[3] == icon and board[6] == icon) or \
        (board[1] == icon and board[4] == icon and board[7] == icon) or \
        (board[2] == icon and board[5] == icon and board[8] == icon) or \
        (board[0] == icon and board[4] == icon and board[8] == icon) or \
        (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False

# Function to check for a tie
def is_tie():
    if ' ' not in board:
        return True
    else:
        return False

# Main game loop
while True:
    print_board()
    player_move('X')
    print_board()
    if is_victory('X'):
        print("Player 1 wins! Congratulations!")
        break
    elif is_tie():
        print("It's a tie!")
        break
    player_move('O')
    if is_victory('O'):
        print_board()
        print("Player 2 wins! Congratulations!")
        break