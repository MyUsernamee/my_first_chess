import chess
import tqdm

board = chess.Board()

print(board)

print(board.legal_moves)

def add_move(output: str, board: chess.Board, move, tabs=0, depth=4):

    # Copy the board
    new_board = board.copy()

    # Make the move
    new_board.push(move)

    board_string = str(new_board).replace("\n", "\\n")

    # Add the board to the output
    output += "\t"* tabs + "if move == \"" + move.uci() + "\":\n"
    output += "\t"* tabs + "\t" + "print(\"" + board_string + "\")\n"

    if board.is_checkmate():
        output += "\t"* tabs + "\t" + "print(\"Checkmate\")\n"
        output += "\t"* tabs + "\t" + "exit()\n"
        return output

    output = new_turn(output, new_board, tabs+1)

    for move in new_board.legal_moves:

        if depth == 1:
            output += "\t"* tabs + "\t" + "print(\"Sorry, I can't go any deeper\")\n"
            output += "\t"* tabs + "\t" + "exit()\n"
            break

        
        output = add_move(output, new_board, move, tabs+1, depth-1)

    return output

def new_turn(output: str, board: chess.Board, tabs=0):

    # Add the board to the output
    tabs_string = "\t"* tabs
    output += tabs_string + "print(\"" + str(board).replace("\n", "\\n") + "\")\n"
    output += tabs_string + "print(\"" + ("White's " if board.turn == chess.WHITE else "Black's ") + " turn\")\n"
    output += tabs_string + "move = input(\"Enter your move: \")\n"

    return output

output = ""

for position in range(0, 1):
    output = new_turn(output, board)

    for move in tqdm.tqdm(board.legal_moves):
        output = add_move(output, board, move, 0, 4)

#Save the output to a python file
with open("game.py", "w") as file:
    file.write(output)
