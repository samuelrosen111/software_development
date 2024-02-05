# This program will implement chess. It's build on the previous version of chess.py but here we will work with classes and objects - thereby restructuring the code.

class Piece:
    def __init__(self, start_pos, end_pos, color, name, short_name):
        self.start_pos = start_pos # Tuple with row and col
        self.end_pos = end_pos # Tuple with row and col
        self.color = color
        self.name = name
        self.short_name = short_name

    def __str__(self):
        # Adjusted to use self.start_pos for row and col information
        return f"Piece(name={self.name}, short_name={self.short_name}, color={self.color}, row={self.start_pos[0]}, col={self.start_pos[1]})"

class Chess:
    def __init__(self):
        self.board = self.create_board()
        self.turn = 'white'
        self.moves = 0

    def create_board(self):
        # Create an 8x8 matrix with None values
        board = [[None for _ in range(8)] for _ in range(8)]

        # Set up white pieces
        for i in range(8):
            board[1][i] = Piece((1, i), None, "white", "pawn", "w_P")
        piece_order = ["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook"]
        for i, piece_name in enumerate(piece_order):
            board[0][i] = Piece((0, i), None, "white", piece_name, "w_" + piece_name[0].upper())

        # Set up black pieces
        for i in range(8):
            board[6][i] = Piece((6, i), None, "black", "pawn", "b_P")
        for i, piece_name in enumerate(piece_order):
            board[7][i] = Piece((7, i), None, "black", piece_name, "b_" + piece_name[0].upper())

        return board
    
    def printBoard(self):
        board = self.board
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

    def move_input_is_invalid(self, from_square, to_square):
        # Is input in correct format?
        if(len(from_square) != 2 or len(to_square) != 2):
            print("Invalid input. Please enter the move in the correct format")
            return True

        valid_leters_array = ["a", "b", "c", "d", "e", "f", "g", "h"]
        valid_numbers_array = ["1", "2", "3", "4", "5", "6", "7", "8"]

        # Check that Letters (columns) are in the correct format, allow also for upper case letters
        letter_from_square = from_square[0]
        letter_to_square = to_square[0]
        if(letter_from_square.lower() not in valid_leters_array or letter_to_square.lower() not in valid_leters_array):
            print("Invalid input. Please enter the move in the correct format")
            return True

        number_from_square = from_square[1]
        number_to_square = to_square[1]
        if(number_from_square not in valid_numbers_array or number_to_square not in valid_numbers_array):
            print("Invalid input. Please enter the move in the correct format")
            return True
        return False
    
    def move_is_invalid(self, from_tuple, to_tuple):
        # Check if the move is invalid. This function will not check specific piece moves, only if the move is valid in general.
        board = self.board
        from_piece = board[from_tuple[0]][from_tuple[1]]
        to_piece = board[to_tuple[0]][to_tuple[1]]
        if(from_piece is None):
            print("There is no piece in the square you want to move from")
            return True
        if(from_piece.color != self.turn):
            print("It's not your turn")
            return True
        if(to_piece is not None and to_piece.color == self.turn):
            print("You can't move to a square with your own piece")
            return True
        return False
    
        
        
    def move(self):
        def transform_input_to_indices(square):
            # Transform the input to row and col indices
            col = ord(square[0].lower()) - 97
            row = int(square[1]) - 1
            return (row, col)

        while True:
            print("Format of move should be 'letter(column)' + 'number(row)' eg E2")
            from_square = input("Enter the square you want to move from: ")
            to_square = input("Enter the square you want to move to: ")
            if(self.move_input_is_invalid(from_square, to_square)): # No need to pass "self" as an argument - since we are already inside the class it is alrready implied.
                continue
            # Now we know the input is valid in format, we can transform it to indices
            from_tuple = transform_input_to_indices(from_square)
            to_tuple = transform_input_to_indices(to_square)
            if(self.move_is_invalid(from_tuple, to_tuple)):
                continue
            else:
                break

        # Given move is correct, now we can move the piece
        board = self.board
        hold_piece = board[from_tuple[0]][from_tuple[1]]
        board[from_tuple[0]][from_tuple[1]] = None
        board[to_tuple[0]][to_tuple[1]] = hold_piece
        
        # Move completed, change turn
        self.turn = "black" if self.turn == "white" else "white"
        


def main():
    chess = Chess()
    chess.printBoard()
    while True:
        chess.move()
        chess.printBoard()


# Calls the main function, also checks if the file is being run directly
if __name__ == "__main__":
    main()