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
            print("move_input_is_invalid -- Please enter the move in the correct format")
            return True

        valid_leters_array = ["a", "b", "c", "d", "e", "f", "g", "h"]
        valid_numbers_array = ["1", "2", "3", "4", "5", "6", "7", "8"]

        # Check that Letters (columns) are in the correct format, allow also for upper case letters
        letter_from_square = from_square[0]
        letter_to_square = to_square[0]
        if(letter_from_square.lower() not in valid_leters_array or letter_to_square.lower() not in valid_leters_array):
            print("move_input_is_invalid -- Please enter the move in the correct format")
            return True

        number_from_square = from_square[1]
        number_to_square = to_square[1]
        if(number_from_square not in valid_numbers_array or number_to_square not in valid_numbers_array):
            print("move_input_is_invalid -- Please enter the move in the correct format")
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
        if(from_tuple == to_tuple):
            print("You have to move the piece")
            return True

        return False
    
    def specific_piece_move_invalid(self, from_tuple, to_tuple):
        # Auxiliary variables
        delta_row = to_tuple[0] - from_tuple[0]
        delta_col = to_tuple[1] - from_tuple[1]
        piece_to_move = self.board[from_tuple[0]][from_tuple[1]]
        target_square = self.board[to_tuple[0]][to_tuple[1]]
        from_row = from_tuple[0]
        to_row = to_tuple[0]
        from_col = from_tuple[1]
        from_col = to_tuple[1]

        # Note: index in the board can be hrd to keep track of. Remember that:
        # [0][0] = A8
        # [7][7] = H1
        # [0][7] = H8
        # [7][0] = A1

        # ROOK ---------------------------------------------------------------------------------------------------

        def check_rook_move():
            # Rook can move in a straight line, either horizontally or vertically.
            if(delta_row == 0 or delta_col == 0):
                # Check that no piece is blocking the way
                if(delta_row == 0):
                    # Moving horizontally
                    for i in range(min(from_tuple[1], to_tuple[1]) + 1, max(from_tuple[1], to_tuple[1])):
                        if(self.board[from_tuple[0]][i] is not None):
                            print("Rook can't jump over pieces")
                            return True
                else:
                    # Moving vertically
                    for i in range(min(from_tuple[0], to_tuple[0]) + 1, max(from_tuple[0], to_tuple[0])):
                        if(self.board[i][from_tuple[1]] is not None):
                            print("Rook can't jump over pieces")
                            return True
            return False
        
        # KNIGHT ---------------------------------------------------------------------------------------------------

        def check_knight_move():
            # Knight can move in an L-shape, 2 squares in one direction and 1 square in the other direction
            if(abs(delta_row) == 2 and abs(delta_col) == 1):
                return False
            if(abs(delta_row) == 1 and abs(delta_col) == 2):
                return False
            print("Knight can't move like that, it must move in an L-shape")
            return True
        
        # BISHOP ---------------------------------------------------------------------------------------------------

        def check_bishop_move():
            # Bishop can move diagonally
            if(abs(delta_row) == abs(delta_col)):
                # Check if we move south-east
                if(delta_row > 0 and delta_col > 0):
                    for i in range(1, delta_row):
                        if(self.board[from_tuple[0] + i][from_tuple[1] + i] is not None):
                            print("Bishop can't jump over pieces")
                            return True
                # Check if we move south-west
                if(delta_row > 0 and delta_col < 0):
                    for i in range(1, delta_row):
                        if(self.board[from_tuple[0] + i][from_tuple[1] - i] is not None):
                            print("Bishop can't jump over pieces")
                            return True
                # Check if we move north-east
                if(delta_row < 0 and delta_col > 0):
                    for i in range(1, abs(delta_row)):
                        if(self.board[from_tuple[0] - i][from_tuple[1] + i] is not None):
                            print("Bishop can't jump over pieces")
                            return True
                # Check if we move north-west
                if(delta_row < 0 and delta_col < 0):
                    for i in range(1, abs(delta_row)):
                        if(self.board[from_tuple[0] - i][from_tuple[1] - i] is not None):
                            print("Bishop can't jump over pieces")
                            return True
            return False
        
        # QUEEN ---------------------------------------------------------------------------------------------------

        def check_queen_move():
            # Queen can move like a rook or a bishop
            rook_invalid = check_rook_move()
            bishop_invalid = check_bishop_move()
            if(rook_invalid and bishop_invalid):
                print("Error, queen must move like rook or bishop and can't jump over pieces")
                return True
            return False

        
        # KING ---------------------------------------------------------------------------------------------------

        def check_king_move():
            # King can move one square in any direction
            if(abs(delta_row) <= 1 and abs(delta_col) <= 1):
                return False
            return True, "King can't move like that, it must move one square in any direction"

        # PAWN ---------------------------------------------------------------------------------------------------

        def check_pawn_move():
            # To make it easier this check will split into two parts, one for white and one for black
            # Note: index in the board can be hard to keep track of. Remember that:
            # [0][0] = A8
            # [7][7] = H1
            # [0][7] = H8
            # [7][0] = A1
            # Starting row black pawns: Chess board index = 6 (!!! program index [1][x]) 
            # Starting row white pawns: Chess board index = 1 (!!! program index [6][x])

            if(piece_to_move.color == "white"):
                # Sideways capture
                if(delta_row == 1 and abs(delta_col) == 1 and target_square is not None and target_square.color == "black"):
                    return False
                # Starting position
                if(from_row == 1):
                    # Moving two squares forward
                    if(delta_row == 2 and delta_col == 0 and target_square is None and self.board[from_row + 1][from_col] is None):
                        return False
                # Moving one square forward
                if(delta_row == 1 and delta_col == 0 and target_square is None):
                    return False
                return True
            else:
                # Sideways capture
                if(delta_row == -1 and abs(delta_col) == 1 and target_square is not None and target_square.color == "white"):
                    return False
                # Starting position
                if(from_row == 6):
                    # Moving two squares forward
                    if(delta_row == -2 and delta_col == 0 and target_square is None and self.board[from_row - 1][from_col] is None):
                        return False
                # Moving one square forward
                if(delta_row == -1 and delta_col == 0 and target_square is None):
                    return False
                return True
            
        # Check which piece, and then call the correct sub-function -------------------------------------------

        piece = self.board[from_tuple[0]][from_tuple[1]]
        if(piece.name == "rook"):
            return check_rook_move()
        if(piece.name == "knight"):
            return check_knight_move()
        if(piece.name == "bishop"):
            return check_bishop_move()
        if(piece.name == "queen"):
            return check_queen_move()
        if(piece.name == "king"):
            return check_king_move()
        if(piece.name == "pawn"):
            return check_pawn_move()
    

    
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

            # Adress flipped indices in the board
            #from_tuple = (from_tuple[0], 7 - from_tuple[1])
            #to_tuple = (to_tuple[0], 7 - to_tuple[1])

            if(self.move_is_invalid(from_tuple, to_tuple)):
                print("Move_is_invalid function triggered, plase make a new move.")
                continue
            


            piece_move_is_invalid = self.specific_piece_move_invalid(from_tuple, to_tuple)
            if(piece_move_is_invalid):
                print("--> Piece specific error, try again.")
                continue

            # Given move is correct, now we can move the piece
            board = self.board
            hold_piece = board[from_tuple[0]][from_tuple[1]]
            board[from_tuple[0]][from_tuple[1]] = None
            board[to_tuple[0]][to_tuple[1]] = hold_piece

            # Move completed, change turn
            if(self.turn == "white"):
                self.turn = "black"
            else:
                self.turn = "white"
            self.moves += 1
            # Move completed, break the loop
            break
        




def main():
    Chess = Chess()
    Chess.printBoard()
    while True:
        Chess.move()
        Chess.printBoard()


# Calls the main function, also checks if the file is being run directly
if __name__ == "__main__":
    main()