game_board_display = [[' ', ' 1 ', ' ', ' 2 ', ' ', ' 3 '],
                      ['1', '   ', '|', '   ', '|', '   '],
                      [' ', '--', '--', '--', '--', '---', ],
                      ['2', '   ', '|', '   ', '|', '   '],
                      [' ', '--', '--', '--', '--', '---', ],
                      ['3', '   ', '|', '   ', '|', '   ']]

map_of_moves = {
    '1': '1',
    '2': '3',
    '3': '5'
}

winning_sets = [{'11', '12', '13'}, {'21', '22', '23'}, {'31', '32', '33'},
                {'11', '21', '31'}, {'12', '22', '32'}, {'13', '23', '33'},
                {'11', '22', '33'}, {'13', '22', '31'}]

players_moves = {'x': set(),
                 'o': set()}


def check_if_correct_move(row, col):
    """Return True if user input was correct. First move is not duplicated, second values of coordinates are within
    board dimension"""
    user_key = str(row) + str(col)
    correct_move = map_of_moves.keys()

    cond1 = user_key not in players_moves['x']
    cond2 = user_key not in players_moves['o']
    cond3 = row in correct_move
    cond4 = col in correct_move

    return cond1 and cond2 and cond3 and cond4


def check_winner():
    """Check is players moves are in winning sets. If so, return winning player. Otherwise, return 0"""
    for win in winning_sets:
        if win.issubset(players_moves['x']):
            return 'x'
        elif win.issubset(players_moves['o']):
            return 'o'
    return 0


def draw_board():
    """Draw boards in the console for players"""
    for i in range(len(game_board_display)):
        print("".join(game_board_display[i]))


def player_input():
    """Check the player input. If there is error repeat process"""
    while True:  # Loop the block until user put correct input
        row = input("Type numer of row: ")
        col = input("Type numer of column: ")
        if check_if_correct_move(row, col):  # If correct break the loop
            break
        else:  # If not correct try again
            print("Wrong move. Try again")
    return row, col


def main():
    """Main body of the program"""
    game_on = True
    whose_turn = 'o'
    number_of_moves = 0

    while game_on and number_of_moves < 9:
        draw_board()
        print(f"It's turn for player '{whose_turn}'.")

        # Handle player input. Monitor errors
        row, col = player_input()

        # Save player move
        players_moves[whose_turn].add(row + col)
        number_of_moves += 1

        # Handle display
        row = map_of_moves[row]
        col = map_of_moves[col]
        game_board_display[int(row)][int(col)] = f' {whose_turn} '

        # Check if there is winning move
        winner = check_winner()
        if winner != 0:  # We have a winner!
            print(f"Winner is '{winner}'\nGame over!")
            draw_board()
            game_on = False
        else:  # Game is ON
            # Flip turns
            if whose_turn == 'o':
                whose_turn = 'x'
            else:
                whose_turn = 'o'

        # Check if there are any moves available. If not call 'draw'
        if number_of_moves == 9:
            draw_board()
            game_on = False
            print("This is a draw. No winner here")


if __name__ == '__main__':
    main()
