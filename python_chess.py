class Piece:
    def __init__(self, row_current, col_current, row_target, col_target, color, piece_type, text_symbol):
        self.row_current = row_current
        self.col_current = col_current
        self.row_target = row_target
        self.col_target = col_target
        self.color = color  # 'white' or 'black'
        self.piece_type = piece_type  # e.g., 'pawn', 'rook', etc.
        self.text_symbol = text_symbol


def create_board():
    board = [[None for _ in range(8)] for _ in range(8)]

    # White pieces
    pieces_order = [('rook', 'w_r'), ('knight', 'w_n'), ('bishop', 'w_b'), ('queen', 'w_q'),
                    ('king', 'w_k'), ('bishop', 'w_b'), ('knight', 'w_n'), ('rook', 'w_r')]

    for col, (piece_type, text_symbol) in enumerate(pieces_order):
        board[0][col] = Piece(0, col, None, None, 'white', piece_type, text_symbol)

    # Populate the second row with white pawns
    for col in range(8):
        board[1][col] = Piece(1, col, None, None, 'white', 'pawn', 'w_p')

    
        # Black pieces
    black_pieces_order = [('rook', 'b_r'), ('knight', 'b_n'), ('bishop', 'b_b'), ('queen', 'b_q'),
                        ('king', 'b_k'), ('bishop', 'b_b'), ('knight', 'b_n'), ('rook', 'b_r')]

    for col, (piece_type, text_symbol) in enumerate(black_pieces_order):
        board[7][col] = Piece(7, col, None, None, 'black', piece_type, text_symbol)

    # Populate the 7th row with black pawns
    for col in range(8):
        board[6][col] = Piece(6, col, None, None, 'black', 'pawn', 'b_p')

    return board


def print_board(board):
    # Define grid characters
    horizontal_line = '—'  # A dash character for horizontal lines
    vertical_line = '|'
    corner = '+'

    # Print the column labels (a-h)
    print("  ", end="")  # Initial spacing for row numbers
    for col in range(8):
        print("   " + chr(97 + col) + "  ", end="")  # 97 is the ASCII code for 'a'
    print()

    # Print the top border of the board
    print("  " + corner + (horizontal_line * 5 + corner) * 8)

    # Print the board with grid lines
    for row in range(8):
        # Print the row label (1-8)
        print(str(row + 1) + " " + vertical_line, end="")

        # Print each piece in the row enclosed in a grid
        for col in range(8):
            piece = board[row][col]
            symbol = piece.text_symbol if piece else "   "  # Three spaces for empty cells
            print(" " + symbol + " " + vertical_line, end="")

        print()  # Newline after each row

        # Print a horizontal grid line after each row
        if row < 7:  # Avoid printing an extra line at the bottom
            print("  " + corner + (horizontal_line * 5 + corner) * 8)

    # Print the bottom border of the board
    print("  " + corner + (horizontal_line * 5 + corner) * 8)


def main():
    board = create_board()
    print_board(board)

main()