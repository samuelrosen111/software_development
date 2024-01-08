import tkinter as tk 
from tkinter import font as tkFont

class Piece:
    def __init__(self, row_current, col_current, row_target, col_target, color, piece_type, text_symbol):
        self.row_current = row_current
        self.col_current = col_current
        self.row_target = row_target
        self.col_target = col_target
        self.color = color  # 'white' or 'black'
        self.piece_type = piece_type  # e.g., 'pawn', 'rook', etc.
        self.text_symbol = text_symbol

class GameState:
    def __init__(self):
        self.player_to_move = True  # True for white, False for black

def create_board():
    board = [[None for _ in range(8)] for _ in range(8)]

    # Black pieces
    black_pieces_order = [('rook', 'b_r'), ('knight', 'b_n'), ('bishop', 'b_b'), ('queen', 'b_q'),
                          ('king', 'b_k'), ('bishop', 'b_b'), ('knight', 'b_n'), ('rook', 'b_r')]

    for col, (piece_type, text_symbol) in enumerate(black_pieces_order):
        board[0][col] = Piece(0, col, None, None, 'black', piece_type, text_symbol)

    # Populate the second row with black pawns
    for col in range(8):
        board[1][col] = Piece(1, col, None, None, 'black', 'pawn', 'b_p')

    # White pieces
    white_pieces_order = [('rook', 'w_r'), ('knight', 'w_n'), ('bishop', 'w_b'), ('queen', 'w_q'),
                          ('king', 'w_k'), ('bishop', 'w_b'), ('knight', 'w_n'), ('rook', 'w_r')]

    for col, (piece_type, text_symbol) in enumerate(white_pieces_order):
        board[7][col] = Piece(7, col, None, None, 'white', piece_type, text_symbol)

    # Populate the 7th row with white pawns
    for col in range(8):
        board[6][col] = Piece(6, col, None, None, 'white', 'pawn', 'w_p')

    return board


def print_board(board):
    print("\n\n")
    # Define the horizontal line and corner pieces for the grid
    horizontal_line = "-------------------------------------------------------"

    # Print the column labels 
    print("     A      B      C      D      E      F      G      H")
    print("  " + horizontal_line)

    # Print each row of the board
    for row in range(8):
        # Start with the row number (8-row for correct orientation)
        print(f"{8-row} ", end="")

        # Print each column in the row
        for col in range(8):
            print("|", end="")  # Start of the grid for each square
            piece = board[row][col]
            if piece is not None:
                if(col==7):
                    print(f" {piece.text_symbol}", end="")
                else:
                    print(f" {piece.text_symbol} ", end=" ")
            else:
                if(col==7):
                    print("    ", end="")  # Fill empty squares with five spaces
                else:
                    print("      ", end="")  # Fill empty squares with five spaces

        # End the row with a vertical line and the row number
        print(f"| {8-row}")

        # Print the horizontal divider for the grid
        print("  " + horizontal_line)

    # Print the column labels again
    print("     A      B      C      D      E      F      G      H")
    print("\n\n")


def printBoardGUI(board):
    # Create the main window
    root = tk.Tk()
    root.title("Chess Board")

    # Define the font for the pieces
    chessFont = tkFont.Font(family="Helvetica", size=14, weight="bold")

    # Create a grid of labels for the chess board
    for row in range(8):
        for col in range(8):
            # Determine background color (checkered pattern)
            bg_color = "#F0D9B5" if (row + col) % 2 == 0 else "#B58863"

            # Create a label for this square
            label = tk.Label(root, text='', bg=bg_color, font=chessFont, width=4, height=2)
            label.grid(row=row, column=col)

            # Add piece text if the square is not empty
            piece = board[row][col]
            if piece:
                label.config(text=piece.text_symbol)
                # Set text color based on the piece color
                label.config(fg='black' if piece.color == 'black' else 'white')

    # Add row and column indices
    for i in range(8):
        tk.Label(root, text=str(8-i), bg='white').grid(row=i, column=8)
        tk.Label(root, text=chr(65+i), bg='white').grid(row=8, column=i)

    # Run the GUI event loop
    root.mainloop()


def illegal_move(source_or_target, board, player_to_move):
    # Check if the move is outside the board
    if len(source_or_target) != 2 or source_or_target[0].upper() < 'A' or source_or_target[0].upper() > 'H' or source_or_target[1] < '1' or source_or_target[1] > '8':
        print("Illegal move. Please enter a valid move like 'A2'")
        return True

    # Convert chess coordinates to array indices
    col = ord(source_or_target[0].upper()) - ord('A')
    row = 8 - int(source_or_target[1])

    # Check if the source square is empty
    piece = board[row][col]
    if piece is None:
        print("There is no piece at the selected square. Please select a square with a piece.")
        return True

    # Check if the player is trying to move an opponent's piece
    if (player_to_move and piece.color != 'white') or (not player_to_move and piece.color != 'black'):
        print("Cannot move opponent's piece. Please choose one of your own pieces.")
        return True

    return False


def move_piece(board_states, game_state):
    player_to_move = game_state.player_to_move
    # Display whose turn it is
    print("White to move" if player_to_move else "Black to move")

    # Function to convert chess coordinates to array indices
    def coords_to_indices(coords):
        col = ord(coords[0].upper()) - ord('A')
        row = 8 - int(coords[1])
        return row, col

    # Prompt user for the piece to move
    source = input("Enter the piece to move (e.g., A2): ")
    if illegal_move(source, board_states[-1], player_to_move):
        return player_to_move
    
    # Prompt user for the square to move the piece to
    target = input("Enter the target square (e.g., A3): ")
    if illegal_move(target, board_states[-1], player_to_move):
        return player_to_move

    src_row, src_col = coords_to_indices(source)
    trg_row, trg_col = coords_to_indices(target)

    # Create a new board (copy of the last state)
    new_board = [[piece for piece in row] for row in board_states[-1]]

    # Move the piece
    piece = new_board[src_row][src_col]
    if piece is None or (player_to_move and piece.color != 'white') or (not player_to_move and piece.color != 'black'):
        print("Invalid move. Try again.")
        return player_to_move

    # Perform the move
    new_board[trg_row][trg_col] = piece
    new_board[src_row][src_col] = None

    # Update the piece's current position
    piece.row_current = trg_row
    piece.col_current = trg_col

    # Append new board state to the list
    board_states.append(new_board)

    # Toggle the player to move and return the new state
    game_state.player_to_move = not game_state.player_to_move


def main():
    board_states = []
    board_states.append(create_board())
    print_board(board_states[-1])
    #printBoardGUI(board_states[-1])
    game_state = GameState()

    while True:
        move_piece(board_states, game_state)
        print_board(board_states[-1])



main()