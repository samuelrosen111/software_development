#print("This program will implement the game of chess.")

# Create Piece class
class Piece:
    def __init__(self, row, column, color, name, short_name):
        self.row = row
        self.column = column
        self.color = color
        self.name = name
        self.short_name = short_name

    def __str__(self):
        return f"Piece(name={self.name}, short_name={self.short_name}, color={self.color}, row={self.row}, column={self.column})"


def main():
    #Create one example piece
    piece = Piece(1, 1, "white", "pawn", "P")
    print(piece)


# Run main function checking if this file is the main file and not an imported file. Also this is a good practice because it allows you to import this file into another file without running the main function.
if __name__ == "__main__":
    main()