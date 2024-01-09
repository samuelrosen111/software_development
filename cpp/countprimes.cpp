#include <iostream>
#include <limits>
#include <cmath>
#include <iomanip>


int upperLimit() {
    int upperLimit;
    while (true) {
        std::cout << "Enter upper limit: ";
        if (!(std::cin >> upperLimit) || upperLimit <= 2) {
            std::cout << "Invalid input. Please enter a positive integer greater than 2." << std::endl;
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        } else {
            break;
        }
    }

    return upperLimit;
}

void printProgressBar(double percentage, int lastPrimeNumber) {
    int barWidth = 70; // Width of the progress bar

    //std::cout << "Latest added prime: " << lastPrimeNumber;
    //std::cout << " | Progress: ";

    std::cout << "[";
    int pos = barWidth * percentage / 100;
    for (int i = 0; i < barWidth; ++i) {
        if (i < pos) std::cout << "=";
        else if (i == pos) std::cout << ">";
        else std::cout << " ";
    }
    std::cout << "] " << std::setw(3) << static_cast<int>(percentage) << "%\r";
    std::cout << "Latest prime = " << static_cast<int>(lastPrimeNumber) << "  "; 
    std::cout.flush();
}


int main() {
    std::cout << "This program will count the number of prime numbers between 2 and the upper limit you enter." << std::endl;
    std::cout << "-----------------------------------------------------------------------------------------------" << std::endl;
    int limit = upperLimit();
    int* dynamicPrimeArray = new int[2];
    int lengthArray = 2;
    dynamicPrimeArray[0] = 2;
    dynamicPrimeArray[1] = 3;
    int currentNumber = 5;
    bool isPrime = true;

    while(currentNumber <= limit) {
        isPrime = true;
        for (int i = 0; i < lengthArray; i++) {
            if (currentNumber % dynamicPrimeArray[i] == 0) {
                isPrime = false;
                break;
            }
        }
        if(isPrime){
            dynamicPrimeArray[lengthArray] = currentNumber;
            lengthArray++;
            // Update the progress bar only when a certain percentage is reached
            double percentage = static_cast<double>(currentNumber) / limit * 100;
            printProgressBar(percentage, dynamicPrimeArray[lengthArray-1]);
        }
        currentNumber = currentNumber + 2;
    }
    std::cout << "There are " << lengthArray << " prime numbers between 2 and " << limit << "." << std::endl;
    std::cout << "The prime numbers are: ";
    for(int i = 0; i < lengthArray; i++) {
        if (dynamicPrimeArray[i] != 0) {
            std::cout << dynamicPrimeArray[i] << " ";
            //add newline for each number:
            std::cout << std::endl;
        }
    }

}
