#print("This program will implement the game of chess.")

# Create Piece class
class Piece:
    def __init__(self, position, color, name, short_name):
        self.position = position # Stores the position of the piece in a tuple (row, column)
        self.color = color
        self.name = name
        self.short_name = short_name

    def __str__(self):
        return f"Piece(name={self.name}, short_name={self.short_name}, color={self.color}, row={self.row}, column={self.column})"


def createBoard():
    # Create a 8x8 matrix with none values
    board = [[None for i in range(8)] for j in range(8)]

    for i in range(8):
        board[1][i] = Piece((1, i), "white", "pawn", "w_P")
    board[0][0] = Piece((0, 0), "white", "rook", "w_R")
    board[0][1] = Piece((0, 1), "white", "knight", "w_N")
    board[0][2] = Piece((0, 2), "white", "bishop", "w_B")
    board[0][3] = Piece((0, 3), "white", "queen", "w_Q")
    board[0][4] = Piece((0, 4), "white", "king", "w_K")
    board[0][5] = Piece((0, 5), "white", "bishop", "w_B")
    board[0][6] = Piece((0, 6), "white", "knight", "w_N")
    board[0][7] = Piece((0, 7), "white", "rook", "w_R")

    for i in range(8):
        board[6][i] = Piece((6, i), "black", "pawn", "b_P")
    board[7][0] = Piece((7, 0), "black", "rook", "b_R")
    board[7][1] = Piece((7, 1), "black", "knight", "b_N")
    board[7][2] = Piece((7, 2), "black", "bishop", "b_B")
    board[7][3] = Piece((7, 3), "black", "queen", "b_Q")
    board[7][4] = Piece((7, 4), "black", "king", "b_K")
    board[7][5] = Piece((7, 5), "black", "bishop", "b_B")
    board[7][6] = Piece((7, 6), "black", "knight", "b_N")
    board[7][7] = Piece((7, 7), "black", "rook", "b_R")

    return board


def printBoard(board):
    # Define the square frame and empty square representation
    top_bottom_border = "------"
    side_border = "|"
    empty_inner = "     "  # Adjusted space for empty squares to maintain square width

    # Print the column labels with padding for alignment
    print("     " + "     ".join(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']))

    # Iterate through each row in reverse order since row 8 is at the top
    for i in range(7, -1, -1):
        # Print the top border for the row if it's the top of the board or after each row
        if i == 7 or i < 7:
            print("  " + top_bottom_border * 8)
        
        # Initialize row strings for the piece layer
        piece_layer = str(i + 1) + " "  # Start with the row number and a space for alignment

        # Iterate through each column in the row
        for j in range(8):
            # Add the left side border for each square
            if j == 0:
                piece_layer += side_border
            
            # Check if the square is occupied by a piece
            if board[i][j] is not None:
                # Center the piece's short_name within the square
                piece_layer += f" {board[i][j].short_name} "
            else:
                # Use empty inner space for empty squares
                piece_layer += empty_inner
            
            # Add the right side border for the square
            piece_layer += side_border

        # Print the piece layer for the row
        print(piece_layer + " " + str(i + 1))  # Add row number to the right as well

    # Print the final bottom border of the board
    print("  " + top_bottom_border * 8)
    # Print the column labels again for better readability
    print("     " + "     ".join(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']))



def main():
    #Create one example piece
    board = createBoard()
    printBoard(board)


# Run main function checking if this file is the main file and not an imported file. Also this is a good practice because it allows you to import this file into another file without running the main function.
if __name__ == "__main__":
    main()