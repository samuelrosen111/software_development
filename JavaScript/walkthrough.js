// Importing necessary module for reading input from console
const readline = require('readline');

// Creating an interface for input/output
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Welcome message
console.log("JavaScript Basics Walkthrough");

// Variables and Data Types
// Let's declare some basic variables
let aNumber = 10; // Number
let aString = "Hello, JavaScript!"; // String
let aBoolean = true; // Boolean

// Displaying the variables
console.log("Number: ", aNumber);
console.log("String: ", aString);
console.log("Boolean: ", aBoolean);

// Conditional Statements
// Using an if-else statement
if (aNumber > 5) {
    console.log(aNumber + " is greater than 5");
} else {
    console.log(aNumber + " is not greater than 5");
}

// Loops
// For loop example
console.log("For Loop from 1 to 5:");
for (let i = 1; i <= 5; i++) {
    console.log(i);
}

// While loop example
console.log("While Loop counting down from 5:");
let count = 5;
while (count > 0) {
    console.log(count);
    count--;
}

// Functions
// Defining a simple function
function square(number) {
    return number * number;
}

// Using the function
console.log("Square of 4 is: " + square(4));

// Reading input from the user
rl.question('Please enter a number to square: ', (answer) => {
    let inputNumber = parseInt(answer);
    console.log("Square of " + inputNumber + " is: " + square(inputNumber));

    // Closing the readline interface
    rl.close();
});

// End of the program
console.log("End of the JavaScript Walkthrough");
