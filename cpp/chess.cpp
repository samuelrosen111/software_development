#include <iostream>
#include <string>

// Define the Piece class
class Piece {
private:
    std::string name; // Attribute to store the name of the piece

public:
    // Constructor to initialize the Piece with a name
    Piece(std::string n) : name(n) {}

    // Method to print the Piece's information
    void print() const {
        std::cout << "Piece Name: " << name << std::endl;
    }
};




// Main function
int main() {
    Piece myPiece("Chess King"); // Create a Piece instance with a name
    myPiece.print(); // Print the Piece's information

    return 0;
}
