# Create Piece clas

#Create a global variable "player_to_move" to keep track of whose turn it is
player_to_move = "white"

class Piece:
    def __init__(self, row, col, color, name, short_name):
        self.row = row  # Stores the row position of the piece
        self.col = col  # Stores the column position of the piece
        self.color = color
        self.name = name
        self.short_name = short_name

    # Add get color function
    def get_color(self):
        return self.color

    def __str__(self):
        return f"Piece(name={self.name}, short_name={self.short_name}, color={self.color}, row={self.row}, col={self.col})"

def createBoard():
    # Create an 8x8 matrix with none values
    board = [[None for _ in range(8)] for _ in range(8)]

    for i in range(8):
        board[1][i] = Piece(1, i, "white", "pawn", "w_P")
    board[0][0] = Piece(0, 0, "white", "rook", "w_R")
    board[0][1] = Piece(0, 1, "white", "knight", "w_N")
    board[0][2] = Piece(0, 2, "white", "bishop", "w_B")
    board[0][3] = Piece(0, 3, "white", "queen", "w_Q")
    board[0][4] = Piece(0, 4, "white", "king", "w_K")
    board[0][5] = Piece(0, 5, "white", "bishop", "w_B")
    board[0][6] = Piece(0, 6, "white", "knight", "w_N")
    board[0][7] = Piece(0, 7, "white", "rook", "w_R")

    for i in range(8):
        board[6][i] = Piece(6, i, "black", "pawn", "b_P")
    board[7][0] = Piece(7, 0, "black", "rook", "b_R")
    board[7][1] = Piece(7, 1, "black", "knight", "b_N")
    board[7][2] = Piece(7, 2, "black", "bishop", "b_B")
    board[7][3] = Piece(7, 3, "black", "queen", "b_Q")
    board[7][4] = Piece(7, 4, "black", "king", "b_K")
    board[7][5] = Piece(7, 5, "black", "bishop", "b_B")
    board[7][6] = Piece(7, 6, "black", "knight", "b_N")
    board[7][7] = Piece(7, 7, "black", "rook", "b_R")

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


def special_moves(board, row_position, col_position, row_target, col_target, player_to_move, board_history):
    # Existing code for special moves like castling and pawn promotion...
    
    current_move = (row_position, col_position, row_target, col_target)
    special_move_has_been_made = False

    delta_row = row_target - row_position
    delta_col = col_target - col_position

    # WHITE Pawn promotion
    if board[row_position][col_position].color == "white" and row_target == 7 and board[row_position][col_position].name == "pawn":
        special_move_has_been_made = True
        while True:
            promotion_piece = input("What piece do you want to promote to? (Queen, Rook, Bishop, Knight): ")
            if promotion_piece.lower() not in ["queen", "rook", "bishop", "knight"]:
                print("Incorrect input, please try again. Input should be Queen, Rook, Bishop or Knight")
                continue
            else:
                break
        if promotion_piece.lower() == "queen":
            board[row_position][col_position] = Piece(row_position, col_position, "white", "queen", "w_Q")
        elif promotion_piece.lower() == "rook":
            board[row_position][col_position] = Piece(row_position, col_position, "white", "rook", "w_R")
        elif promotion_piece.lower() == "bishop":
            board[row_position][col_position] = Piece(row_position, col_position, "white", "bishop", "w_B")
        elif promotion_piece.lower() == "knight":
            board[row_position][col_position] = Piece(row_position, col_position, "white", "knight", "w_N")

    # BLACK Pawn promotion
    elif board[row_position][col_position].color == "black" and row_target == 0 and board[row_position][col_position].name == "pawn":
        special_move_has_been_made = True
        while True:
            promotion_piece = input("What piece do you want to promote to? (Queen, Rook, Bishop, Knight): ")
            if promotion_piece.lower() not in ["queen", "rook", "bishop", "knight"]:
                print("Incorrect input, please try again. Input should be Queen, Rook, Bishop or Knight")
                continue
            else:
                break
        if promotion_piece.lower() == "queen":
            board[row_position][col_position] = Piece(row_position, col_position, "black", "queen", "b_Q")
        elif promotion_piece.lower() == "rook":
            board[row_position][col_position] = Piece(row_position, col_position, "black", "rook", "b_R")
        elif promotion_piece.lower() == "bishop":
            board[row_position][col_position] = Piece(row_position, col_position, "black", "bishop", "b_B")
        elif promotion_piece.lower() == "knight":
            board[row_position][col_position] = Piece(row_position, col_position, "black", "knight", "b_N")

    # Castling and other special moves logic continues unchanged...

    return board, special_move_has_been_made

def enPassant(board, row_position, col_position, row_target, col_target, player_to_move, board_history):
    # Initialize a flag to track if en passant capture occurred
    en_passant_capture = False

    # Check if it's the pawn's first move (from its initial position)
    if player_to_move == "white" and row_position == 1 and row_target == 3:
        # For white pawn, moving from row 1 to row 3 indicates a two-square move
        two_square_move = True
    elif player_to_move == "black" and row_position == 6 and row_target == 4:
        # For black pawn, moving from row 6 to row 4 indicates a two-square move
        two_square_move = True
    else:
        two_square_move = False

    # Only proceed if it was a two-square move
    if two_square_move:
        # Check for adjacent enemy pawns that could potentially capture en passant
        pawns_to_left = col_position > 0 and board[row_position][col_position - 1] is not None
        pawns_to_right = col_position < 7 and board[row_position][col_position + 1] is not None

        # If there's a pawn to the left/right, check if it belongs to the opposing player
        if pawns_to_left and board[row_position][col_position - 1].color != player_to_move:
            pawns_to_left = board[row_position][col_position - 1].name == "pawn"
        else:
            pawns_to_left = False

        if pawns_to_right and board[row_position][col_position + 1].color != player_to_move:
            pawns_to_right = board[row_position][col_position + 1].name == "pawn"
        else:
            pawns_to_right = False

        # If there are eligible pawns for en passant, ask the player which one to capture
        if pawns_to_left or pawns_to_right:
            print("En passant capture is available.")
            if pawns_to_left:
                print("Enter 'l' to capture the pawn to the left.")
            if pawns_to_right:
                print("Enter 'r' to capture the pawn to the right.")
            choice = input("Your choice (anything else to skip): ")

            # Execute the en passant capture based on the player's choice
            if choice == 'l' and pawns_to_left:
                # Remove the captured pawn and move the capturing pawn
                board[row_position][col_position - 1] = None
                board[row_position][col_position] = None
                board[row_target][col_target] = Piece(row_target, col_target, player_to_move, "pawn", player_to_move[0] + "_P")
                en_passant_capture = True
            elif choice == 'r' and pawns_to_right:
                # Remove the captured pawn and move the capturing pawn
                board[row_position][col_position + 1] = None
                board[row_position][col_position] = None
                board[row_target][col_target] = Piece(row_target, col_target, player_to_move, "pawn", player_to_move[0] + "_P")
                en_passant_capture = True

    # Return the board and whether an en passant capture occurred
    return board, en_passant_capture


def movePiece(board, player_to_move, board_history):

    def wrongInput(input_str):
        if len(input_str) != 2:
            print("Incorrect input length, please try again. Input should be A1 to H8")
            return True
        letter, number = input_str[0].upper(), input_str[1]
        if letter in 'ABCDEFGH' and number in '12345678':
            return False
        else:
            print("Incorrect input, please try again. Input should be A1 to H8")
            return True

    def convertLetterToIndex(letter):
        return 'ABCDEFGH'.index(letter.upper())

    while True:
        squareToMove = input("Enter the piece you want to move (example: E2 to move king's pawn): ")
        if wrongInput(squareToMove):
            continue
        targetSquare = input("Enter the square you want to move the piece to (example: E4): ")
        if wrongInput(targetSquare):
            continue

        # Convert input into separate row and col attributes, correctly mapping the user's input to the board's internal representation
        row_position = -1 + int(squareToMove[1]) 
        col_position = convertLetterToIndex(squareToMove[0])
        row_target = -1 + int(targetSquare[1])
        col_target = convertLetterToIndex(targetSquare[0])

        board, enPassant_performance = enPassant(board, row_position, col_position, row_target, col_target, player_to_move, board_history)
        if(enPassant_performance):
            return board

        board, special_move_has_been_made = special_moves(board, row_position, col_position, row_target, col_target, player_to_move, board_history)
        if(special_move_has_been_made):
            return board

        if(board[row_position][col_position] is None):
            print("There is no piece at the starting square. Please try again.")
            continue

        if(player_to_move != board[row_position][col_position].color):
            print("You cannot move your opponent's piece. Please try again.")
            continue

        if(row_position == row_target and col_position == col_target):
            print("You cannot move a piece to the same square. Please try again.")
            continue

        # Check if the starting square is empty
        if board[row_position][col_position] is None:
            print("There is no piece at the starting square. Please try again.")
            continue
        if(move_is_not_legal(board, row_position, col_position, row_target, col_target, player_to_move, board_history)):
            print("That is not a legal move (see reason above). Please try again.")
            continue
        # Move the piece
        
        board[row_target][col_target] = board[row_position][col_position]
        board[row_position][col_position] = None
        return board

def move_is_not_legal(board, row_position, col_position, row_target, col_target, player_to_move, board_history):
    # AUXILLIARY functions used to check moves for each piece

    def rook_move_is_illegal(board, row_position, col_position, row_target, col_target, player_to_move):
        # Check if the move is horizontal or vertical
            if not (row_position == row_target or col_position == col_target):
                error_msg = "The rook can only move horizontally or vertically."
                return True, error_msg
            # If rook moves, check if there are any pieces in between
            if(row_position == row_target):
                # Check if there are any pieces in between
                if(col_position < col_target):
                    for i in range(col_position + 1, col_target):
                        if(board[row_position][i] is not None):
                            error_msg = "There is a piece in between the rook and the target square."
                            return True, error_msg
                else:
                    for i in range(col_target + 1, col_position):
                        if(board[row_position][i] is not None):
                            error_msg = "There is a piece in between the rook and the target square."
                            return True, error_msg
            # Check that rook is moving vertically
            else:
                # Check if there are any pieces in between
                if(row_position < row_target):
                    for i in range(row_position + 1, row_target):
                        if(board[i][col_position] is not None):
                            error_msg = "There is a piece in between the rook and the target square."
                            return True, error_msg
                else:
                    for i in range(row_target + 1, row_position):
                        if(board[i][col_position] is not None):
                            error_msg = "There is a piece in between the rook and the target square."
                            return True, error_msg
            return False, "Legal Move"

    def knight_move_is_illegal(board, row_position, col_position, row_target, col_target, player_to_move):
        # Check if the move is L-shaped
        if not ((abs(row_position - row_target) == 2 and abs(col_position - col_target) == 1) or (abs(row_position - row_target) == 1 and abs(col_position - col_target) == 2)):
            message = "The knight can only move in an L-shape."
            return True, message
        return False, "Legal Move"

    def bishop_move_is_illegal(board, row_position, col_position, row_target, col_target, player_to_move):
        delta_row = row_target - row_position
        delta_col = col_target - col_position
        # Check if the move is diagonal
        if not (abs(delta_row) == abs(delta_col)):
            message = "The bishop can only move diagonally."
            return True, message
        # Given diagonal move check if there are any pieces in between
        if(delta_row > 0 and delta_col > 0):
            for i in range(1, delta_row):
                if(board[row_position + i][col_position + i] is not None):
                    message = "There is a piece in between the bishop and the target square."
                    return True, message
        elif(delta_row > 0 and delta_col < 0):
            for i in range(1, delta_row):
                if(board[row_position + i][col_position - i] is not None):
                    message = "There is a piece in between the bishop and the target square."
                    return True, message
        elif(delta_row < 0 and delta_col > 0):
            for i in range(1, abs(delta_row)):
                if(board[row_position - i][col_position + i] is not None):
                    message = "There is a piece in between the bishop and the target square."
                    return True, message
        else:
            for i in range(1, abs(delta_row)):
                if(board[row_position - i][col_position - i] is not None):
                    message = "There is a piece in between the bishop and the target square."
                    return True, message
        return False, "Legal Move"

    def queen_move_is_illegal(board, row_position, col_position, row_target, col_target, player_to_move):
        # Begin by checking if move is like a rook, bishop or none of the above
        delta_row = row_target - row_position
        delta_col = col_target - col_position
        # Check if the move is diagonal
        if (abs(delta_row) == abs(delta_col)): 
            # Given a diagonal move use the bishop function to check if there are any pieces in between
            is_illegal, msg = bishop_move_is_illegal(board, row_position, col_position, row_target, col_target, player_to_move)
            #Edit message to be for queen, not bishop
            msg = msg.replace("bishop", "queen")
            return is_illegal, msg
        # Check if the move is horizontal or vertical (rook)
        elif (row_position == row_target or col_position == col_target):
            # Queen now moves like a rook, use the rook function to check if there are any pieces in between
            is_illegal, msg = rook_move_is_illegal(board, row_position, col_position, row_target, col_target, player_to_move)
            #Edit message to be for queen, not rook
            msg = msg.replace("rook", "queen")
            return is_illegal, msg
        else:
            message = "The queen can only move diagonally, horizontally or vertically."
            return True, message
        return False, "Legal Move"

    def king_move_is_illegal(board, row_position, col_position, row_target, col_target, player_to_move):
        delta_row = row_target - row_position
        delta_col = col_target - col_position
        # Check that the move is only one square in any direction
        if not (abs(delta_row) <= 1 and abs(delta_col) <= 1):
            message = "The king can only move one square in any direction."
            return True, message
        return False, "Legal Move"

    def pawn_move_is_illegal(board, row_position, col_position, row_target, col_target, player_to_move):
        delta_row = row_target - row_position
        delta_col = col_target - col_position
        #Implements en passant for wite pawn
        # White pawn
        if(player_to_move == "white"):
            # Side capture is always legal
            if(abs(delta_col) == 1 and delta_row == 1 and board[row_target][col_target].color == "black"):
                return False, "Legal Move"
            # If pawn is in starting position it can move two squares forward or one square forward
            if(delta_col==0 and delta_row==2 or delta_col==0 and delta_row==1):
                return False, "Legal Move"
            # If pawn is not in starting position it can only move one square forward
            if(delta_col==0 and delta_row==1):
                return False, "Legal Move"
            else:
                message = "The pawn can only move one square forward, two squares forward from starting position or one square diagonally to capture."
                return True, message
            # We will ignore en-passant for now
            #TODO: Implement en-passant
        # Black pawn
        else:
            # Side capture is always legal
            if(abs(delta_col) == 1 and delta_row == -1 and board[row_target][col_target].color == "white"):
                return False, "Legal Move"
            # If pawn is in starting position it can move two squares forward or one square forward
            #Check if pawn is in starting position
            
            if(delta_col==0 and delta_row==-2 or delta_col==0 and delta_row==-1):
                return False, "Legal Move"
            # If pawn is not in starting position it can only move one square forward
            if(delta_col==0 and delta_row==-1):
                return False, "Legal Move"
            else:
                message = "The pawn can only move one square forward, two squares forward from starting position or one square diagonally to capture."
                return True, message
            # We will ignore en-passant for now


    # There are already some checks in place from the movePiece function, they are: 
    # 1) The starting square is not empty
    # 2) The target square is not the same as the starting square
    # 3) The starting square contains a piece of the player's color
    change_in_row = row_target - row_position # Auxiliary variables to check if the move is horizontal, vertical or diagonal
    change_in_col = col_target - col_position # Auxiliary variables to check if the move is horizontal, vertical or diagonal

    piece_to_move = board[row_position][col_position]
    # Basic checks:
    # Check if target square is occupied by a piece of the same color
    if(board[row_target][col_target] is not None):
        if board[row_target][col_target].get_color() == piece_to_move.get_color():
            print("The target square is occupied by a piece of the same color.")
            return True # Illegal move
    
    # ROOK ------------------------------------------------------------------------------------------------------------------------
    if(piece_to_move.name == "rook"):
        is_illegal, msg = rook_move_is_illegal(board, row_position, col_position, row_target, col_target, player_to_move)
        if(is_illegal):
            print(msg)
            return True
    # KNIGHT ------------------------------------------------------------------------------------------------------------------------
    elif(piece_to_move.name == "knight"):
        is_illegal, msg = knight_move_is_illegal(board, row_position, col_position, row_target, col_target, player_to_move)
        if(is_illegal):
            print(msg)
            return True
    # BISHOP ------------------------------------------------------------------------------------------------------------------------
    elif(piece_to_move.name == "bishop"):
        # Uses the auxiliary variables to check if the move is diagonal
        is_illegal, msg = bishop_move_is_illegal(board, row_position, col_position, row_target, col_target, player_to_move)
        if(is_illegal):
            print(msg)
            return True

    # QUEEN ------------------------------------------------------------------------------------------------------------------------
    elif(piece_to_move.name == "queen"):
        # Basic check to see if move is diagonal, horizontal or vertical
        is_illegal, msg = queen_move_is_illegal(board, row_position, col_position, row_target, col_target, player_to_move)
        if(is_illegal):
            print(msg)
            return True
    # KING ------------------------------------------------------------------------------------------------------------------------
    elif(piece_to_move.name == "king"):
        # Check if the move is only one square in any direction
        is_illegal, msg = king_move_is_illegal(board, row_position, col_position, row_target, col_target, player_to_move)
        if(is_illegal):
            print(msg)
            return True
    # PAWN ------------------------------------------------------------------------------------------------------------------------
    elif(piece_to_move.name == "pawn"):
        # Check if the move is only one square in any direction
        is_illegal, msg = pawn_move_is_illegal(board, row_position, col_position, row_target, col_target, player_to_move)
        if(is_illegal):
            print(msg)
            return True
    # If none of the above checks are triggered the move is legal
    else:
        print("The piece you are trying to move is not a legal chess piece. This error message should not appear - if it does the program has an error to it.")
        return True
        
    
    return False # If all checks are passed it is a legal move




    print("Not implemented yet")


def main():
    player_to_move = "white"
    # Create the initial chessboard
    board = createBoard()
    printBoard(board)
    board_history = [] # Create a list to store the board history to enable en-passant, castling, pawn promotion, 3 move repetition and 50 move rule

    # Start the game loop for moving pieces
    while True:
        print("It is " + player_to_move + "'s turn to move.")

        board = movePiece(board, player_to_move, board_history)
        printBoard(board)
        board_history.append(board)


        if(player_to_move == "white"):
            player_to_move = "black"
        else:
            player_to_move = "white"

# Run the main function only if this file is the main file (not imported)
if __name__ == "__main__":
    main()


# Additional core functionality to implement:

#TODO: Implement board history to enable en-passant, castling, pawn promotion, 3 move repetition and 50 move rule
#TODO: Search for check and checkmate
#DONE: Implement castling
# --> TODO: look for checkmate when castling
#TODO: Implement en-passant
#DONE: Implement pawn promotion
# --> TODO: look for checkmate when pawn promotion
#TODO: Implement stalemate
#TODO: Implement draw by 3 move repetition
#TODO: Implement draw by 50 move rule
#TODO: Implement draw by insufficient material
#TODO: Implement draw by agreement (At each turn a player can offer a draw to their opponent. If the opponent accepts the game ends in a draw. Else the game continues.)
#TODO: Add option to resign by typing "resign" at any time 
    

# Extra features to implement:
#TODO: Implement GUI