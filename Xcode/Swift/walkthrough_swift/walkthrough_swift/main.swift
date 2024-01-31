// Swift Basics Walkthrough

// Importing necessary modules (not needed for this basic example)
import Foundation

// Declaring Variables and Constants

// Variables (can be changed)
var myVariable = 42
myVariable = 50

// Constants (cannot be changed)
let myConstant = 42

// Data Types

// Integer
let myInt: Int = 10

// Double (floating-point number)
let myDouble: Double = 3.14

// String
let myString: String = "Hello, Swift!"

// Boolean
let isTrue: Bool = true

// Arrays and Dictionaries

// Array of integers
var numbers: [Int] = [1, 2, 3, 4, 5]

// Dictionary (key-value pairs)
var personInfo: [String: Any] = ["name": "John", "age": 30, "isStudent": true]

// Control Flow

// If statement
if isTrue {
    print("It's true!")
} else {
    print("It's false!")
}

// For loop
for number in numbers {
    print(number)
}

// Switch statement
let fruit = "apple"
switch fruit {
case "apple":
    print("It's an apple.")
case "banana":
    print("It's a banana.")
default:
    print("It's something else.")
}

// Functions

// Define a function
func greet(name: String) -> String {
    return "Hello, \(name)!"
}

// Call a function
let greeting = greet(name: "Alice")
print(greeting)

// Optional Types

var optionalInt: Int? = 5 // Optional integer
if let unwrappedInt = optionalInt {
    print("The value is \(unwrappedInt)")
} else {
    print("The value is nil")
}

// Classes and Objects

// Define a class
class Person {
    var name: String
    var age: Int
    
    init(name: String, age: Int) {
        self.name = name
        self.age = age
    }
    
    func sayHello() {
        print("Hello, my name is \(name) and I am \(age) years old.")
    }
}

// Create an object
let person = Person(name: "Bob", age: 25)
person.sayHello()

// Optional Chaining

class Address {
    var street: String?
}

let myAddress = Address()
myAddress.street = "123 Main St"

if let street = myAddress.street {
    print("My street is \(street)")
} else {
    print("No street information available.")
}

// Enums

enum DayOfWeek {
    case monday
    case tuesday
    case wednesday
    case thursday
    case friday
    case saturday
    case sunday
}

let today = DayOfWeek.tuesday
print("Today is \(today)")

// Conclusion

print("Swift basics walkthrough complete!")
